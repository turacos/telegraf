# telegraf

some configuration files to be used with telegraf/kafka/influxdb

# kafka

```
bin/kafka-configs.sh --alter \
  --add-config retention.ms=10000 \
  --bootstrap-server=0.0.0.0:9092 \
  --topic http_metrics
```
