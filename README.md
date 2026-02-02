# TP KAFKA TOM LARGUIER DATAENG MASTER2

TP1 Kafka - Producer & Consumer JSON
1) Lancer Docker: `docker compose up -d`.
2) Creer le topic: `docker exec tp1-kafka kafka-topics.sh --bootstrap-server localhost:9092 --create --topic events-json --partitions 1 --replication-factor 1`.
3) Verifier le topic: `docker exec tp1-kafka kafka-topics.sh --bootstrap-server localhost:9092 --list`.
4) Installer Python >= 3.8 et `kafka-python`.
5) Lancer le consumer: `python consumer.py`.
6) Lancer le producer: `python producer.py`.
7) Ouvrir Kafka UI: http://localhost:8080.
8) Verifier que `events-json` existe et que des messages sont visibles.
9) Le consumer affiche les messages JSON recus dans la console.
10) Group id utilise: `tp1-consumer`.
