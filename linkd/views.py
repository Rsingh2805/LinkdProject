# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from linkd.models import INTEREST_AREAS, Mentor
from django.http import HttpResponseRedirect
from django.urls import reverse
from difflib import SequenceMatcher


def index(request):
    try:
        search_query = request.POST['search']
        mList = []

        interest = max(INTEREST_AREAS.items(), key=lambda(k, v): SequenceMatcher(None, search_query, v).ratio())[0]

        mentors = Mentor.objects.filter(mentor_interest__contains=interest)
        for mentor in mentors:
            mList.append(mentor)
        return render(request, 'linkd/index.html', {'dictionary': INTEREST_AREAS, 'mlist': mList, 'query': search_query})
    except:
        return render(request, 'linkd/index.html', {'dictionary': INTEREST_AREAS})


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
        'dictionary': INTEREST_AREAS,
    })


def form(request):
    return render(request, 'linkd/form.html', {'dictionary': INTEREST_AREAS})
