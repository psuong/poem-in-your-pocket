# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from buzzfeed import SECTIONS
from algorithm.haiku_generate import generate_haiku
from twilio_api.twilio_sendsms import send_sms
from format_haiku import format_haiku_lines
import twilio.twiml
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    context_dict = {
        'page_title': 'Poem In Your Pocket',
        'form_url': '',
        'feeds': SECTIONS,
    }

    if request.method == 'POST':
        haiku = format_haiku_lines(generate_haiku(request.POST['topic']))
        context_dict['haiku'] = haiku
        context_dict['from_feed'] = request.POST['topic']
        if request.POST['phone_number']:
            phone_digits = request.POST['phone_number']
            phone_digits = phone_digits.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
            print request.POST['phone_number']
            if phone_digits == '3473292301':
                return render(request, 'index.html', context_dict)
            phone_num = '+1' + request.POST['phone_number']
            send_sms(phone_num, '%s\n%s\n%s' % (haiku[0], haiku[1], haiku[2]))
        return render(request, 'index.html', context_dict)
    else:
        return render(request, 'index.html', context_dict)


@csrf_exempt
def sms_response(request):
    '''http://poem-in-your-pocket-psuong.c9users.io/haiku/sms/get'''
    if request.method == 'POST':
        # first loop through words in request.POST['body'] for a theme
        # if none found, return possible sections
        # check if the SECTION is in the POST 
        for keyword in request.POST['Body'].split(' '):
            if keyword.lower() in SECTIONS:
                # found a keyword
                haiku = generate_haiku(keyword)
                send_sms(request.POST['From'], '%s\n%s\n%s' % (haiku[0], haiku[1], haiku[2]))
                return HttpResponse('OK - POST')
        # the keyword was not found, send a message with a list of possible keywords
        send_sms(request.POST['From'], 'Possible keywords: ' + str(SECTIONS))
        return HttpResponse('OK - POST - NO HAIKU')
    else:
        print request.GET
        return HttpResponse('OK - ' + request.method.upper())
