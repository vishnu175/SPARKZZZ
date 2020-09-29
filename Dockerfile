FROM alpine

RUN git clone -b master https://github.com/vishnu175/SPARKZZZ /root/userbot
RUN mkdir /root/userbot/bin/
RUN chmod 777 /root/userbot
WORKDIR /root/userbot/

CMD ["python3","-m","userbot"]
