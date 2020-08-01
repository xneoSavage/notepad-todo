# Generated by Django 3.0.7 on 2020-08-01 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('due_date', models.DateTimeField()),
                ('label', models.CharField(choices=[('P', 'primary'), ('SE', 'secondary'), ('S', 'success'), ('D', 'danger'), ('W', 'warning'), ('I', 'info'), ('L', 'light'), ('D', 'dark')], max_length=2)),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
    ]
