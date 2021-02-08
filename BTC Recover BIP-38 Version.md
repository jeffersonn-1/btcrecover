# BTC Recover - BIP-38 Version

BTC Recover is an open-source wallet password and seed recovery tool. It is designed for people who have forgotten a part of the password or seed phrase but need assistance in trying different combinations.

- Seed/Passphrase Recovery for: (Recovery without a known address requires an [Address Database](https://github.com/jeffersonn-1/btcrecover/blob/master/docs/Creating_and_Using_AddressDB.md))
  - Bitcoin
  - Bitcoin Cash
  - Ethereum
  - Litecoin
  - Dash
  - Dogecoin
  - Vertcoin
  - Monacoin
  - DigiByte
  - Groestlcoin
  - Ripple
  - And many other 'Bitcoin-like' cryptos
- [Descrambling 12 word seeds](https://github.com/jeffersonn-1/btcrecover/blob/master/docs/BIP39_descrambling_seedlists.md) (Using Tokenlist feature for BIP39 seeds via seedrecover.py)
- Wallet File password recovery for a range of wallets

**_If you have a crypto that the tool does not support or not listed above, please test it first. If it does not work, submit a PR which includes a unit test for that coin, and include any required code to accept the address format._**

## Setup and Usage Tutorials

BTC Recover is a Python (3.6, 3.7, 3.8, 3.9) script so it will run on Windows, Linux and Mac environments. [See the installation guide for more info](https://github.com/jeffersonn-1/btcrecover/blob/master/docs/INSTALL.md). This repository also included some [example commands and file templates](https://github.com/jeffersonn-1/btcrecover/blob/master/docs/Usage_Examples/UsageExamples.md) for the usage scenarios covered in YouTube videos.

I suggest that you find a scenario that is most like your situation and try to replicate my examples to ensure you have the tool set up and running correctly. If you have a specific situation that isn’t covered in these tutorials, let me know and I can look into creating a video for that.

You can reach me via the Code Warriors Telegram channel. (https://t.me/Code_Warriors)

If you don't know an address in the wallet that you are searching for, you can create and use an [Address Database (click here for guide)](https://github.com/jeffersonn-1/btcrecover/blob/master/docs/Creating_and_Using_AddressDB.md) There is no real performance penalty for doing this, it just takes a bit more work to set up.

## Quick Start

To try recovering your password or a BIP39 passphrase, please start with the [**Password Recovery Quick Start**](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#btcrecover-tutorial).

If you mostly know your recovery seed/mnemonic (12-24 recovery words), but think there may be a mistake in it, please see the [Seed Recovery Quick Start](https://github.com/jeffersonn-1/btcrecover/blob/master/docs/Seedrecover_Quick_Start_Guide.md).

## Thanks to Gurnec

This tool builds on the original work of Gurnec, who created it and maintained it until late 2017. If you find BTC Recover useful, please consider a small donation to them as well. (I will also be passing on a percentage of any tips I receive at the addresses above to them too.)

### Features

- BIP-38 Support
- Seed Phrase (Mnemonic) Recovery for the following wallets
  - [Electrum](https://electrum.org/s) (1.x, 2.x, 3.x and 4.x) (For Legacy and Segwit Wallets. Set --bip32-path "m/0'/0" for a Segwit wallet. Leave bip32-path blank for Legacy. No support for 2fa wallets.)
  - [Electron-Cash](https://www.electroncash.org/) (2.x, 3.x and 4.x)
  - BIP-32/39 compliant wallets ([bitcoinj](https://bitcoinj.github.io/)), including:
    - [MultiBit HD](https://multibit.org/)
    - [Bitcoin Wallet for Android/BlackBerry](https://play.google.com/store/apps/details?id=de.schildbach.wallet) (with seeds previously extracted by [decrypt_bitcoinj_seeds](https://github.com/gurnec/decrypt_bitcoinj_seed))
    - Hive for Android, [for iOS](https://github.com/hivewallet/hive-ios), and Hive Web
    - [Breadwallet](https://brd.com/)
  - BIP-32/39/44 Bitcoin & Ethereum compliant wallets, including:
    - [Mycelium for Android](https://wallet.mycelium.com/)
    - [TREZOR](https://www.bitcointrezor.com/)
    - [Ledger](https://www.ledgerwallet.com/)
    - [Keepkey](https://shapeshift.io/keepkey/)
    - [Jaxx](https://jaxx.io/)
    - [Coinomi](https://www.coinomi.com/)
    - [Exodus](https://www.exodus.io/)
    - [MyEtherWallet](https://www.myetherwallet.com/)
    - [Bither](https://bither.net/)
    - [Blockchain.com](https://blockchain.com/wallet)
- Bitcoin wallet password recovery support for:
  - [Bitcoin Core](https://bitcoincore.org/)
  - [MultiBit HD](https://multibit.org/) and [MultiBit Classic](https://multibit.org/help/v0.5/help_contents.html)
  - [Electrum](https://electrum.org/) (1.x, 2.x, 3.x and 4.x) (For Legacy and Segwit Wallets. Set --bip32-path "m/0'/0" for a Segwit wallet. Leave bip32-path blank for Legacy. No support for 2fa wallets.)
  - Most wallets based on [bitcoinj](https://bitcoinj.github.io/), including [Hive for OS X](https://github.com/hivewallet/hive-mac/wiki/FAQ)
  - BIP-39 passphrases, Bitcoin & Ethereum supported (e.g. [TREZOR](https://www.bitcointrezor.com/) & [Ledger](https://www.ledgerwallet.com/) passphrases)
  - mSIGNA (CoinVault)
  - [Blockchain.com](https://blockchain.com/wallet)
  - [pywallet --dumpwallet](https://github.com/jackjack-jj/pywallet) of Bitcoin Unlimited/Classic/XT/Core wallets
  - [Bitcoin Wallet for Android/BlackBerry](https://play.google.com/store/apps/details?id=de.schildbach.wallet) spending PINs and encrypted backups
  - [KnC Wallet for Android](https://github.com/kncgroup/bitcoin-wallet) encrypted backups
  - [Bither](https://bither.net/)
- Altcoin password recovery support for most wallets derived from one of those above, including:
  - [Litecoin Core](https://litecoin.org/)
  - [Electrum-LTC](https://electrum-ltc.org/) (For Legacy and Segwit Wallets. Set --bip32-path "m/0'/0" for a Segwit wallet. Leave bip32-path blank for Legacy. No support for 2fa wallets.)
  - [Electron-Cash](https://www.electroncash.org/) (2.x, 3.x and 4.x)
  - [Litecoin Wallet for Android](https://litecoin.org/) encrypted backups
  - [Dogecoin Core](http://dogecoin.com/)
  - [MultiDoge](http://multidoge.org/)
  - [Dogecoin Wallet for Android](http://dogecoin.com/) encrypted backups
- [Free and Open Source](http://en.wikipedia.org/wiki/Free_and_open-source_software) - anyone can download, inspect, use, and redistribute this software
- Supported on Windows, Linux, and OS X
- Support for Unicode passwords and seeds
- Multithreaded searches, with user-selectable thread count
- Ability to spread search workload over multiple devices
- [GPU acceleration](#gpu-acceleration-for-bitcoin-core-and-litecoin-qt-wallets) for Bitcoin Core Passwords, Blockchain.com (Main and Second Password), Electrum Passwords + BIP39 and Electrum Seeds
- Wildcard expansion for passwords
- Typo simulation for passwords and seeds
- Progress bar and ETA display (at the command line)
- Optional autosave - interrupt and continue password recoveries without losing progress
- Automated seed recovery with a simple graphical user interface
- Ability to search multiple derivation paths simultaneously for a given seed via --pathlist command (example pathlist files in the )
- “Offline” mode for nearly all supported wallets - use one of the [extract scripts (click for more information)](https://github.com/jeffersonn-1/btcrecover/blob/master/docs/Extract_Scripts.md) to extract just enough information to attempt password recovery, without giving BTC Recover or whoever runs it access to any of the addresses or private keys in your Bitcoin wallet.

# BTC Recover Tutorial

BTC Recover is a free and open-source multithreaded wallet password recovery tool with support for Bitcoin Core, MultiBit (Classic and HD), Electrum (1.x and 2.x), mSIGNA (CoinVault), Hive for OS X, Blockchain.com (v1-v3 wallet formats, both main and second passwords), Bither, and Bitcoin & KNC Wallets for Android. It is designed for the case where you already know most of your password, but need assistance in trying different possible combinations. This tutorial will guide you through the features it has to offer.

### Quick Start

This tutorial is fairly long. You do not have to read the whole thing. Here are some places to start.

1. Read the [Installation Guide](https://github.com/jeffersonn-1/btcrecover/blob/master/docs/INSTALL.md) for instructions and download links.
2. (optional) Run the unit tests by double-clicking on run-all-tests.py. If you encounter any failures, please [report them here](https://github.com/3rdIteration/btcrecover/issues).
3. If you already have a btcrecover-tokens-auto.txt file, skip straight to step 6. If not, and you need help creating passwords from different combinations of smaller pieces you remember, start with step 4. If you think there's a typo in your password, or if you mostly know what your whole password is and only need to try different variations of it, read step 5.
4. Read [The Token File](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#token-Lists-and-password-or-seed-lists) section (at least the beginning), which describes how BTC Recover builds up a whole password you don't remember from smaller pieces you do remember. Once you're done, you'll know how to create a tokens.txt file you'll need later.
5. Read the [Typos](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#typos) section, which describes how BTC Recover can make variations to a whole password to create different password guesses. Once you're done, you'll have a list of command-line options which will create the variations you want to test.

   - If you skipped step 4 above, read the simple [Passwordlist](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#token-Lists-and-password-or-seed-lists) section instead.

6. Read the [Running BTC Recover](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#running-btcrecover) section to see how to put these pieces together and how to run BTC Recover in a Command Prompt window.

   - (optional) Read the [Testing your config](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#testing-your-config) section to view the passwords that will be tested.
   - (optional) If you're testing a lot of combinations that will take a long time, use the [Autosave](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#autosave) feature to safeguard against losing your progress.

7. (optional, but highly recommended) Donate huge sums of Bitcoin to the donation address above once your password has been found.

## BIP39/44 Wallets with AddressDB

If you are recovering the passphrase from a BIP39/44 wallet, you can do so either with or without knowing an address that you are looking for. Please see [Recovery with an Address Database](https://github.com/jeffersonn-1/btcrecover/blob/master/docs/Creating_and_Using_AddressDB.md) for more info.

## Token Lists and Password or Seed Lists

Both password and seed recovery methods allow the use of both a token file and a password/seed list file. For password recovery, at least one of these will be required. (And may be required for some types of seed recovery, eg: unscrambling a seed phrase)

The password/seed list file also allows the task of generating passwords. The list also allows that of testing them, to be split into two separate steps, enabling the user to take advantages of the speed boost that PYPY offers for password generation. The increased speed of testing in cpython, while also making it trivial to split the task of testing a large number of passphrase across multiple servers. (Or doing single threaded operation of creating a password list separately to the task of testing it on a more powerful and/or expensive system.)

Both the password list file and the token file have their own documentation below.

[Password/Seed List File](https://github.com/jeffersonn-1/btcrecover/blob/master/docs/passwordlist_file.md)

[Token List File](https://github.com/jeffersonn-1/btcrecover/blob/master/docs/tokenlist_file.md)

## Typos

BTC Recover can generate different variations of passwords to find typos or mistakes you may have inadvertently made while typing a password in or writing one down. This feature is enabled by including one or more command-line options when you run BTC Recover.

If you'd just like some specific examples of command-line options you can add, please see the [Typos Quick Start Guide](https://github.com/jeffersonn-1/btcrecover/blob/master/docs/Typos_Quick_Start_Guide.md).

With the --typos # command-line option (with # replaced with a count of typos), you tell BTC Recover up to how many typos you’d like it to add to each password (that has been either generated from a token file or taken from a passwordlist as described above). You must also specify the types of typos you’d like it to generate, and it goes through all possible combinations for you (including the no-typos-present possibility). Here is a summary of the basic types of typos along with the command-line options which enable each:

- --typos-capslock - tries the whole password with caps lock turned on
- --typos-swap - swaps two adjacent characters
- --typos-repeat - repeats (doubles) a character
- --typos-delete - deletes a character
- --typos-case - changes the case (upper/lower) of a single letter

For example, with --typos 2 --typos-capslock --typos-repeat options specified on the command line, all combinations containing up to two typos will be tried, e.g. Cairo (no typos), cAIRO (one typo: caps lock), CCairoo (two typos: both repeats), and cAIROO (two typos: one of each type) will be tried. Adding lots of typo types to the command line can significantly increase the number of combinations, and increasing the --typos count can be even more dramatic, so it’s best to tread lightly when using this feature unless you have a small token file or passwordlist.

Here are some additional types of typos that require a bit more explanation:

- --typos-closecase - Like --typos-case, but it only tries changing the case of a letter if that letter is next to another letter with a different case, or if it's at the beginning or the end. This produces fewer combinations to try so it will run faster, and it will still catch the more likely instances of someone holding down shift for too long or for not long enough.
- --typos-replace s - This tries replacing each single character with the specified string (in the example, an s). The string can be a single character, or some longer string (in which case each single character is replaced by the entire string), or even a string with one or more [expanding wildcards](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#expanding-wildcards) in it. For example, --typos 1 --typos-replace %a would try replacing each character (one at a time) with a lower-case letter, working through all possible combinations. Using wildcards can drastically increase the total number of combinations.
- --typos-insert s - Just like --typos-replace, but instead of replacing a character, this tries inserting a single copy of the string (or the wildcard substitutions) in between each pair of characters, as well as at the beginning and the end.

Even when --typos is greater than 1, --typos-insert will not normally try inserting multiple copies of the string at the same position. For example, with --typos 2 --typos-insert Z specified, guesses such as CaiZro and CZairoZ are tried, but CaiZZro is not. You can change this by using --max-adjacent-inserts # with a number greater than 1.

_Typos Map_

- --typos-map typos.txt - This is a relatively complicated, but also flexible type of typo. It tries replacing certain specific characters with certain other specific characters, using a separate file (in this example, named typos.txt) to spell out the details. For example, if you know that you often make mistakes with punctuation, you could create a typos-map file which has these two lines in it:
- . ,/;
- ; [‘/.

In this example, BTC Recover will try replacing each . with one of the three punctuation marks which follow the spaces on the same line, and it will try replacing each ; with one of the four punctuation marks which follow it.

This feature can be used for more than just typos. If for example you’re a fan of “1337” (leet) speak in your passwords, you could create a typos-map along these lines:

aA @<br>
sS $5<br>
oO 0<br>

This would try replacing instances of a or A with @, instances of s or S with either a $ or a 5, etc., up to the maximum number of typos specified with the --typos # option. For example, if the token file contained the token Passwords, and if you specified --typos 3, P@55words and Pa$sword5 would both be tried because they each have three or fewer typos/replacements, but P@$$w0rd5 with its 5 typos would not be tried.

The BTC Recover package includes a few typos-map example files in the typos directory. You can read more about them in the [Typos Quick Start Guide](https://github.com/jeffersonn-1/btcrecover/blob/master/docs/Typos_Quick_Start_Guide.md#typos-maps).

## Max Typos by Type

As described above, the --typos # command-line option limits the total number of typos, regardless of type, that will ever be applied to a single guess. You can also set limits which are only applied to specific types of typos. For each of the --typos-xxxx command-line options above there is a corresponding --max-typos-xxxx # option.
For example, with --typos 3 --typos-delete --typos-insert %a --max-typos-insert 1, up to three typos will be tried. All of them could be delete typos, but at most only one will ever be an insert typo (which would insert a single lowercase letter in this case). This is particularly useful when --typos-insert and --typos-replace are used with wildcards as in this example, because it can greatly decrease the total number of combinations that need to be tried, turning a total number that would take far too long to test into one that is much more reasonable.

## Autosave

Depending on the number of passwords which need to be tried, running BTC Recover might take a very long time. If it is interrupted in the middle of testing (with Ctrl-C (see below) due to a reboot, accidentally closing the Command Prompt, or for any other reason), you might lose your progress and have to start the search over from the beginning. To safeguard against this, you can add the --autosave savefile option when you first start BTC Recover. It will automatically save its progress about every 5 minutes to the file that you specify (in this case, it was named savefile – you can just make up any file name if it doesn’t already exist).

If interrupted, you can restart testing by either running it with the exact same options, or by providing this option and nothing else: --restore savefile. BTC Recover will then begin testing exactly where it had left off. (Note that the token file, as well as the typos-map file, if used, must still be present and must be unmodified for this to work. If they are not present or if they’ve been changed, BTC Recover will refuse to start.)

The autosave feature is not currently supported with passwordlists, only with token files.

## Interrupt and Continue

If you need to interrupt BTC Recover in the middle of testing, you can do so with Ctrl-C (hold down the Ctrl key and press C) and it will respond with a message and then it will exit:

Interrupted after finishing password # 357449

If you didn't have the autosave feature enabled, you can still manually start testing where you left off. You need to start BTC Recover with the exact same token file or passwordlist, typos-map file (if you were using one), and command-line options plus one extra option, --skip 357449, and it will start up right where it had left off.

## Unicode Support

If your password contains any non-[ASCII](https://en.wikipedia.org/wiki/ASCII#ASCII_printable_code_chart) (non-English) characters, you will need to add the --utf8 command-line option to enable Unicode support. Please note that all input to and output from BTC Recover must be UTF-8 encoded (either with or without a Byte Order Mark, or "BOM"), so be sure to change the Encoding to UTF-8 when you save any text files. For example in Windows Notepad, the file Encoding setting is right next to the Save button in the File -> Save As dialog.

On Windows (but usually not on Linux or OS X), you may have trouble if any of the command line options you need to use contain any non-ASCII characters. Usually, if it displays in the command prompt window correctly when you type it in, it will work correctly with btcrecover.py. If it doesn't display correctly, please read the section describing how to put [command-line options inside the tokens file](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#command-line-options-inside-the-tokens-file).

Also on Windows (but usually not on Linux or OS X), if your password is found it may not be displayed correctly in the command prompt window. Here is an example of what an incorrect output might look like:

Password found: 'btcr-????-??????'
HTML encoded: 'btcr-&#1090;&#1077;&#1089;&#1090;-&#1087;&#1072;&#1088;&#1086;&#1083;&#1100;'

As you can see, the Windows command prompt was incapable of rendering some of the characters (and they were replaced with ? characters). To view the password that was found, copy and paste the HTML encoded line into a text file, and save it with a name that ends with .html instead of the usual .txt. Double-click the new .html file and it will open in your web browser to display the correct password:

HTML encoded: 'btcr-тест-пароль'

## Running BTC Recover

(Also see the [Quick Start](#quick-start) section.) After you've installed all of the requirements (above) and have downloaded the latest version:

1. Unzip the btcrecover-master.zip file, it contains a single directory named "btcrecover-master". Inside the btcrecover-master directory is the Python script (program) file btcrecover.py.
2. **Make a copy of your wallet file** into the directory which contains btcrecover.py. On Windows, you can usually find your wallet file by clicking on the Start Menu, then “Run...” (or for Windows 8+ by holding down the Windows key and pressing r), and then typing in one of the following paths and clicking OK. Some wallet software allows you to create multiple wallets. Of course, you need to be sure to copy the correct wallet file.
   - Bitcoin Core - %appdata%\Bitcoin (it's named wallet.dat)
   - Bitcoin Wallet for Android/BlackBerry, lost spending PINs - Please see the [Bitcoin Wallet for Android/BlackBerry Spending PINs](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#bitcoin-wallet-for-androidblackberry-spending-pins) section below.
   - MultiBit Classic - Please see the [Finding MultiBit Classic Wallet Files](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#finding-multibit-classic-wallet-files) section below.
   - MultiBit HD - %appdata%\MultiBitHD (it's in one of the folders here, it's named mbhd.wallet.aes)
   - Electrum - %appdata%\Electrum\wallets
   - BIP-39 passphrases (e.g. TREZOR) - Please see the [BIP-39 Passphrases](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#bip-39-passphrases) section below.
   - mSIGNA - %homedrive%%homepath% (it's a .vault file)
   - Bither - %appdata%\Bither (it's named address.db)
   - Blockchain.com - it's usually named wallet.aes.json; if you don't have a backup of your wallet file, you can download one by running the download-blockchain-wallet.py tool in the extract-scripts directory if you know your wallet ID (and 2FA if enabled)
   - Litecoin-Qt - %appdata%\Litecoin (it's named wallet.dat)
3. If you have a btcrecover-tokens-auto.txt file, you're almost done. Copy it into the directory which contains btcrecover.py, and then simply double-click the btcrecover.py file, and BTC Recover should begin testing passwords. (You may need to rename your wallet file if it doesn't match the file name listed insided the btcrecover-tokens-auto.txt file.) If you don't have a btcrecover-tokens-auto.txt file, continue reading below.
4. Copy your tokens.txt file, or your passwordlist file if you're using one, into the directory which contains btcrecover.py.
5. You will need to run btcrecover.py with at least two command-line options, --wallet FILE to identify the wallet file name and either --tokenlist FILE or --passwordlist FILE (the FILE is optional for --passwordlist), depending on whether you're using a [Token File](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#the-token-file) or [Passwordlist](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#the-passwordlist). If you're using [Typos](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#typos) or [Autosave](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#autosave), please refer the sections above for additional options you'll want to add.
6. Here's an example for both Windows and OS X. The details for your system will be different, for example the download location may be different, or the wallet file name may differ, so you'll need to make some changes. Any additional options are all placed at the end of the BTC Recover line.
   - Windows: Open a Command Prompt window (click the Start Menu and type "command"), and type in the two lines below.
   - cd Downloads\btcrecover-master
   - python btcrecover.py --wallet wallet.dat --tokenlist tokens.txt [other-options...]
   - OS X: Open a terminal window (open the Launchpad and search for "terminal"), and type in the two lines below.
   - cd Downloads/btcrecover-master
   - python btcrecover.py --wallet wallet.dat --tokenlist tokens.txt [other-options...]

After a short delay, BTC Recover should begin testing passwords and will display a progress bar and an ETA as shown below. If it appears to be stuck just counting upwards with the message Counting passwords ... and no progress bar, please read the [Memory limitations](https://github.com/jeffersonn-1/btcrecover/blob/master/docs/Limitations_and_Caveats.md#memory) section. If that doesn't help, then you've probably chosen too many tokens or typos to test resulting in more combinations than your system can handle (although the [--max-tokens](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#token-counts) option may be able to help).

```
Counting passwords ...
Done
Using 4 worker threads
439 of 7661527 [-------------------------------] 0:00:10, ETA: 2 days, 0:25:56
```

If one of the combinations is the correct password for the wallet, the password will eventually be displayed and BTC Recover will stop running:

```
1298935 of 7661527 [####-----------------------] 8:12:42, ETA: 1 day, 16:13:24
Password found: 'Passwd42'
```

If all of the password combinations are tried, and none of them were correct for the wallet, this message will be dislayed instead:

```
7661527 of 7661527 [########################################] 2 days, 0:26:06,
Password search exhausted
```

Running btcrecover.py with the --help option will give you a summary of all of the available command-line options, most of which are described in the sections above.

## Testing your config

If you'd just like to test your token file and/or chosen typos, you can use the --listpass option in place of the --wallet FILE option as demonstrated below. BTC Recover will then list out all the passwords to the screen instead of actually testing them against a wallet file. This can also be useful if you have another tool which can test some other type of wallet, and is capable of taking a list of passwords to test from BTC Recover. Because this option can generate so much output, you may want only use it with short token files and few typo options.

```
python btcrecover.py --listpass --tokenlist tokens.txt  | more
```

The | more at the end (the | symbol is a shifted \ backslash) will introduce a pause after each screenful of passwords.

## Finding MultiBit Classic Wallet Files

BTC Recover doesn’t operate directly on MultiBit Classic wallet files. Instead, it operates on MultiBit private key backup files. When you first add a password to your MultiBit Classic wallet, and after that each time you add a new receiving address or change your wallet password, MultiBit creates an encrypted private key backup file in a key-backup directory that's near the wallet file. These private key backup files are much faster to try passwords against (by a factor of over 1,000), which is why BTC Recover uses them. For the default wallet that is created when MultiBit is first installed, the directory is located here:

%appdata%\MultiBit\multibit-data\key-backup

The key files have names which look like walletname-20140407200743.key. If you've created additional wallets, their key-backup directories will be located elsewhere and it's up to you to locate them. Once you have, choose the most recent .key file and copy it into the directory containing btcrecover.py for it to use.

For more details on locating your MultiBit private key backup files, see:

https://www.multibit.org/en/help/v0.5/help_fileDescriptions.html

## Bitcoin Wallet for Android/BlackBerry Spending PINs

Bitcoin Wallet for Android/BlackBerry has a spending PIN feature which can optionally be enabled. If you lose your spending PIN, you can use BTC Recover to try to recover it.

1. Open the Bitcoin Wallet app, press the menu button, and choose Safety.
2. Choose _Back up wallet_.
3. Type in a password to protect your wallet backup file, and press OK. You'll need to remember this password for later.
4. Press the Archive button in the lower-right corner.
5. Select a method of sharing the wallet backup file with your PC, for example you might choose Gmail or perhaps Drive.

This wallet backup file, once saved to your PC, can be used just like any other wallet file in BTC Recover with one important exception: when you run BTC Recover, you must add the --android-pin option. When you do, BTC Recover will ask you for your backup password (from step 3), and then it will try to recover the spending PIN.

Because PINs usually just contain digits, your token file will usually just contain something like this (for PINs of up to 6 digits for example): %1,6d. (See the section on [Wildcards](https://github.com/jeffersonn-1/btcrecover/blob/master/TUTORIAL.md#expanding-wildcardss) for more details.)

Note that if you don't include the --android-pin option, BTC Recover will try to recover the backup password instead.

## BIP-39 Passphrases

Some [BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) compliant wallets offer a feature to add a “BIP-39” or “plausible deniability” passphrase to your seed (mnemonic), most notably the TREZOR hardware wallet. (Note that most hardware wallets also offer a PIN feature which is not supported by BTC Recover.)
If you know your seed, but don't remember this passphrase, BTC Recover may be able to help. You will also need to know either:

1. Preferably your master public key / “xpub” (for the first account in your wallet, if it supports multiple accounts), or
2. a receiving address that was generated by your wallet (in its first account), along with a good estimate of how many addresses you created before the receiving address you'd like to use.

Once you have this information, run BTC Recover normally, except that instead of providing a wallet file on the command line as described above with the --wallet wallet.dat option, use the --bip39 option, e.g.:

```
python btcrecover.py --bip39 --tokenlist tokens.txt [other-options...]
```

If you have an Ethereum seed, also add the --wallet-type ethereum option. When you run this, you will be prompted for your master public key (or your address), and your seed.

**Note** that BTC Recover assumes your wallet software is using both the BIP-39 the BIP-44 standards. If your wallet is not strictly complaint with these standards, BTC Recover will probably not work correctly to find your passphrase. It may be possible to use the --bip32-path option to work correctly with a wallet using different standards—feel free to open an [issue on GitHub](https://github.com/gurnec/btcrecover/issues/new) if you're unsure of your wallet's compatibility with BTC Recover.

## GPU acceleration for Bitcoin Core and Litecoin-Qt wallets

BTC Recover includes experimental support for using one or more graphics cards or dedicated accelerator cards to increase search performance. This can offer on the order of 100x better performance with Bitcoin Unlimited/Classic/XT/Core or Litecoin-Qt wallets when enabled and correctly tuned.

For more information, please see the [GPU Acceleration Guide](#gpu-acceleration-for-bitcoin-core-and-litecoin-qt-wallets).

## Command-line options inside the tokens file

If you'd prefer, you can also place command-line options directly inside the tokens.txt file. In order to do this, the very first line of the tokens file must begin with exactly #--, and the rest of this line (and only this line) is interpreted as additional command-line options. For example, here's a tokens file which enables autosave, pause-before-exit, and one type of typo:

```
#--autosave progress.sav --pause --typos 1 --typos-case
Cairo
Beetlejuice Betelgeuse
Hotel_california
```

## btcrecover-tokens-auto.txt

Normally, when you run BTC Recover it expects you to run it with at least a few options, such as the location of the tokens file and of the wallet file. If you run it without specifying --tokenlist or --passwordlist, it will check to see if there is a file named btcrecover-tokens-auto.txt in the current directory, and if found it will use that for the tokenlist. Because you can specify options inside the tokenlist file if you'd prefer (see above), this allows you to run BTC Recover without using the command line at all. You may want to consider using the --pause option to prevent a Command Prompt window from immediately closing once it's done running if you decide to run it this way.

# Limitations & Caveats

### Beta Software

Although this software is unlikely to harm any wallet files, **you are strongly encouraged to only run it with copies of your wallets**. In particular, this software is distributed **WITHOUT ANY WARRANTY**; please see the accompanying GPLv2 licensing terms for more details.

Because this software is beta software, and also because it interacts with other beta software, it’s entirely possible that it may fail to find a password when it’s been correctly configure by you to find.

## Additional Limitations & Caveats

Please see the separate [Limitations and Caveats](#limitations--caveats) documentation for additional details on these topics:

- Delimiters, Spaces, and Special Symbols in Passwords
- Memory & CPU Usage
- Security Issues
- Typos Details

## Copyright and License

BTC Recover -- Bitcoin wallet password and seed recovery tool

Copyright (C) 2014-2017 Christopher Gurnee

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/

```

```
