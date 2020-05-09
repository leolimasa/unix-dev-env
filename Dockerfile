FROM ubuntu:eoan

COPY . /ude

RUN apt-get update
RUN /ude/install.sh
