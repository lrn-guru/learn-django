from django.http import HttpResponse
from .models import Person

# Create your views here.
def home(request):
	people = Person.objects.all()
	info = "Some cool names:<br>" + "<br>".join(people)
	return HttpResponse(info)
