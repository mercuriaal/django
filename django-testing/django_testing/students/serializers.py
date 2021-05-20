from django.conf import settings

from rest_framework import serializers

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate_students(self, value):
        if len(value) > settings.MAX_STUDENTS_PER_COURSE:
            raise serializers.ValidationError(f'Число студентов на курсе не должно превышать '
                                              f'{settings.MAX_STUDENTS_PER_COURSE} человек')
        return value

