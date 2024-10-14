from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from .tasks import notify_customers
import requests

# cache will only exists for 5 mins
@cache_page(5 * 60)
def say_hello(request):
    response = requests.get('https://httpbin.org/delay/2')
    data = response.json()
    return render(request, 'hello.html', {'name': data})
