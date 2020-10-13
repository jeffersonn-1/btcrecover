# *btcrecover* - BIP-38 Version ![license](https://img.shields.io/badge/license-GPLv2-blue.svg) #

*btcrecover* is an open source wallet password and seed recovery tool. It is designed for the case where you already know most of your password or seed phrase, but need assistance in trying different possible combinations.

* Seed/Passphrase Recovery when for: (Recovery without a known address requires an [Address Database](docs/Creating_and_Using_AddressDB.md))
    * Bitcoin
    * Bitcoin Cash
    * Ethereum
    * Litecoin
    * Dash
    * Dogecoin
    * Vertcoin
    * Monacoin
    * DigiByte
    * Groestlcoin (Requires groestlcoin_hash module installed via PIP)
    * Ripple
    * Zilliqa
    * And many other 'Bitcoin Like' cryptos
 * [Descrambling 12 word seeds](docs/BIP39_descrambling_seedlists.md) (Using Tokenlist feature for BIP39 seeds via seedrecover.py)
 * Wallet File password recovery for a range of wallets

## Using BTCRecover with Altcoins, forks,clones or custom derivation paths

By default, seedrecover.py will check **the first account** using common Bitcoin derivation paths for BIP39 wallets derivation paths for any altcoins selected via the gui or specified via --wallet-type. You can also edit the files in the common-derivation-pathslists folder to either add, or remove derivation paths that will be searched. (To use the 2nd account, etc, you typically increment the last digit of the derivation path from /0 to /1)

You can also try to specifiy a custom derivation path for altcoins/forks which share the same address format as any supported coins.

[You can click here to view a list of the cryptos that are supported, along with the derivation paths they check by default.](common-derivation-pathlists)

If you want the tool to support a crypto that isn't listed above, please test that it works and submit a PR which includes a unit test for that coin and also any required code to accept the address format.

**_If you are trying to do a recovery for a coin that isn't listed above, feel free to contact me as it may be possible for you to sponsor the addition of that crypto as part of an assisted recovery fee._**


## Setup and Usage Tutorials ##
BTCRecover is a Python (3.6, 3.7, 3.8, 3.9) script so will run on Windows, Linux and Mac environments. [See the installation guide for more info](docs/INSTALL.md)

This repository also included some [example commands and file templates](docs/Usage_Examples/UsageExamples.md) for the usage scenarios covered in YouTube videos.

My suggestion is that you find a scenario that is most-like your situation and try to replicate my examples to ensure that you have the tool set up and running correctly. If you have a specific situation that isn't covered in these tutorials, let me know and I can look into creating a video for that.

