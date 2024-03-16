from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):

    # Render index.html
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active port. query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})

from django.views import generic
from portfolio_app.models import Student

class StudentListView(generic.ListView):
    model=Student

class StudentDetailView(generic.DetailView):
    model=Student
