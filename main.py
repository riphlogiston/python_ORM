import requests

from db import models, films

URL = 'https://cinematica.kg/api/v1/movies/today'

def get_response_to_json(url):
    response=requests.get(url).json()
    return response

json_response=get_response_to_json(URL)['list']
film1=(json_response[0].get('details'))


class Film:
    def __init__(self, *args,**kwargs):
        self.__dict__.update(kwargs)

    def get_info(self):
        return self.__dict__

all_films=[Film(**film) for film in film1]
for film in all_films:
    try:
        print(films.FilmModel.create(**film.get_info()))
    except Exception:
        print(film.get_info())
        continue


def get_films(sort:str=None): #Select * from filmmodel;
    if sort==None:
        for film in films.FilmModel.select():
            print(film.id, film.title,film.value, film.order)
    else:
        if hasattr(films.FilmModel, sort):
            # filter=getattr(films.FilmModel,sort)
            for film in films.FilmModel.select().order_by(films.FilmModel.title):
                print(film.id, film.title,film.value, film.order)
        else:
            raise ValueError('нет такого поля')



def get_film(pk:int): #Select * from filmmodel where id=pk;
    film=films.FilmModel.get(films.FilmModel.id==pk)
    return {'id':film.id, 'title':film.title, 'value':film.value}


def delete_film(pk:int):
    try:
        film=films.FilmModel.get(films.FilmModel.id==pk)
    except Exception:
        print(f'object how to id {pk} DoesNotExist')
    else:
        return film.delete_instance()

def update_film(pk:int, **kwargs):
    film=films.FilmModel.get(films.FilmModel.id==pk)
    film.title=kwargs.get('title', film.title)
    film.order=kwargs.get('order', film.order)
    film.value=kwargs.get('value', film.value) #ленивый запрос
    film.save()

get_films(sort='title')

# update_film(pk=5, title='new_test', order=5)

# get_films()

# print(delete_film(pk=10))
# get_films()

# get_films()

# obj1=Film(**film1[1])

# film_model1=films.FilmModel(order=obj1.order, value=obj1.value, title=obj1.title)
# film_model1.save() #ленивый запрос
# films.FilmModel.create(order=3, value='test3', title='test1')
# print(film_model1)

# print(obj1.get_info())
# print(obj1.order)
# print(obj1.value)
# print(obj1.title)


#CRUD Create Read Update Delete

# models.create_table()

