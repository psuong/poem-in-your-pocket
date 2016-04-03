# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from buzzfeed import SECTIONS
from algorithm.haiku_generate import generate_haiku
from twilio_api.twilio_sendsms import send_sms
from format_haiku import format_haiku_lines


# Create your views here.
def index(request):
    context_dict = {
        'page_title': 'Poem In Your Pocket',
        'form_url': '',
        'feeds': SECTIONS,
    }

    if request.method == 'POST':
        phone_num = '+1' + request.POST['phone_number']
        haiku = format_haiku_lines(generate_haiku(request.POST['topic']))
        context_dict['haiku'] = haiku
        send_sms(phone_num, '%s\n%s\n%s' % (haiku[0], haiku[1], haiku[2]))
        return render(request, 'index.html', context_dict)
    else:
        return render(request, 'index.html', context_dict)
