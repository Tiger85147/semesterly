# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-30 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0035_auto_20210323_2126'),
        ('timetable', '0033_section_course_section_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advisors', models.ManyToManyField(related_name='invited_transcripts', to='student.Student')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_transcripts', to='student.Student')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Semester')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='transcript',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.Transcript'),
        ),
        migrations.AlterUniqueTogether(
            name='transcript',
            unique_together=set([('owner', 'semester')]),
        ),
    ]
