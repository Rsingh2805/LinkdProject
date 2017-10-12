# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from .models import dictionary,Mentor


def index(request):
    return render(request, 'linkd/index.html',{'dictionary':dictionary})

def form(request):
    return render(request,'linkd/form.html',{'dictionary':dictionary})

def readform(request):
	get_checked = request.POST.getlist('mentor_interest')
	mentor = Mentor(
		mentor_name=request.POST['mentor_name'],
		mentor_emailid=request.POST['mentor_emailid'],
		mentor_github =request.POST['mentor_github'],
		mentor_interest = ''.join(get_checked)
		)
	mentor.save()
	return render(request,'linkd/mentor.html',{
			'mentor':mentor,
			'dictionary':dictionary,
		})
#	return render(request,'linkd/readform.html')

def getmentor(request,mentor_id):
	mentor = get_object_or_404(Mentor,pk=mentor_id)
	return render(request,'linkd/mentor.html',{
			'mentor':mentor,
			'dictionary':dictionary,
		})

def favorite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song= album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        context = {'album' : album,
            'error_message' : "You didnt selected a valid song"}
        return render(request,'music/detail.html',context)
    else:
        selected_song.is_favorite = True
        selected_song.save()
        context = {'album' : album}
        return render(request,'music/detail.html',context)