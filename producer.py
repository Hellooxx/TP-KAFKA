# Kafka producer for JSON events
import json
import time
from datetime import datetime, timezone

from kafka import KafkaProducer

TOPIC = "events-json"
BOOTSTRAP = "localhost:9092"


def build_event(event_id: int, event_type: str, source: str) -> dict:
    return {
        "event_id": event_id,
        "event_type": event_type,
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": source,
    }


def main() -> None:
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    events = [
        build_event(1, "login", "tp1-producer"),
        build_event(2, "view", "tp1-producer"),
        build_event(3, "click", "tp1-producer"),
        build_event(4, "logout", "tp1-producer"),
        build_event(5, "purchase", "tp1-producer"),
    ]

    for event in events:
        producer.send(TOPIC, event)
        print(f"sent: {event}")
        time.sleep(0.2)

    producer.flush()
    producer.close()


if __name__ == "__main__":
    main()
