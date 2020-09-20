# A collection of OpenCL helper functions that are common across both btcrpass and btcrseed (to avoid duplciation)
# btcrpass.py -- btcrecover main library
# Copyright (C) 2019-2020 Stephen Rothery
#
# This file is part of btcrecover.
#
# btcrecover is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version
# 2 of the License, or (at your option) any later version.
#
# btcrecover is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/

try:
    from lib.opencl_brute import opencl
    from lib.opencl_brute.opencl_information import opencl_information
    import pyopencl
except:
    pass

import btcrecover.btcrpass

def auto_select_opencl_platform(loaded_wallet):
    best_device_worksize = 0
    best_score_sofar = -1
    for i, platformNum in enumerate(pyopencl.get_platforms()):
        for device in platformNum.get_devices():
            cur_score = 0
            if device.type & pyopencl.device_type.ACCELERATOR:
                cur_score += 8  # always best
            elif device.type & pyopencl.device_type.GPU:
                cur_score += 4  # better than CPU
            if "nvidia" in device.vendor.lower():
                cur_score += 2  # is never an IGP: very good
            elif "amd" in device.vendor.lower():
                cur_score += 1  # sometimes an IGP: good
            if cur_score >= best_score_sofar:  # (intel is always an IGP)
                if cur_score > best_score_sofar:
                    best_score_sofar = cur_score
                    best_device = device.name
                    best_platform = i
                    if device.max_work_group_size > best_device_worksize:
                        best_device_worksize = device.max_work_group_size

    loaded_wallet.opencl_platform = best_platform
    loaded_wallet.opencl_device_worksize = best_device_worksize
    print("OpenCL: Auto Selecting Best Platform")

def init_opencl_contexts(loaded_wallet, openclDevice = 0):
    dklen = 64
    platform = loaded_wallet.opencl_platform
    debug = 0
    write_combined_file = False

    loaded_wallet.opencl_algo = opencl.opencl_algos(platform, debug, write_combined_file, inv_memory_density=1, openclDevice=openclDevice)

    if type(loaded_wallet) is btcrecover.btcrpass.WalletBlockchain:
        loaded_wallet.opencl_context_pbkdf2_sha1 = loaded_wallet.opencl_algo.cl_pbkdf2_init("sha1", len(
            loaded_wallet._salt_and_iv), dklen)
    elif type(loaded_wallet) is btcrecover.btcrpass.WalletBlockchainSecondpass:
        loaded_wallet.opencl_context_hash_iterations_sha256 = loaded_wallet.opencl_algo.cl_hash_iterations_init(
            "sha256")
    elif type(loaded_wallet) is btcrecover.btcrpass.WalletYoroi:
        loaded_wallet.opencl_context_pbkdf2_sha512 = loaded_wallet.opencl_algo.cl_pbkdf2_init("sha512", 32, 32)
    elif type(loaded_wallet) is btcrecover.btcrpass.WalletBitcoinCore:
        loaded_wallet.opencl_context_hash_iterations_sha512 = loaded_wallet.opencl_algo.cl_hash_iterations_init(
            "sha512")
    elif type(loaded_wallet) is btcrecover.btcrpass.WalletBIP38:
        loaded_wallet.opencl_context_scrypt = loaded_wallet.opencl_algo.cl_scrypt_init(14)
    elif type(loaded_wallet) in (btcrecover.btcrpass.WalletBIP39, btcrecover.btcrpass.WalletElectrum28):
        salt = b"mnemonic"
        loaded_wallet.opencl_context_pbkdf2_sha512 = loaded_wallet.opencl_algo.cl_pbkdf2_init("sha512",
                                                                                              len(salt), dklen)
    else: # Must a btcrseed.WalletBIP39
        loaded_wallet.opencl_context_pbkdf2_sha512 = []
        for salt in loaded_wallet._derivation_salts:
            loaded_wallet.opencl_context_pbkdf2_sha512.append(loaded_wallet.opencl_algo.cl_pbkdf2_init("sha512",
                                                                                              len(salt), dklen))