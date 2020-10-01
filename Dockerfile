FROM kalilinux/kali-rolling
RUN apt-get update && apt upgrade -y && apt-get install sudo -y
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get install -y\
    coreutils \
    bash \
    nodejs \
    bzip2 \
    curl \
    figlet \
    gcc \
    g++ \
    git \
    util-linux \
    libevent-dev \
    libjpeg-dev \
    libffi-dev \
    libpq-dev \
    libwebp-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    musl \
    neofetch \
    libcurl4-openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-server-dev-all \
    openssl \
    mediainfo \
    wget \
    python3 \
    python3-dev \
    python3-pip \
    libreadline-dev \
    zipalign \
    sqlite \
    ffmpeg \
    libsqlite3-dev \
    zlib1g-dev \
    recoverjpeg \
    zip \
    megatools \
    libfreetype6-dev \
    procps \
    policykit-1 \
    tree

RUN pip3 install --upgrade pip setuptools 
RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi 
RUN if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi 
RUN rm -r /root/.cache
RUN git clone https://github.com/vishnu175/SPARKZZZ /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/
RUN chmod +x /usr/local/bin/*
RUN pip3 install -r requirements.txt
ENV PATH="/home/userbot/bin:$PATH"
CMD ["bash","sparkzzz/start.sh"]
