-- create external table --
CREATE OR REPLACE EXTERNAL TABLE `graphite-scout-414507.week_3_zoomcamp_dataset.green_taxi_data`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://terraform_zoomcamp_data/green-taxi-data/green_tripdata_2022-*.parquet']
);

-- create unpartitioned table --
CREATE OR REPLACE TABLE `graphite-scout-414507.week_3_zoomcamp_dataset.green_taxi_data_2022_nonpartitioned`
AS SELECT * FROM `graphite-scout-414507.week_3_zoomcamp_dataset.green_taxi_data`;

-- create partitioned table --
CREATE OR REPLACE TABLE `graphite-scout-414507.week_3_zoomcamp_dataset.green_taxi_data_2022_partitioned`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS (
  AS SELECT * FROM `graphite-scout-414507.week_3_zoomcamp_dataset.green_taxi_data`;
);