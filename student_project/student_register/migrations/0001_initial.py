# Generated by Django 4.0 on 2023-02-01 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Rno', models.CharField(max_length=6)),
                ('Emp', models.CharField(max_length=15)),
                ('Position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_register.position')),
            ],
        ),
    ]
