from django.shortcuts import render

from .models import PageView


def tag(request, tag):
    user_agent = request.META.get('HTTP_USER_AGENT')
    ip = get_client_ip(request)
    pageview = PageView.objects.create(user_agent=user_agent, ip=ip, tag=tag)
    pageview.save()
    return render(request, 'tag.html')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    return render(request, 'index.html', { 'pageviews': PageView.objects.all()})

