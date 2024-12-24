from dotenv import load_dotenv
from kafka import KafkaProducer
import json
import os


load_dotenv(verbose=True)


def produce(topic_name: str, message: str, key: str):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_serializer= lambda value: json.dumps(value).encode('utf-8'),
        key_serializer=lambda k: k.encode('utf-8')
    )
    producer.send(
        topic_name,
        value=message,
        key=key
    )