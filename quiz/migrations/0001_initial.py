# Generated by Django 5.1 on 2024-08-08 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300, unique=True, verbose_name='Question')),
                ('option1', models.CharField(max_length=300, verbose_name='Option 1')),
                ('option2', models.CharField(max_length=300, verbose_name='Option 2')),
                ('option3', models.CharField(max_length=300, verbose_name='Option 3')),
                ('option4', models.CharField(max_length=300, verbose_name='Option 4')),
                ('answer', models.CharField(choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3'), ('option4', 'Option 4')], help_text='Select the correct option', max_length=300, verbose_name='Answer')),
                ('status', models.BooleanField(default=False, help_text='Publish status of the question', verbose_name='Status')),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='quizzes', to='course.lesson')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totall', models.PositiveSmallIntegerField(default=0, verbose_name='Total Questions')),
                ('score', models.PositiveSmallIntegerField(default=0, verbose_name='Score')),
                ('percent', models.FloatField(max_length=5, verbose_name='Percentage')),
                ('correct', models.PositiveSmallIntegerField(default=0, verbose_name='Correct Answers')),
                ('wrong', models.PositiveSmallIntegerField(default=0, verbose_name='Incorrect Answers')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='quizzes_result', to='course.lesson')),
            ],
            options={
                'verbose_name': 'Result',
                'verbose_name_plural': 'Results',
            },
        ),
    ]
