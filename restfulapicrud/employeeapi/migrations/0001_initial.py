# Generated by Django 4.0 on 2022-04-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]