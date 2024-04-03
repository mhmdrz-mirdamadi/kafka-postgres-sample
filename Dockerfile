FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip cron && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /home/src

COPY ./requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY ./src/ .

COPY ./cronjob /etc/cron.d/cronjob
RUN chmod 0644 /etc/cron.d/cronjob
RUN crontab /etc/cron.d/cronjob

CMD service cron start && \
    python3 get_data.py & \
    python3 add_ts.py & \
    python3 add_label.py & \
    python3 write_db.py
