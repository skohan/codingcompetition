FROM python:3.6

RUN mkdir /app
WORKDIR /app

ADD . /app/

ENV PORT=8000

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-setuptools \
        g++ && \
        apt-get clean && rm -rf /var/lib/apt/lists/*

# RUN pip3 install  --upgrade pip
# RUN pip3 install virtualenv

# RUN virtualenv .env
# RUN .env/bin/activate

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD gunicorn codingcompetition.wsgi --bind 0.0.0.0:$PORT

