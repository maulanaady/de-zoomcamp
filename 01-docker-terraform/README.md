# 01-Docker-Terraform

# Usage
1. Deploy postgres and pgadmin docker container
```docker compose -f  docker-compose.yaml up -d```

2. Build the Image
```docker build -t ny_taxi_ingest:1.0 .```

3. Ingest needed data
```
docker run --network zoomcamp_network ny_taxi_ingest:1.0 --host=postgres --db=ny_taxi --user=maulana --password=zoomcamp --url=https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz --filepath=green_tripdata_2019-09.csv.gz --table=green_taxi_data --convert=True

docker run --network zoomcamp_network ny_taxi_ingest:1.0 --host=postgres --db=ny_taxi --user=maulana --password=zoomcamp --url=https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv --filepath=taxi_zone_lookup.csv --table=taxi_zone_lookup
```
