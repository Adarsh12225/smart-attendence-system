from django.urls import path
from .views import CreateSubjectView

urlpatterns = [
    path('create-subject/', CreateSubjectView.as_view(), name='create-subject'),
]
