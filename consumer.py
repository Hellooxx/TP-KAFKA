# Kafka consumer for JSON events
import json

from kafka import KafkaConsumer

TOPIC = "events-json"
BOOTSTRAP = "localhost:9092"
GROUP_ID = "tp1-consumer"


def main() -> None:
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP,
        group_id=GROUP_ID,
        auto_offset_reset="latest",
        enable_auto_commit=True,
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    )

    print(f"listening on {TOPIC} (group_id={GROUP_ID})")
    for msg in consumer:
        print(msg.value)


if __name__ == "__main__":
    main()
