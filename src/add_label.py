import json 
from kafka import KafkaConsumer, KafkaProducer
from wonderwords import RandomWord

if __name__ == '__main__':
    r = RandomWord()

    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    consumer = KafkaConsumer(
        'users_info',
        bootstrap_servers=['broker:29092'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    for message in consumer:
        res = message.value
        res['label'] = r.word(include_parts_of_speech=["nouns", "adjectives"])
        producer.send('users_label', json.dumps(res).encode('utf-8'))
        print(f"{res}")
