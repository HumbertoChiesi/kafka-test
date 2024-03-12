from kafka import KafkaProducer, KafkaConsumer
import time
import json

bootstrap_servers = 'localhost:49092,localhost:39092,localhost:29092'
topic = 'test_topic'


def produce_message(producer, topic, json_data):
    message = json.dumps(json_data).encode('utf-8')
    producer.send(topic, value=message)
    producer.flush()
    print("Message sent successfully.")
    consume_messages(consumer, topic)


def consume_messages(consumer, topic):
    consumer.subscribe(topics=[topic])

    for message in consumer:
        print("Received message:", json.loads(message.value.decode('utf-8')))


if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers,
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             group_id='test_group')

    data = {"time": time.time()}

    produce_message(producer, topic, data)
