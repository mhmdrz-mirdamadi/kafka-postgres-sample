import json 
import time
from kafka import KafkaConsumer, KafkaProducer

if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    consumer = KafkaConsumer(
        'users_info',
        bootstrap_servers=['broker:29092'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    for message in consumer:
        res = message.value
        res['ts'] = int(time.time())
        producer.send('users_ts', json.dumps(res).encode('utf-8'))