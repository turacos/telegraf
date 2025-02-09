from kafka import KafkaConsumer
consumer = KafkaConsumer('http_metrics',bootstrap_servers='xxx.xxx.xxx.xxx:9092',enable_auto_commit=True)
consumer.partitions_for_topic('http_metrics')
consumer.seek_to_beginning()
for msg in consumer:
  print (msg)
