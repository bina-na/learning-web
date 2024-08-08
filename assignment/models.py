from django.db import models
from django.conf import settings
from django.utils import timezone
from course.models import Course


class Assignment(models.Model):
   title = models.CharField(max_length=255, help_text="assignmet number, eg, Assignment1")
   description = models.TextField()
   document = models.FileField(upload_to='assignments/', blank=True, null=True)  # Document for the assignment
   course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
   instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignments_creator')
   deadline = models.DateTimeField()

   def __str__(self):
       return self.title

   class Meta:
       ordering = ['-deadline']


class StudentAssignmentSubmit(models.Model):
   assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='student_assignments')
   student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignments_submitted')
   document = models.FileField(upload_to='student_assignments/', blank=True, null=True)
   grade = models.IntegerField(default=0, blank=True, null=True)
   submitted_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return f"{self.student} - {self.assignment.title}"

   def is_past_due(self):
       return timezone.now() > self.deadline

class Payment(models.Model):
    unit_price = models.DecimalField( max_digits=6 , decimal_places=2)
    reference_no = models.CharField(max_length = 255)
    course = models.ForeignKey(Course , on_delete=models.CASCADE , related_name= "payment_course")
    student = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.CASCADE , related_name= "purschaser_name")


