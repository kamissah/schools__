# Generated by Django 2.2.6 on 2019-11-10 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=64)),
                ('courseCategory', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Examiner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examinerName', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ExaminerGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradeName', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolName', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='')),
                ('studentID', models.CharField(max_length=25)),
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.CharField(max_length=64)),
                ('otherNames', models.CharField(blank=True, max_length=64, null=True)),
                ('birthDate', models.DateField()),
                ('gender', models.CharField(max_length=25)),
                ('region', models.CharField(blank=True, max_length=64, null=True)),
                ('nationality', models.CharField(max_length=64)),
                ('email', models.EmailField(blank=True, max_length=64, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('indexNumber', models.CharField(blank=True, max_length=25, null=True)),
                ('admissionYear', models.DateField(max_length=64)),
                ('completionYear', models.DateField(blank=True, max_length=64, null=True)),
                ('completed', models.BooleanField(blank=True, null=True)),
                ('timeSubmitted', models.DateTimeField(auto_now_add=True)),
                ('updatedTime', models.DateTimeField(auto_now=True)),
                ('beceResult', models.FileField(blank=True, null=True, upload_to='')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentcourse', to='cumRec.Course')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentschoool', to='cumRec.School')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updatedTime', '-timeSubmitted'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(max_length=64)),
                ('subjectCategory', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StudentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form1Term1', models.IntegerField(blank=True, null=True)),
                ('form1Term2', models.IntegerField(blank=True, null=True)),
                ('form1Term3', models.IntegerField(blank=True, null=True)),
                ('form2Term1', models.IntegerField(blank=True, null=True)),
                ('form2Term2', models.IntegerField(blank=True, null=True)),
                ('form2Term3', models.IntegerField(blank=True, null=True)),
                ('form3Term1', models.IntegerField(blank=True, null=True)),
                ('form3Term2', models.IntegerField(blank=True, null=True)),
                ('form3Term3', models.IntegerField(blank=True, null=True)),
                ('capstoneExam', models.IntegerField(blank=True, null=True)),
                ('totalScore', models.IntegerField(blank=True, null=True)),
                ('averageScore', models.IntegerField(blank=True, null=True)),
                ('gpa', models.IntegerField(blank=True, null=True)),
                ('finalResult', models.FileField(blank=True, null=True, upload_to='')),
                ('timeSubmitted', models.DateTimeField(auto_now_add=True)),
                ('updatedTime', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courserec', to='cumRec.Course')),
                ('examinerName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='examinernamerec', to='cumRec.Examiner')),
                ('gradeName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gradenamerec', to='cumRec.ExaminerGrade')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentrec', to='cumRec.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjectrec', to='cumRec.Subject')),
            ],
            options={
                'ordering': ['-updatedTime', '-timeSubmitted'],
            },
        ),
    ]
