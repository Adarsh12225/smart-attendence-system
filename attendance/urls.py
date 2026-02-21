from django.urls import path
from .views import (
    CreateSubjectView,
    StartSessionView,
    ActiveSessionsView,
    MarkAttendanceView,
    PendingAttendanceView,
    CloseSessionView,
    ApproveAttendanceView
)

urlpatterns = [
    path('create-subject/', CreateSubjectView.as_view(), name='create-subject'),
    path('start-session/', StartSessionView.as_view()),
    path('active-sessions/', ActiveSessionsView.as_view()),
    path('mark-attendance/', MarkAttendanceView.as_view()),
    path('pending/', PendingAttendanceView.as_view()),
    path('approve-attendance/<int:pk>/', ApproveAttendanceView.as_view()),
    path('close-session/<int:pk>/', CloseSessionView.as_view()),
]
