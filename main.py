from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Date
)

from faker import Faker
from dotenv import load_dotenv
import os


# Cargar variables del archivo .env
load_dotenv()

usuario = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
puerto = os.getenv("MYSQL_PORT")
bd = os.getenv("MYSQL_DATABASE")

# Conexión a MySQL usando SQLAlchemy

conexion = (
f"mysql+pymysql://{usuario}:{password}@{host}:{puerto}/{bd}"
)

engine = create_engine(conexion)

metadata = MetaData()


tabla = Table(

    "personas_andres",

    metadata,

    Column("id", Integer, primary_key=True),

    Column("nombre", String(100)),
    Column("correo", String(100)),
    Column("telefono", String(50)),
    Column("ciudad", String(50)),
    Column("direccion", String(200)),
    Column("empresa", String(100)),
    Column("ocupacion", String(100)),
    Column("fecha_nacimiento", Date)

)

# Generador de datos ficticios colombianos

fake = Faker("es_CO")

# Función para crear registros aleatorios

def generar():

    return {

        "nombre": fake.name(),

        "correo": fake.email(),

        "telefono": fake.phone_number(),

        "ciudad": fake.city(),

        "direccion": fake.address(),

        "empresa": fake.company(),

        "ocupacion": fake.job(),

        "fecha_nacimiento":
        fake.date_of_birth()

    }



def main():

    metadata.create_all(engine)

    personas = []

    for i in range(100000):

        personas.append(generar())


    with engine.begin() as conn:

        conn.execute(
            tabla.insert(),
            personas
        )

    print("100000 registros insertados")



if __name__ == "__main__":

    main()
