from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from apps.tvShows.models import *

def shows(request):

    context = {
        'shows': Shows.objects.all(),
    }
    return render(request,'tvShows/allshows.html',context)

def shows_new(request):
    return render(request, "tvShows/newshow.html")

def shows_create(request):
    errors = Shows.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:

        context={
            'show': request.POST,
        }
        
        showid = Shows.objects.create(title=context['show']['title'], network=context['show']['network'],releaseDate=str(context['show']['releaseDate']),description=str(context['show']['description']))
        messages.success(request, "Show successfully added")
        return redirect("/shows/"+str(showid.id))

def shows_show(request,id):
    context = {
        'show': Shows.objects.get(id=id)
    }
    return render(request,"tvShows/show.html",context)

def shows_edit(request,id):
    context = {
        'show': Shows.objects.get(id=id)
    }
    print(context['show'].releaseDate)
    return render(request,"tvShows/editshow.html",context)

def shows_update(request,id):
    errors = Shows.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+str(id)+'/edit')
    else:
        context = {
            'show': Shows.objects.get(id=id),
            'updates':request.POST,
        }
    
        print(context['updates'])
        print(context['updates']['releaseDate'])
        context['show'].title =context['updates']['title']
        context['show'].network =context['updates']['network']
        context['show'].releaseDate =context['updates']['releaseDate']
        context['show'].description =context['updates']['description']
        context['show'].save()
        
        return redirect("/shows/"+str(id))

def shows_destroy(request,id):
    context = {
        'show': Shows.objects.get(id=id)
    }
    context['show'].delete()
    return redirect("/shows")