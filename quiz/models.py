from django.db import models
from course.models import Lesson
from django.conf import settings


class Quizes(models.Model):
   CHOICES = [
       ('option1', 'Option 1'),
       ('option2', 'Option 2'),
       ('option3', 'Option 3'),
       ('option4', 'Option 4'),
   ]
   lesson = models.ForeignKey(Lesson, related_name='quizzes', on_delete=models.PROTECT , null=True)
   question = models.CharField(max_length=300, unique=True, verbose_name='Question')
   option1 = models.CharField(max_length=300, verbose_name='Option 1')
   option2 = models.CharField(max_length=300, verbose_name='Option 2')
   option3 = models.CharField(max_length=300, verbose_name='Option 3')
   option4 = models.CharField(max_length=300, verbose_name='Option 4')
   answer = models.CharField(max_length=300, choices=CHOICES, verbose_name='Answer', help_text='Select the correct option')
   status = models.BooleanField(default=False, help_text='Publish status of the question', verbose_name='Status')

   def __str__(self):
       return self.question

   class Meta:
       verbose_name = 'Question'
       verbose_name_plural = 'Questions'


class QuizResult(models.Model):
   username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT , null=True)
   lesson = models.ForeignKey(Lesson, related_name='quizzes_result', on_delete=models.PROTECT , null=True)
   totall = models.PositiveSmallIntegerField(default=0, verbose_name='Total Questions')
   score = models.PositiveSmallIntegerField(default=0, verbose_name='Score')
   percent = models.FloatField(max_length=5, verbose_name='Percentage')
   correct = models.PositiveSmallIntegerField(default=0, verbose_name='Correct Answers')
   wrong = models.PositiveSmallIntegerField(default=0, verbose_name='Incorrect Answers')
   created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

   def __str__(self):
       return self.fullname

   class Meta:
       verbose_name = 'Result'
       verbose_name_plural = 'Results'
