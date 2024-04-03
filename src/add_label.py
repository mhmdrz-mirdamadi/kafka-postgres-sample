import json 
from kafka import KafkaConsumer

if __name__ == '__main__':
    print("Connecting to consumer ...")
    consumer = KafkaConsumer(
        'users_info',
        bootstrap_servers=['broker:29092'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    for message in consumer:
        print(f"{message.value}")
