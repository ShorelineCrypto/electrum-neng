FROM ubuntu:18.04@sha256:b58746c8a89938b8c9f5b77de3b8cf1fe78210c696ab03a1442e235eea65d84f

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

RUN dpkg --add-architecture i386 && \
    apt-get update -q && \
    apt-get install -qy \
        wget=1.19.4-1ubuntu2.2 \
        gnupg2 \
        dirmngr \
        python3-software-properties=0.96.24.32.1 \
        software-properties-common=0.96.24.32.1

RUN apt-get update -q && \
        apt-get install -qy \
        git \
        p7zip-full=16.02+dfsg-6 \
        make=4.1-9.1ubuntu1 \
        mingw-w64=5.0.3-1 \
        autotools-dev=20180224.1 \
        autoconf=2.69-11 \
        libtool=2.4.6-2 \
        gettext=0.19.8.1-6

RUN wget -nc https://dl.winehq.org/wine-builds/Release.key && \
        echo "c51bcb8cc4a12abfbd7c7660eaf90f49674d15e222c262f27e6c96429111b822 Release.key" | sha256sum -c - && \
        apt-key add Release.key && \
        rm Release.key && \
    wget -nc https://dl.winehq.org/wine-builds/winehq.key && \
        echo "d965d646defe94b3dfba6d5b4406900ac6c81065428bf9d9303ad7a72ee8d1b8 winehq.key" | sha256sum -c - && \
        apt-key add winehq.key && \
        rm winehq.key && \
    apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/ && \
    apt-get update -q && \
    apt-get install -qy \
        wine-stable-amd64:amd64=4.0.3~bionic \
        wine-stable-i386:i386=4.0.3~bionic \
        wine-stable:amd64=4.0.3~bionic \
        winehq-stable:amd64=4.0.3~bionic

RUN rm -rf /var/lib/apt/lists/* && \
    apt-get autoremove -y && \
    apt-get clean
