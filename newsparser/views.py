from django.shortcuts import render
from django.http import HttpResponse
from .parser import stopgame_parser
import requests

def index(request):
	game_and_link = ''
	list_game_news = stopgame_parser(requests)
	templates = 'index.html'
	for i in range(len(list_game_news)):
		game = f'{list_game_news[i]["title"]}<br>'
		game_link = f'<a href = "{list_game_news[i]["href"]}">Читать</a><br>'
		game_and_link += f'{game}  {game_link}<br>' 
	context = {
		'game_and_link' : game_and_link,
		}
	return render(request, templates, context)