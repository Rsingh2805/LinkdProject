# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from models import dictionary, Mentor
from django.http import HttpResponseRedirect
from django.urls import reverse
from difflib import SequenceMatcher


def index(request):
    try:
        s = request.GET['search']
        mlist = []
        q = Mentor.objects.all()
        for obj in q:
            for (key, value) in dictionary.items():
                if SequenceMatcher(None, s, value).ratio() >= 0.4 and (key in obj.interest_as_list()):
                    mlist.append(obj)
                    continue
        return render(request, 'linkd/index.html', {'dictionary': dictionary, 'mlist': mlist, 'query': s})
    except:
        return render(request, 'linkd/index.html', {'dictionary': dictionary})


def search(request):
    return HttpResponseRedirect(reverse('linkd:indexsearch', args=(request.POST['search'],)))


def readform(request):
    get_checked = request.POST.getlist('mentor_interest')
    mentor = Mentor(
        mentor_name=request.POST['mentor_name'],
        mentor_emailid=request.POST['mentor_emailid'],
        mentor_github=request.POST['mentor_github'],
        mentor_interest=''.join(get_checked)
    )
    mentor.save()
    return HttpResponseRedirect(reverse('linkd:getmentor', args=(mentor.pk,)))


def getmentor(request, mentor_id):
    mentor = get_object_or_404(Mentor, pk=mentor_id)
    return render(request, 'linkd/mentor.html', {
        'mentor': mentor,
        'dictionary': dictionary,
    })


def form(request):
    return render(request, 'linkd/form.html', {'dictionary': dictionary})
