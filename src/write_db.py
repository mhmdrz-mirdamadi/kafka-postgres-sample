import json 
from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'users_label',
        bootstrap_servers=['broker:29092'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    for message in consumer:
        res = message.value
        print(f"{res}")