You can reach me via the Code Warriors Telegram channel. (https://t.me/Code_Warriors)

If you don't know an address in the wallet that you are searching for, you can create and use an [Address Database (click here for guide)](docs/Creating_and_Using_AddressDB.md) _There is no real performance penalty for doing this, it just takes a bit more work to set up_.

## Quick Start ##

To try recovering your password or a BIP39 passphrase, please start with the **[Password Recovery Quick Start](TUTORIAL.md#btcrecover-tutorial)**.

If you mostly know your recovery seed/mnemonic (12-24 recovery words), but think there may be a mistake in it, please see the **[Seed Recovery Quick Start](docs/Seedrecover_Quick_Start_Guide.md)**.

## Thanks to Gurnec ##
This tool builds on the original work of Gurnec who created it and maintained it until late 2017. If you find *btcrecover* helpful, please consider a small donation to them too. (I will also be passing on a portion of any tips I recieve at the addys above to them too)

## Features ##
* BIP-38 Support
* Seed Phrase (Mnemonic) Recovery for the following wallets
     * [Electrum](https://electrum.org/) (1.x, 2.x, 3.x and 4.x) (For Legacy and Segwit Wallets. Set --bip32-path "m/0'/0" for a Segwit wallet, leave bip32-path blank for Legacy... No support for 2fa wallets...)
     * [Electron-Cash](https://www.electroncash.org/) (2.x, 3.x and 4.x)
     * BIP-32/39 compliant wallets ([bitcoinj](https://bitcoinj.github.io/)), including:
         * [MultiBit HD](https://multibit.org/)
         * [Bitcoin Wallet for Android/BlackBerry](https://play.google.com/store/apps/details?id=de.schildbach.wallet) (with seeds previously extracted by [decrypt\_bitcoinj\_seeds](https://github.com/gurnec/decrypt_bitcoinj_seed))
         * [Hive for Android](https://play.google.com/store/apps/details?id=com.hivewallet.hive.cordova), [for iOS](https://github.com/hivewallet/hive-ios), and [Hive Web](https://hivewallet.com/)
         * [Breadwallet](https://brd.com/)
     * BIP-32/39/44 Bitcoin & Ethereum compliant wallets, including:
         * [Mycelium for Android](https://wallet.mycelium.com/)
         * [TREZOR](https://www.bitcointrezor.com/)
         * [Ledger](https://www.ledgerwallet.com/)
         * [Keepkey](https://shapeshift.io/keepkey/)
         * [Jaxx](https://jaxx.io/)
         * [Coinomi](https://www.coinomi.com/)
         * [Exodus](https://www.exodus.io/)
         * [MyEtherWallet](https://www.myetherwallet.com/)
         * [Bither](https://bither.net/)
         * [Blockchain.com](https://blockchain.com/wallet)
 * Bitcoin wallet password recovery support for:
     * [Bitcoin Core](https://bitcoincore.org/)
     * [MultiBit HD](https://multibit.org/) and [MultiBit Classic](https://multibit.org/help/v0.5/help_contents.html)
     * [Electrum](https://electrum.org/) (1.x, 2.x, 3.x and 4.x) (For Legacy and Segwit Wallets. Set --bip32-path "m/0'/0" for a Segwit wallet, leave bip32-path blank for Legacy... No support for 2fa wallets...)
     * Most wallets based on [bitcoinj](https://bitcoinj.github.io/), including [Hive for OS X](https://github.com/hivewallet/hive-mac/wiki/FAQ)
     * BIP-39 passphrases, Bitcoin & Ethereum supported (e.g. [TREZOR](https://www.bitcointrezor.com/) & [Ledger](https://www.ledgerwallet.com/) passphrases)
     * [mSIGNA (CoinVault)](https://ciphrex.com/products/)
     * [Blockchain.com](https://blockchain.com/wallet)
     * [pywallet --dumpwallet](https://github.com/jackjack-jj/pywallet) of Bitcoin Unlimited/Classic/XT/Core wallets
     * [Bitcoin Wallet for Android/BlackBerry](https://play.google.com/store/apps/details?id=de.schildbach.wallet) spending PINs and encrypted backups
     * [KnC Wallet for Android](https://github.com/kncgroup/bitcoin-wallet) encrypted backups
     * [Bither](https://bither.net/)
 * Altcoin password recovery support for most wallets derived from one of those above, including:
     * [Litecoin Core](https://litecoin.org/)
     * [Electrum-LTC](https://electrum-ltc.org/) (For Legacy and Segwit Wallets. Set --bip32-path "m/0'/0" for a Segwit wallet, leave bip32-path blank for Legacy... No support for 2fa wallets...)
     * [Electron-Cash](https://www.electroncash.org/) (2.x, 3.x and 4.x)
     * [Litecoin Wallet for Android](https://litecoin.org/) encrypted backups
     * [Dogecoin Core](http://dogecoin.com/)
     * [MultiDoge](http://multidoge.org/)
     * [Dogecoin Wallet for Android](http://dogecoin.com/) encrypted backups
     * [Yoroi Wallet for Cardano](https://yoroi-wallet.com/#/) Master_Passwords extracted from the wallet data (In browser or on rooted/jailbroken phones)
 * [Free and Open Source](http://en.wikipedia.org/wiki/Free_and_open-source_software) - anyone can download, inspect, use, and redistribute this software
 * Supported on Windows, Linux, and OS X
 * Support for Unicode passwords and seeds
 * Multithreaded searches, with user-selectable thread count
 * Ability to spread search workload over multiple devices
 * [GPU acceleration](docs/GPU_Acceleration.md) for Bitcoin Core Passwords, Blockchain.com (Main and Second Password), Electrum Passwords + BIP39 and Electrum Seeds
 * Wildcard expansion for passwords
 * Typo simulation for passwords and seeds
 * Progress bar and ETA display (at the command line)
 * Optional autosave - interrupt and continue password recoveries without losing progress
 * Automated seed recovery with a simple graphical user interface
 * Ability to search multiple derivation paths simultaneously for a given seed via --pathlist command (example pathlist files in the )
 * “Offline” mode for nearly all supported wallets - use one of the [extract scripts (click for more information)](docs/Extract_Scripts.md) to extract just enough information to attempt password recovery, without giving *btcrecover* or whoever runs it access to *any* of the addresses or private keys in your Bitcoin wallet.
