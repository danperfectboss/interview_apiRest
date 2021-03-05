# Make application using get post update, delete (CRUD)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

lista_db = list()

class Person(BaseModel):
    name: str
    lastname: str
    age: int

#Regresa todo lo contenido en la lista
@app.get("/")
def index():
    return lista_db


#Inserta el elemento dentro de la lista
@app.post('/person')
def create_person(person:Person):
    #agrega el elemnto a la lista
    lista_db.append(person.dict())
    
    #regresa el ultimo elemento de la lista, en este caso regresa el elemento insertado
    return lista_db[-1]

#Elimina el elemento dentro de la lista verificando con el id de la posición
@app.delete('/person_del/{id}')
def delete_person(person_id: int):
    lista_db.pop(person_id)
    print(person_id)
    #regresa los elementos existentes en la lista
    return lista_db

#Actualiza elemento de la lista
@app.put('/persona/{id},{name}')
def update_person(person_id:int,person_name:str):
    lista_db[person_id]['name']=person_name
    # Regresa el elemento editado
    return lista_db[person_id]