from sqlalchemy import MetaData, Integer, String, Table, Column
from sqlalchemy import create_engine

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