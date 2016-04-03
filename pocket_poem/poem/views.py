# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from twilio import send_sms


# Create your views here.
def index(request):
    context_dict = {
        'page_title': "Poem In Your Pocket",
        'form_url': '/sendtext'
    }
    return render(request, 'index.html', context_dict)


def send_text(request):
    try:
        # TODO: Add the generated haiku to content
        content = "Some crap"
        phone_num = '1' + request.POST['phone_number']
        send_sms(phone_num, content)
        return "Works?"
    except:
        return "Fails"
