from django.shortcuts import render
from .models import Favorites
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
def favorites(request):
    if request.method=="GET":
        name = request.GET.get('name')
        desc = request.GET.get('desc')
        src = request.GET.get('imgsrc')
        current_user = request.user
        if Favorites.objects.filter(image=src,userid=current_user.username).exists():
            pass
        else:
            fav=Favorites()
            fav.movie_name=name
            fav.movie_desc=desc
            fav.image=src
            fav.userid=current_user.username
            fav.save()
            return HttpResponse('Added to Favorites')

def favorite_movies(request):
    if request.user.is_authenticated:
        favorites= Favorites.objects.filter(userid=request.user.username).all()
        n= len(favorites)
        rows= n//4 + 1
        params={'favorites':favorites,'rows':range(1,rows)}
        return render(request,'favorites.html',params)
    else:
        return HttpResponse('Login and try again')
    
def favorite_movies_delete(request):
    if request.method=="GET":
        name = request.GET.get('name')
        desc = request.GET.get('desc')
        src = request.GET.get('imgsrc')
        current_user = request.user
        data=Favorites.objects.get(movie_name=name,image=src,userid=current_user.username)
        data.delete()
        return HttpResponse('Deleted')