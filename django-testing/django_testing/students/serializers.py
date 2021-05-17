from django.conf import settings

from rest_framework import serializers

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate_students(self, data):
        if len(data) != 0:
            student = data[0].id
            students_quantity = Course.objects.filter(students=student).prefetch_related('students')
            if len(students_quantity) == settings.MAX_STUDENTS_PER_COURSE:
                raise serializers.ValidationError(f'Число студентов на курсе не должно превышать '
                                                  f'{settings.MAX_STUDENTS_PER_COURSE} человек')
            return data
        return data
