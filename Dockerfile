 
# We're using Ubuntu 20.10
FROM groovy
#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/vishnu175/SPARKZZZ /root/userbot
RUN mkdir /root/userbot/.bin
WORKDIR /root/userbot

# Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/vishnu175/SPARKZZZ/master/requirements.txt
#
CMD ["python3","-m","userbot"]
