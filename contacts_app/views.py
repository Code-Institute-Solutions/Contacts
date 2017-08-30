from django.shortcuts import render
from contacts_app.models import Contact
from django.http import HttpResponse


# Create your views here.
def get_contacts(request):
    return render(request, "index.html",
                  {'contact_list': Contact.objects.all()})


def get_index(request):
    return HttpResponse('Hello World!')