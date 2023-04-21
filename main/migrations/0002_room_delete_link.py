# Generated by Django 4.2 on 2023-04-21 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('capacity', models.IntegerField()),
                ('is_projector', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Link',
        ),
    ]