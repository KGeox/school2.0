from django.shortcuts import render
from .models import Topic

# Create your views here.
def chemistry(request):
    topics = Topic.objects.all()
    context={'topics':topics}
    return render(request, 'Chemistry/chemistry.html', context)
