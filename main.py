from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['movies'])    #acceder a movies,  para añadir un parametro va entre llaves, en este caso ID, es lo que espero que me devuelva
def get_movie(id: int):    # para poder acceder al id tambien tenemos que agregarlo aca, y tenemos que poner que tipo es
    for item in movies:     #para hacer el filtrado de una peli por id, que recorra cada uno de los item
        if item["id"] == id:   #agrego la condicion que si el item con el id es igual al id q estamos recibiendo como parametro, justamente que me retorne ese item
            return item 
    return []    #en caso contrario que no lo devuelva y que devuelva una lista vacia