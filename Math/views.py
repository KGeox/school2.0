from django.shortcuts import render
from .models import Topic

# Create your views here.
def math(request):
    topics = Topic.objects.all()
    context={'topics':topics}
    context={}
    return render(request, 'Math/math.html', context)
