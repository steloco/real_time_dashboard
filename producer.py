import random
import time

from confluent_kafka import Producer
import socket
import json

import uuid

conf = {"bootstrap.servers": "localhost:9092", "client.id": socket.gethostname()}

producer = Producer(conf)

TOPIC = "fakeevents"


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))


while True:
    data = random.randrange(1, 6)
    payload = json.dumps(
        {"uuid": str(uuid.uuid4()), "data": data, "timestamp_": int(time.time() * 1000)}
    )
    print(payload)
    producer.produce(
        TOPIC,
        #  key="key",
        #  value=data.to_bytes(2, byteorder='big', signed=True),
        value=payload,
        callback=acked,
    )
    time.sleep(0.1)