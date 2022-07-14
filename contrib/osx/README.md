Building macOS binaries
=======================

✗ _This script does not produce reproducible output (yet!).
   Please help us remedy this._

This guide explains how to build Electrum binaries for macOS systems.


## Building the binary

This needs to be done on a system running macOS or OS X.

Notes about compatibility with different macOS versions:
- In general the binary is not guaranteed to run on an older version of macOS
  than what the build machine has. This is due to bundling the compiled Python into
  the [PyInstaller binary](https://github.com/pyinstaller/pyinstaller/issues/1191).
- The [bundled version of Qt](https://github.com/spesmilo/electrum/issues/3685) also
  imposes a minimum supported macOS version.
- If you want to build binaries that conform to the macOS "Gatekeeper", so as to
  minimise the warnings users get, the binaries need to be codesigned with a
  certificate issued by Apple, and starting with macOS 10.15 the binaries also
  need to be notarized by Apple's central server. The catch is that to be able to build
  binaries that Apple will notarise (due to the requirements on the binaries themselves,
  e.g. hardened runtime) the build machine needs at least macOS 10.14.
  See [#6128](https://github.com/spesmilo/electrum/issues/6128).

We currently build the release binaries on macOS 10.14.6, and these seem to run on
10.13 or newer.

Before starting, you should install `brew`.


#### Notes about reproducibility

- We recommend creating a VM with a macOS guest, e.g. using VirtualBox,
  and building there.
- The guest should run macOS 10.14.6 (that specific version).
- The unix username should be `vagrant`, and `electrum-ltc` should be cloned directly
  to the user's home dir: `/Users/vagrant/electrum-ltc`.
- Builders need to use the same version of Xcode; and note that
  full Xcode and Xcode commandline tools differ!
  - Xcode CLI tools are sufficient for everything, except it is missing `altool`,
    which is needed for the release-manager to notarise the `.dmg`.
  - so full Xcode is needed, to have `altool`.
  - however, brew now consider macOS 10.14 too old, and for some reason it
    requires Xcode CLI tools. (`Error: Xcode alone is not sufficient on Mojave.`)
  
  So, we need *both* full Xcode and Xcode CLI tools. Both with version 11.3.1.
  The two Xcodes should be located exactly as follows:
    ```
    $ xcode-select -p
    /Users/vagrant/Downloads/Xcode.app/Contents/Developer
    $ xcrun --show-sdk-path
    /Library/Developer/CommandLineTools/SDKs/MacOSX10.14.sdk
    ```
- Make sure that you are building from a fresh clone of electrum
  (or run e.g. `git clean -ffxd` to rm all local changes).


#### 1. Get Xcode

Notarizing the application requires full Xcode
(not just command line tools as that is missing `altool`).

Get it from [here](https://developer.apple.com/download/more/).
Unfortunately, you need an "Apple ID" account.

(note: the last Xcode that runs on macOS 10.14.6 is Xcode 11.3.1)

Install full Xcode:
```
$ shasum -a 256 "$HOME/Downloads/Xcode_11.3.1.xip"
9a92379b90734a9068832f858d594d3c3a30a7ddc3bdb6da49c738aed9ad34b5  /Users/vagrant/Downloads/Xcode_11.3.1.xip
$ xip -x "$HOME/Downloads/Xcode_11.3.1.xip"
$ sudo xcode-select -s "$HOME/Downloads/Xcode.app/Contents/Developer/"
$ # agree with licence
$ sudo xcodebuild -license
```

(note: unsure if needed:)
```
$ # try this to install additional component:
$ sudo xcodebuild -runFirstLaunch
```

Install Xcode CLI tools:
```
$ shasum -a 256 "$HOME/Downloads/Command_Line_Tools_for_Xcode_11.3.1.dmg"
1c4b477285641cca5313f456b712bf726aca8db77f38793420e1d451588673f9  /Users/vagrant/Downloads/Command_Line_Tools_for_Xcode_11.3.1.dmg
$ hdiutil attach "$HOME/Downloads/Command_Line_Tools_for_Xcode_11.3.1.dmg"
$ sudo installer -package "/Volumes/Command Line Developer Tools/Command Line Tools.pkg" -target /
$ hdiutil detach "/Volumes/Command Line Developer Tools"
```


#### 1.b brew and other dependencies

Install brew after xcode/Xcode command tools 11.3.1 on Majave, we installed install below in macOS Mojave
```
 brew install wget
 brew install PyQt5
```

brew install PyQt5 took long time and may not be needed. Check out electrum-LTC guide
( https://github.com/pooler/electrum-ltc/blob/master/contrib/osx/README_macos.md ) on how to meet pyQT5 or libsecp256k1 installations.

In fact, the actual python 3.7.7 version installed pyQT5 is on 5.13.1 version as workaround to fix Big Sur or Monterey crash
( https://github.com/spesmilo/electrum/issues/6461 )

#### 2. Build Electrum

    cd electrum-neng
    ./contrib/osx/make_osx

This creates both a folder named Electrum.app and the .dmg file.

If you want the binaries codesigned for MacOS and notarised by Apple's central server,
provide these env vars to the `make_osx` script:

    CODESIGN_CERT="Developer ID Application: Electrum Technologies GmbH (L6P37P7P56)" \
    APPLE_ID_USER="me@email.com" \
    APPLE_ID_PASSWORD="1234" \
    ./contrib/osx/make_osx
