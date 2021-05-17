import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_retrieve_course(api_client, course_factory):
    course = course_factory()
    url = reverse("courses-detail", args=[course.id])
    response = api_client.get(url)
    response_json = response.json()
    assert response.status_code == HTTP_200_OK
    assert course.id == response_json['id']


@pytest.mark.django_db
def test_list_courses(api_client, course_factory):
    url = reverse("courses-list")
    courses = course_factory(_quantity=10)
    response = api_client.get(url)
    response_json = response.json()
    assert response.status_code == HTTP_200_OK
    assert len(courses) == len(response_json)


@pytest.mark.django_db
def test_id_filter(api_client, course_factory):
    url = reverse("courses-list")
    courses = course_factory(_quantity=10)
    test_id = courses[0].id
    params = {"id": test_id}
    response = api_client.get(url, params)
    response_json = response.json()
    assert response.status_code == HTTP_200_OK
    assert response_json[0]['id'] == params['id']


@pytest.mark.django_db
def test_name_filter(api_client, course_factory):
    url = reverse("courses-list")
    course = course_factory(name='Chemistry')
    params = {'name': 'Chemistry'}
    response = api_client.get(url, params)
    response_json = response.json()
    assert response.status_code == HTTP_200_OK
    assert response_json[0]['name'] == course.name


@pytest.mark.django_db
def test_course_creation(api_client):
    url = reverse("courses-list")
    payload = {
        'name': 'Chemistry'
    }
    response = api_client.post(url, payload)
    response_json = response.json()
    assert response.status_code == HTTP_201_CREATED
    assert response_json['name'] == payload['name']


@pytest.mark.django_db
def test_course_update(api_client, course_factory, student_factory):
    course = course_factory()
    new_student = student_factory()
    url = reverse("courses-detail", args=[course.id])
    payload = {
        'students': new_student.id
    }
    response = api_client.patch(url, payload)
    response_json = response.json()
    assert response.status_code == HTTP_200_OK
    assert response_json['students'][0] == new_student.id


@pytest.mark.django_db
def test_course_delete(api_client, course_factory):
    course = course_factory()
    url = reverse("courses-detail", args=[course.id])
    response = api_client.delete(url)
    assert response.status_code == HTTP_204_NO_CONTENT


@pytest.mark.parametrize(
    ['students_max_value', 'http_response'],
    (
        (0, HTTP_400_BAD_REQUEST),
        (1, HTTP_201_CREATED)
    )
)
@pytest.mark.django_db
def test_post_max_students(settings, api_client, student_factory, students_max_value, http_response):
    settings.MAX_STUDENTS_PER_COURSE = students_max_value
    new_student = student_factory()
    url = reverse('courses-list')
    payload = {
        'name': 'Some_course',
        'students': new_student.id
    }
    response = api_client.post(url, payload)
    assert response.status_code == http_response


@pytest.mark.parametrize(
    ['students_max_value', 'http_response'],
    (
        (0, HTTP_400_BAD_REQUEST),
        (1, HTTP_200_OK)
    )
)
@pytest.mark.django_db
def test_patch_max_students(settings, api_client, course_factory, student_factory, students_max_value, http_response):
    settings.MAX_STUDENTS_PER_COURSE = students_max_value
    course = course_factory()
    new_student = student_factory()
    url = reverse('courses-detail', args=[course.id])
    payload = {
        'students': new_student.id
    }
    response = api_client.patch(url, payload)
    assert response.status_code == http_response
