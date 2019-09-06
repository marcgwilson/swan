FROM ubuntu:18.10
LABEL maintainer="marcgwilson"

RUN export DEBIAN_FRONTEND=noninteractive && \
	apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential software-properties-common \
    wget curl unzip sqlite3 jq python3 python3-dev \
    python3-setuptools python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python

ENV PYTHONIOENCODING=utf_8

ADD pip3 /usr/bin/pip3
RUN chmod +x /usr/bin/pip3 && /usr/bin/pip3 install --upgrade pip

RUN mkdir -p /root/.ptpython && touch /root/.ptpython/config.py

ADD src /root/src

WORKDIR /root/src
RUN pip3 install -r requirements.txt
RUN /bin/bash -c ./bootstrap.sh

EXPOSE 8000

ENTRYPOINT [ "/bin/sh", "-c" ]
CMD [ "python manage.py runserver 0:8000" ]
