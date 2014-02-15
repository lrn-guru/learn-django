from django.http import HttpResponse
from guest_book.people.models import Person

def home(request):
    people = Person.objects.all()
    summary = ''
    for person in people:
        summary += person.name + ' says ' + person.message + '.<br>'
    return HttpResponse(summary)
