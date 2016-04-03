# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from twilio_api import send_sms
from buzzfeed import SECTIONS
from algorithm.haiku_generate import generate_haiku


# Create your views here.
def index(request):
    context_dict = {
        'page_title': 'Poem In Your Pocket',
        'form_url': '',
        'feeds': SECTIONS,
    }

    if request.method == 'POST':
        print request.POST
        phone_num = '+1' + request.POST['phone_number']
        haiku = generate_haiku(request.POST['topic'])
        context_dict['haiku'] = haiku
        # send_sms(phone_num, haiku)
        return render(request, 'index.html', context_dict)
    else:
        return render(request, 'index.html', context_dict)
