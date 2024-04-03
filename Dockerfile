FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip cron && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /home/src

COPY ./requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY ./src/ .
RUN chmod +x docker_entrypoint.sh && \
    chmod a+x get_data.py

CMD ["./docker_entrypoint.sh"]