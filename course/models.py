from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Curriculum(models.Model):
   CURICULUM_CHOICES = [
        ('TVET_LEVEL_1', 'TVET_1'),
        ('TVET_LEVEL_2', 'TVET_2'),
        ('TVET_LEVEL_3', 'TVET_3'),
        ('TVET_LEVEL_4', 'TVET_4'),
        ('TVET_LEVEL_5', 'TVET_5'),
        ('DIPLOMA', 'DIPLOMA'),
]

   Criculum_level = models.CharField(max_length=255, choices=CURICULUM_CHOICES , default='TVET_LEVEL_1')
   description = models.TextField(blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return self.name

   class Meta:
       ordering = ['-created_at']


class Category(models.Model):
   title = models.CharField(max_length=255)

   def __str__(self):
       return self.title



class Course(models.Model):
    STATUS_PENDING = 'Y'
    STATUS_PUBLISHED = 'O'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_PUBLISHED, 'Published'),
    ]

    LEVEL_BEGINNER = 'B'
    LEVEL_INTERMEDIATE = 'I'
    LEVEL_ADVANCED = 'A'

    LEVEL_CHOICES = [
        (LEVEL_BEGINNER, 'Beginner'),
        (LEVEL_INTERMEDIATE, 'Intermediate'),
        (LEVEL_ADVANCED, 'Advanced'),
    ]
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    instructors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="course_instructors")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="course_category")
    curriculum = models.ForeignKey('Curriculum', on_delete=models.CASCADE, related_name="courses")
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES, default=LEVEL_BEGINNER)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

class Lesson(models.Model):
    number = models.PositiveIntegerField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE , related_name='included_course' )
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='lessons/videos/', blank=True, null=True)
    doc_file = models.FileField(upload_to='lessons/docs/', blank=True, null=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f"Lesson {self.number}: {self.title}"


