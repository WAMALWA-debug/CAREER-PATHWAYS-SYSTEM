from django.urls import path
from . import views

urlpatterns = [
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('upload-csv/', views.upload_csv, name='upload_csv'),
    path('download-pdf', views.download_pdf, name='download_pdf')
]