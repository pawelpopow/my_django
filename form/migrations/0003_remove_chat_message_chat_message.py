# Generated by Django 4.0.3 on 2022-04-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='Message',
        ),
        migrations.AddField(
            model_name='chat',
            name='Message',
            field=models.ManyToManyField(null=True, to='form.message'),
        ),
    ]
