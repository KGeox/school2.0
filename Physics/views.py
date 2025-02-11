from django.shortcuts import render
from .models import Topic

# Create your views here.
def physics(request):
    topics = Topic.objects.all()
    context={'topics':topics}
    context={}
    return render(request, 'Physics/physics.html', context)
