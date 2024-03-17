from django.forms import ModelForm
from .models import Project,Portfolio,Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#create class for project form
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title','description',)

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ('title', 'is_active', 'about', 'contact_email',)

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'major', 'email',)