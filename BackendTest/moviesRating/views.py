from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from moviesRating.models import Movie, Rating, Reaction
import json


#this function are to created a movies crud
def addMovie(request):
    data = json.loads(request.body)
    Movie.save(data)
    data = {
        'message': "Seve Movie",
    }
    return JsonResponse(data)

def updateMovie(request, id):
    item = Movie.objects.get(id=id)
    item.name = request.data.get('name')
    item.image = request.data.get('image')
    item.url = request.data.get('url')
    item.language = request.data.get('language')
    item.summary = request.data.get('summary')
    item.save()
    
    data = {
        'message': item.name + "has bean updated",
    }
    return JsonResponse(data)

def listMovie(request):
    querySet = Movie.objects.all().values("name", "language", "summary")
    json_resp = serializers.serialize(querySet, 'json')
    return HttpResponse(json_resp, content_type="application/json")


def deleteMovie(request, id):
    item = Movie.objects.get(id=id)
    if (item.isdeleted):
        rating = Rating.objects.get(id=item.ratingid)
        rating.delete()
        
        listReactions = Reaction.objects.filter(movieid=id).all()
        for r in listReactions:
            r.delete()
    item.delete()
    data = {
        'message': "Movie: " + id + "remove ok",
    }
    return JsonResponse(data)

#this function are to created a reaction crud
def addUserReaction(request):
    data = json.loads(request.body)
    Reaction.save(data)
    data = {
        'message': "Seve Reaction",
    }
    return JsonResponse(data)

def updateUserReaction(request, id):
    item = Reaction.objects.get(id=id)
    item.type = request.data.get('type')
    item.save()
    
    data = {
        'message': "Raiting has bean updated",
    }
    return JsonResponse(data)

def listUserReactionByMovieId(request, id=id):
    querySet = Reaction.objects.filter(movieid=id).all()
    json_resp = serializers.serialize(querySet, 'json')
    return HttpResponse(json_resp, content_type="application/json")


def deleteUserReaction(request, id):
    item = Reaction.objects.get(id=id)
    item.delete()
    data = {
        'message': "Reaction: " + id + "remove ok",
    }
    return JsonResponse(data)

