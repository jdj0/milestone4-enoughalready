# Generated by Django 4.1.3 on 2023-03-12 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='subtitle',
            field=models.CharField(max_length=99, null=True),
        ),
    ]
