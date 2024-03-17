from django.urls import path
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('student/', views.StudentListView.as_view(), name='student'),
path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
path('portfolio/<int:portfolio_id>/update-portfolio', views.update_portfolio, name='update-portfolio'),
path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
path('portfolio/<int:portfolio_id>/create-project', views.create_project, name='create-project'),
path('portfolio/<int:portfolio_id>/update-project/<int:project_id>', views.update_project, name='update-project'),
path('portfolio/<int:portfolio_id>/delete-project/<int:project_id>', views.delete_project, name='delete-project')

]
