import os
import json 
from kafka import KafkaConsumer
import psycopg2
from dotenv import load_dotenv

load_dotenv()

db_params = {
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT")
}

create_table_query = """
    CREATE TABLE IF NOT EXISTS data (
        content JSONB
    )
"""

insert_table_query = """
    INSERT INTO data (content)
    VALUES (%s)
"""

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'users_label',
        bootstrap_servers=['broker:29092'],
        value_deserializer=lambda x: x.decode('utf-8'))
    
    with psycopg2.connect(**db_params) as conn:
            with conn.cursor() as cur:
                cur.execute(create_table_query)
                conn.commit()

    for message in consumer:
        res = message.value

        with psycopg2.connect(**db_params) as conn:
            with conn.cursor() as cur:
                cur.execute(insert_table_query, (res,))
                conn.commit()
