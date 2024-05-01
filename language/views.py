from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.translation import activate

def set_language(request):
    language = request.GET.get('language', 'en')  # Default to English if not specified
    activate(language)
    response = redirect(request.GET.get('next', '/'))
    response.set_cookie('django_language', language)
    return response
