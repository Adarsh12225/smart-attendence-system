from rest_framework import serializers
from .models import Subject,ClassSession, Attendance


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['id', 'name', 'teacher']
        read_only_fields = ['teacher']

class ClassSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassSession
        fields = ['id', 'subject', 'created_at', 'is_active']
        read_only_fields = ['created_at', 'is_active']


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'session', 'student', 'is_approved', 'marked_at']
        read_only_fields = ['student', 'is_approved', 'marked_at']