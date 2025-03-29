Build Binary Release for Electrum-NENG on Windows/Linux/MacOS/Chromebook
============================


## Linux
For linux binary release, follow "contrib/build-linux/appimage/README.md"
 using docker method. The appimage result file is statically linked and should be runnable in any x64 linux version OS. 

## Chromebook

The linux appimage file should be runnable in x64 Chromebook with linux enabled.
###### Workaround on Chromebook Errors

The newest version of Chromebook will generate QT errors when running linux appimage release file. The errors are like below
```
QObject::connect: No such signal QPlatformNativeInterface
xkbcommon: ERROR: Key "<CAPS>"
qt.qpa.wayland: ...
```
The QT xkb and wayland errors can be fixed by patching two lines at ".bashrc", run below in chromebook terminal
```commandline
echo "export QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb" >> ~/.bashrc
echo "export QT_QPA_PLATFORM=xcb" >>  ~/.bashrc
```
Exit the chromebook terminal and restart a new terminal.

## Windows
For windows 10 binary release, follow "contrib/build-wine/README.md" using wine cross building method.

## MacOS
For macOS binary release, follow "contrib/osx/README.md"


### Electrum-NENG Wallet Server Connection Issues

When electrumX server back end has an upgrade, or the server URL changed, you may need to delete old certificate by following this guide to clear the old cache:
https://www.reddit.com/r/cheetahcoin/comments/xrqay2/nengchta_electrum_server_connection_issue/
