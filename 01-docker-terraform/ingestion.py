import polars as pl
import gzip,os,argparse
from sqlalchemy import create_engine, Engine
from urllib.request import urlretrieve
#pyarrow, pandas

class GetConnection(object):
    def __init__(self, host: str, port: str, db:str, username: str, password: str):
        self.host= host
        self.port = port
        self.db = db
        self.username = username
        self.password = password
    def get_conn_uri(self) -> str:
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db}"
    def get_engine(self) -> Engine:
        create_engine(self.get_conn_uri)



class Ingestion(object):
    def __init__(self, url: str, filepath: str, table: str, is_convert: bool):
        self.url = url
        self.filepath = filepath
        self.table = table
        self.is_convert = is_convert
    def download(self):
        if os.path.exists(self.filepath) is False:
            urlretrieve(self.url, self.filepath)
    def read(self) -> pl.DataFrame:
        self.download()
        if self.filepath.endswith('.parquet') or self.filepath.endswith('.pq'):
            df = pl.read_parquet(self.filepath, low_memory=True)
        elif self.filepath.endswith('.csv'):
            df = pl.read_csv(self.filepath)
        elif self.filepath.endswith('.gz'):
            df = pl.read_csv(gzip.open(self.filepath,'rb'))
        else:
            raise ValueError(f"{self.filepath.split('.')[-1]} is not supported!")
        if self.is_convert:
            df = df.with_columns(pl.col("lpep_pickup_datetime","lpep_dropoff_datetime").str.to_datetime(format="%Y-%m-%d %H:%M:%S"))
        return df
    def write_sql(self, df: pl.DataFrame, conn_uri: str):
        df.write_database(self.table, conn_uri, if_table_exists="replace")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-H", "--host", help="Postgres host", default="localhost")
    parser.add_argument("-P", "--port", help="Postgres port", default=5432)
    parser.add_argument("-db", "--db", help="Postgres database")
    parser.add_argument("-U", "--user", help="Postgres user")
    parser.add_argument("-p", "--password", help="Postgres password")
    parser.add_argument("-u", "--url", help="URL data source")
    parser.add_argument("-f", "--filepath", help="Filepath to read")
    parser.add_argument("-t", "--table", help="Table name to write/update")
    parser.add_argument("-c", "--convert", help="flagging to convert columns", default=False)
    
    args = parser.parse_args()

    cnx = GetConnection(args.host,args.port,args.db,args.user,args.password)
    ingestion_sql = Ingestion(args.url,args.filepath,args.table,is_convert=args.convert)


    conn_uri = cnx.get_conn_uri()
    df = ingestion_sql.read()
    ingestion_sql.write_sql(df,conn_uri)