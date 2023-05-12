from django.shortcuts import render, redirect
from .models import Grade, Teacher, Subject, Class, Course, Document
from documents.forms import DocumentForm
from documents.models import Document

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
    if request.method == 'POST':
        document_form = DocumentForm(request.POST, request.FILES)
        if document_form.is_valid():
            document_form.save()
            return redirect('index')
    else:
        document_form = DocumentForm()

    context['document_form'] = document_form
    return render(request, 'index.html', context)

def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    documents = Document.objects.filter(course=course)
    context = {
        'course': course,
        'documents': documents
    }
    return render(request, 'course_detail.html', context)
