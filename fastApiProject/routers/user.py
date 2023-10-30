from fastapi import APIRouter,HTTPException
from pydantic import BaseModel

router = APIRouter(prefix='/user',
                   tags=['user'],
                   responses={404:{'message':'No encontrado'}})

#Inicio el server: uvicorn user:app --reload

#Entidad User
class User(BaseModel):
    id:int
    name:str
    surname:str
    url: str
    age:int

users_list = [User(id=1,name='Juanpi',surname='Calvo',url='www.none.com',age=8),
            User(id=2,name='Brais',surname='Moure',url='https//:.com',age=20),
            User(id=3,name='Brais',surname='Moure',url='https//:.com',age=67)]

@router.get('/usersjson')
async def usersjson():
    return [{'name':'Brais','surname':'Moure','url':'https//:.com','age':20},
            {'name':'Brais','surname':'Moure','url':'https//:.com','age':40},
            {'name':'Brais','surname':'Moure','url':'https//:.com','age':67}]


@router.get('/users')
async def users():
    return users_list

# Path: Parametros que son fijos

@router.get('/{id}')
async def users(id: int):
    return search_user(id)


# Query: Parametros que no suelen ser obligatorios para la petición

@router.get('/userbyquery')
async def users(id: int):
    return search_user(id)

@router.post('/adduser',response_model=User, status_code=201)
async def new_user(user: User):
    if type(search_user(user.id))== User:
        raise HTTPException(status_code=204, detail='El usuario ya existe')
    users_list.append(user)
    return user

@router.put('/modifyuser')
async def user(user: User):
    found = False
    for index, u in enumerate(users_list):
        if u.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {'error':'No se ha encontrado el usuario '}
    else:
        return user

@router.delete('/deleteuser/{id}')
async def user(id: int):
    found = False
    for index, u in enumerate(users_list):
        if u.id == id:
            del users_list[index]
            found = True
    if not found:
        return {'error': 'No se ha eliminado usuario '}

def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {'error': 'No se ha encontrado el usuario'}


