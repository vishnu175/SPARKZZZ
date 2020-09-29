FROM alpine

RUN git clone https://github.com/vishnu175/SPARKZZZ /root/userbot
RUN mkdir /root/userbot/bin/
RUN chmod +x /usr/local/bin/*
WORKDIR /root/userbot/

CMD ["python3","-m","userbot"]
