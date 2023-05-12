from django.shortcuts import render
from .models import Grade, Teacher, Subject, Class, Course, Document

def index(request):
    grades = Grade.objects.all()
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    classes = Class.objects.all()
    courses = Course.objects.all()
    documents = Document.objects.all()
    context = {
        'grades': grades,
        'teachers': teachers,
        'subjects': subjects,
        'classes': classes,
        'courses': courses,
        'documents': documents
    }
    return render(request, 'index.html', context)

def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    documents = Document.objects.filter(course=course)
    context = {
        'course': course,
        'documents': documents
    }
    return render(request, 'course_detail.html', context)
