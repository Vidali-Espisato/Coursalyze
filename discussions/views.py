from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Discussions
# Create your views here.


def index(request):
    items = Discussions.objects.all().order_by("added_date")
    return render(request, 'discussions.html', {
        'items': items
    })


def add_item(request):
    current_date = timezone.now()
    content = request.POST['input_text']
    Discussions.objects.create(
        user=request.user, added_date=current_date, text=content)
    return HttpResponseRedirect('/discussions/')


def delete_item(request, item_id):
    Discussions.objects.get(id=item_id).delete()
    return HttpResponseRedirect('/discussions/')
