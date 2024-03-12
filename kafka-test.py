from kafka import KafkaProducer, KafkaConsumer

bootstrap_servers = 'localhost:9092'
topic = 'test_topic'


def produce_message(producer, topic):
    # Produce a test message
    message = b"Hello, Kafka!"
    producer.send(topic, value=message)
    producer.flush()
    print("Message sent successfully.")


def consume_messages(consumer, topic):
    # Subscribe to the topic
    consumer.subscribe(topics=[topic])
    # Consume messages
    for message in consumer:
        print("Received message:", message.value.decode('utf-8'))


if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers,
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             group_id='test_group')

    # Produce a test message
    produce_message(producer, topic)

    # Consume messages
    consume_messages(consumer, topic)
