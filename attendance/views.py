from rest_framework import generics, permissions
from .models import Subject,Attendance
from .serializers import (
    SubjectSerializer,
    ClassSessionSerializer,
    AttendanceSerializer
)

class IsTeacher(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == 'teacher'


class CreateSubjectView(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsTeacher]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class StartSessionView(generics.CreateAPIView):
    serializer_class = ClassSessionSerializer
    permission_classes = [IsTeacher]

    def perform_create(self, serializer):
        serializer.save()

class ActiveSessionsView(generics.ListAPIView):
    serializer_class = ClassSessionSerializer

    def get_queryset(self):
        return ClassSession.objects.filter(is_active=True)

class MarkAttendanceView(generics.CreateAPIView):
    serializer_class = AttendanceSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class ApproveAttendanceView(generics.UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsTeacher]

    def perform_update(self, serializer):
        serializer.save(is_approved=True)