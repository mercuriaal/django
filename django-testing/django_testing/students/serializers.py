from django.conf import settings

from rest_framework import serializers

from students.models import Course, Student


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate_students(self, value):
        method = self.context['request'].stream.method
        if method == 'PATCH':
            course_name = self.instance.name
            students_quantity = Student.objects.filter(courses__name__exact=course_name).prefetch_related('courses')
            if students_quantity.count() == settings.MAX_STUDENTS_PER_COURSE:
                raise serializers.ValidationError(f'Число студентов на курсе не должно превышать '
                                                  f'{settings.MAX_STUDENTS_PER_COURSE} человек')
            return value
        if method == 'POST' and len(value) != 0:
            course_name = value[0].name
            students_quantity = Student.objects.filter(courses__name__exact=course_name).prefetch_related('courses')
            if students_quantity.count() == settings.MAX_STUDENTS_PER_COURSE:
                raise serializers.ValidationError(f'Число студентов на курсе не должно превышать '
                                                  f'{settings.MAX_STUDENTS_PER_COURSE} человек')
            return value
        return value
