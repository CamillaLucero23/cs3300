from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from portfolio_app.models import Student
from .forms import ProjectForm, PortfolioForm, StudentForm


# Create your views here.
def index(request):

    # Render index.html
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active port. query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})

class StudentListView(generic.ListView):
    model=Student

    #This allows us to display all relevant projects from our portfolio
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet 
        context["portfolio_list"] = Portfolio.objects.all()
        return context

class StudentDetailView(generic.DetailView):
    model=Student

class PortfolioDetailView(generic.DetailView):
    model=Portfolio

    #This allows us to display all relevant projects from our portfolio
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["project_list"] = Project.objects.all()

        return context

 
class ProjectDetailView(generic.DetailView):
    model=Project

#------------------------------------------------------------------------------------------
#Forms & Such

def create_project(request, portfolio_id):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)

    if request.method == 'POST':
        #create new dictionary with form data
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        form = ProjectForm(project_data)

        if form.is_valid():
            #save form without committing to database
            project = form.save(commit=False)
            #set portfolio relationship
            project.portfolio = portfolio
            project.save()

            #redirect back to port detail page
            return redirect('portfolio-detail', portfolio_id)
        
    context = {'form' : form}
    return render(request, 'portfolio_app/create_project.html', context)


def update_project(request,portfolio_id,project_id):
    project = Project.objects.get(id=project_id)
    form = ProjectForm(instance=project)
    portfolio = Portfolio.objects.get(pk=portfolio_id)

    if request.method == 'POST':
        #create new dictionary with form data
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        form = ProjectForm(project_data)

        if form.is_valid():
            #save form without committing to database
            project = form.save(commit=False)
            #set portfolio relationship
            project.portfolio = portfolio
            project.save()

            #redirect back to port detail page
            return redirect('portfolio-detail', portfolio_id)
        
    context = {'form' : form}
    return render(request, 'portfolio_app/update_project.html', context)


def delete_project(request,portfolio_id, project_id):
    project = Project.objects.get(id=project_id)
    
    if request.method == 'POST':
        project.delete()
        #redirect back to port detail page
        return redirect('portfolio-detail', portfolio_id)
    
    context = {'project' : project}  
    return render(request, 'portfolio_app/delete_project.html', context)


def update_portfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(id=portfolio_id)
    form = PortfolioForm(instance=portfolio)
  
    if request.method == 'POST':
        #create a new dictionary with form data and student_id
        portfolio_data = request.POST.copy()
        form = PortfolioForm(portfolio_data)

        if form.is_valid():
            #Save form without committing
            portfolio = form.save(commit=False)
            portfolio.save()

            #redirect
            return redirect('student-detail', portfolio_id)
    
    context = {'form': form}
    return render(request, 'portfolio_app/update_portfolio.html', context)

