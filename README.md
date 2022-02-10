TL;DR

```
docker-compose up --scale sentinel=3 --build -d
docker logs redis-sentinel-stand_sentinel_1 -f
docker logs app -f
docker exec -it redis-master redis-cli DEBUG sleep 120
```