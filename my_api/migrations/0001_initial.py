# Generated by Django 5.1 on 2024-09-02 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=5)),
                ('mobile', models.IntegerField()),
            ],
        ),
    ]
