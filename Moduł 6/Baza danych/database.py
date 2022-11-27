import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_connection_in_memory():

    conn = None
    try:
        conn = sqlite3.connect(":memory:")
        print(f"Connected, sqlite version: {sqlite3.version}")
    except Error as e:
       print(e)
    finally:
        if conn:
            conn.close()

def execute_sql(conn, sql):

    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)


def add_heroes(conn, heroes):

    sql = '''INSERT INTO bohaterowie(imie, nazwisko, pseudonim)
             VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, heroes)
    conn.commit()
    return cur.lastrowid

def add_origin(conn, origin):

    sql = '''INSERT INTO pochodzenie(heroes_id, miasto, uniwersum, bohater_pozytywny)
             VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, origin)
    conn.commit()
    return cur.lastrowid

def update(conn, table, id, **kwargs):

    parameters = [f"{k} = ?" for k in kwargs]
    parameters = ", ".join(parameters)
    values = tuple(v for v in kwargs.values())
    values += (id, )

    sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("OK")
    except sqlite3.OperationalError as e:
        print(e)

def delete_where(conn, table, **kwargs):

    qs = []
    values = tuple()
    for k, v in kwargs.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)

    sql = f'DELETE FROM {table} WHERE {q}'
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    print("Usunięto")

def delete_all(conn, table):

    sql = f'DELETE FROM {table}'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print("Usunięto")

if __name__ == "__main__":
    create_connection("superhero.db")
    create_connection_in_memory()
    conn = create_connection("superhero.db")
    
    create_bohaterowie_sql = """
    -- bohaterowie table
    CREATE TABLE IF NOT EXISTS bohaterowie (
        id integer PRIMARY KEY,
        imie VARCHAR(30) NOT NULL,
        nazwisko VARCHAR(30) NOT NULL,
        pseudonim VARCHAR(30) NOT NULL
    );
    """
    create_pochodzenie_sql = """
    -- pochodzenie table
    CREATE TABLE IF NOT EXISTS pochodzenie (
        id integer PRIMARY KEY,
        heroes_id integer NOT NULL,
        miasto text NOT NULL,
        uniwersum VARCHAR(15) NOT NULL,
        bohater_pozytywny VARCHAR(15) NOT NULL,
        FOREIGN KEY (heroes_id) REFERENCES bohaterowie (id)
    );
    """

    execute_sql(conn, create_bohaterowie_sql)
    execute_sql(conn, create_pochodzenie_sql)

    hero1 = ("Clark", "Cent", "Superman")
    hero2 = ("Wade", "Wilson", "Deadpool")
    hero3 = ("Bruce", "Wane", "Gotham City")
    hero4 = ("Max", "Eisenhardt", "Magneto")
    hero5 = ("Peter", "Parker", "Spiderman")
    
    h1_id = add_heroes(conn, hero1)
    h2_id = add_heroes(conn, hero2)
    h3_id = add_heroes(conn, hero3)
    h4_id = add_heroes(conn, hero4)
    h5_id = add_heroes(conn, hero5)

    origin1 = (h1_id, "Metropolis", "DC", "tak")
    origin2 = (h2_id, "Vancouver", "Marvel", "nie")
    origin3 = (h3_id, "Gotham City", "DC", "tak")
    origin4 = (h4_id, "Various", "Marvel", "nie")
    origin5 = (h5_id, "Nowy Jork", "Marvel", "tak")

    origin1_id = add_origin(conn, origin1)
    origin2_id = add_origin(conn, origin2)
    origin3_id = add_origin(conn, origin3)
    origin4_id = add_origin(conn, origin4)
    origin5_id = add_origin(conn, origin5)
    
    update(conn, "bohaterowie", 1, nazwisko ="Kent")
    update(conn, "pochodzenie", 2, bohater_pozytywny ="tak")

    delete_where(conn, "pochodzenie", id=3)
    # delete_all(conn, "pochodzenie")
    # delete_all(conn, "bohaterowie")
    conn.close()