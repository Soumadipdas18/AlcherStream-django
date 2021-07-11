from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Reviews,Comments
import datetime
# Create your views here.
params={}
def reviews(request):
    if request.method=="GET":
        name = request.GET.get('name')
        desc = request.GET.get('desc')
        src = request.GET.get('imgsrc')
        if Reviews.objects.filter(image=src,movie_name=name).exists():
            return HttpResponse('Added to Reviews')
        else:
            rev=Reviews()
            rev.movie_name=name
            rev.movie_desc=desc
            rev.image=src
            rev.save()
            return HttpResponse('Added to Reviews')
        # return render(request,'reviews.html',params)

def allreview(request,slug):

    print(slug)
    path='https://image.tmdb.org/t/p/w500//'+slug+'.jpg'
    review=Reviews.objects.get(image=path)
    if not Comments.objects.filter(image=path).exists():
        return render(request,'reviews.html',{'review':review})
    else:
        comments=Comments.objects.filter(image=path).all()
        return render(request,'reviews.html',{'review':review,'comments':comments})
   

def postcomment(request,slug):
    if request.method=="POST":
        desc=request.POST['msg']
        com=Comments()
        com.image=slug
        com.what_commented=desc
        com.who_commented=request.user.username
        com.when_commented=datetime.datetime.now()
        com.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponse("404- Not found")    

def deletereview(request,slug):
    data=Comments.objects.get(comment_id=slug)
    data.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

