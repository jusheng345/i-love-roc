
from django.db import models

class Grade(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=50, unique=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classes = models.ManyToManyField(Class, related_name='courses')

    def __str__(self):
        return f'{self.subject} - {self.name} ({self.teacher})'

class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Grade：年級
# Teacher：教師
# Subject：科目
# Class：班級
# Course：課程，包含了教師、科目、班級等資訊
# Document：文件，包含了上傳的課程計畫等資訊，與課程是一對多的關係