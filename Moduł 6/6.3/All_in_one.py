import sqlite3
from sqlite3 import Error
import csv
from sqlalchemy import MetaData, Integer, String, Table, Column
from sqlalchemy import create_engine

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def execute_sql(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def get_clean_stations():
    clean_stations = open("clean_stations.csv")
    rows = csv.reader(clean_stations)
    cur = conn.cursor()
    cur.executemany("INSERT OR IGNORE INTO stations VALUES (?, ?, ?, ?, ?, ?, ?)", rows)
    conn.commit()
    
def get_clean_measure():
    clean_measure = open("clean_measure.csv")
    rows = csv.reader(clean_measure)
    cur = conn.cursor()
    cur.executemany("INSERT OR IGNORE INTO measure VALUES (?, ?, ?, ?)", rows)
    conn.commit()

def select_all(conn, table):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()

    return rows

def select_where(conn, table, **query):
    cur = conn.cursor()
    qs = []
    values = ()
    for k, v in query.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)
    cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
    rows = cur.fetchall()
    return rows

if __name__ == "__main__":

    db_file = "baza.db"   
    conn = create_connection(db_file)

    create_stations_sql = """
    -- stations table
    CREATE TABLE IF NOT EXISTS stations (
        station text PRIMARY KEY,
        latitude float,
        longitude float,
        elevation float,
        name text,
        country text,
        state text
    );
    """

    create_measure_sql = """
    -- measure table
    CREATE TABLE IF NOT EXISTS measure (
        station_name text PRIMARY KEY,
        date text,
        precip float,
        tobs integer,
        FOREIGN KEY (station_name) REFERENCES stations (station)
    );
    """

    if conn is not None:
        execute_sql(conn, create_stations_sql)
        execute_sql(conn, create_measure_sql)
    

    get_clean_stations()
    get_clean_measure()

    print(conn.execute("SELECT * FROM stations LIMIT 5").fetchall())

engine = create_engine('sqlite:///baza.db')
meta = MetaData()


stations = Table(
    "stations", meta,
    Column("id", Integer, primary_key=True),
    Column("station", String),
    Column("date", String),
    Column("precip", String),
    Column("tobs", String),
    Column("latitude", Integer),
    Column("longitude", Integer),
    Column("elevation", Integer),
    Column("name", String),
    Column("country", String),
    Column("state", String),
)

meta.create_all(engine)

conn = engine.connect()

for i in conn.execute("SELECT * FROM stations LIMIT 5").fetchall():
    print(i)