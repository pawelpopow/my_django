# Generated by Django 4.0.3 on 2022-04-08 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_remove_chat_message_chat_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='Message',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='form.message'),
        ),
    ]
