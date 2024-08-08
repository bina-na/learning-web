from django.db import models
from django.conf import settings
from course.models import Course

class Exam(models.Model):
   title = models.CharField(max_length=255, help_text="Enter exam title, e.g., Exam 1")
   course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams')
   duration_minutes = models.PositiveIntegerField(
       help_text="Enter the duration of the exam in minutes. For example, enter 60 for a 1-hour exam."
   )
   instructions = models.TextField(blank=True, null=True)

   def __str__(self):
       return self.title

   class Meta:
       ordering = ['title']
       verbose_name = 'Exam'
       verbose_name_plural = 'Exams'

class ExamQuestion(models.Model):
   CHOICES = [
       ('option1', 'Option 1'),
       ('option2', 'Option 2'),
       ('option3', 'Option 3'),
       ('option4', 'Option 4'),
   ]
   exam = models.ForeignKey('Exam', related_name='questions', on_delete=models.CASCADE)
   question = models.CharField(max_length=300, unique=True, verbose_name='Question')
   option1 = models.CharField(max_length=300, verbose_name='Option 1')
   option2 = models.CharField(max_length=300, verbose_name='Option 2')
   option3 = models.CharField(max_length=300, verbose_name='Option 3')
   option4 = models.CharField(max_length=300, verbose_name='Option 4')
   answer = models.CharField(max_length=300, choices=CHOICES, verbose_name='Answer', help_text='Select the correct option')
   status = models.BooleanField(default=False, help_text='Publish status of the exam', verbose_name='Status')

   def __str__(self):
       return self.question

   class Meta:
       verbose_name = 'Exam Question'
       verbose_name_plural = 'Exam Questions'

class ExamResult(models.Model):
   username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT , null=True)
   exam = models.ForeignKey('Exam', related_name='exam_id', on_delete=models.PROTECT , null=True)
   totall = models.PositiveSmallIntegerField(default=0, verbose_name='Total Questions')
   score = models.PositiveSmallIntegerField(default=0, verbose_name='Score')
   percent = models.FloatField(max_length=5, verbose_name='Percentage')
   correct = models.PositiveSmallIntegerField(default=0, verbose_name='Correct Answers')
   wrong = models.PositiveSmallIntegerField(default=0, verbose_name='Incorrect Answers')
   created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

   def __str__(self):
       return self.username

   class Meta:
       verbose_name = 'Result'
       verbose_name_plural = 'Results'
