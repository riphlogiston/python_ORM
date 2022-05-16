from peewee import PostgresqlDatabase, Model

db=PostgresqlDatabase('snake_film', user='daria', password='1', host='localhost', port=5432, autorollback=True)

class BaseModel(Model):
    
    class Meta:
        database=db