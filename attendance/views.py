from rest_framework import generics, permissions
from .models import Subject,Attendance
from .serializers import (
    SubjectSerializer,
    ClassSessionSerializer,
    AttendanceSerializer
)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from .models import ClassSession, Attendance
from .serializers import ClassSessionSerializer, AttendanceSerializer
from .permissions import IsTeacher, IsStudent

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
    queryset = ClassSession.objects.all()
    serializer_class = ClassSessionSerializer
    permission_classes = [IsTeacher]
    if ClassSession.objects.filter(is_active=True).exists():
        raise ValidationError("Another session is already active.")

    def perform_create(self, serializer):
        serializer.save()
        

class ActiveSessionsView(generics.ListAPIView):
    serializer_class = ClassSessionSerializer

    def get_queryset(self):
        return ClassSession.objects.filter(is_active=True)

class MarkAttendanceView(generics.CreateAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsStudent]

    def perform_create(self, serializer):
        session = serializer.validated_data['session']

        if not session.is_active:
            raise ValidationError("Session is not active")

        serializer.save(student=self.request.user)


class ApproveAttendanceView(generics.UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsTeacher]

    def perform_update(self, serializer):
        serializer.save(is_approved=True)

class PendingAttendanceView(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsTeacher]

    def get_queryset(self):
        return Attendance.objects.filter(
            is_approved=False,
            session__is_active=True
        )
class CloseSessionView(generics.UpdateAPIView):
    queryset = ClassSession.objects.all()
    serializer_class = ClassSessionSerializer
    permission_classes = [IsTeacher]

    def perform_update(self, serializer):
        serializer.save(is_active=False)
class AttendanceSummaryView(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsTeacher]

    def get_queryset(self):
        return Attendance.objects.filter(is_approved=True)