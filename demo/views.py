from django.shortcuts import render, HttpResponse
from .models import Student
# Create your views here.

def home(request):
    objs = Student.objects.all()
    html = '<table><tr><th>Roll</th><th>Name</th><th>City</th></tr>'
    for obj in objs:
        html += f'<tr><td>{obj.roll}</td><td>{obj.name}</td><td>{obj.city}</td></tr>'
    html+='</html>'
    return HttpResponse(html)