# Generated by Django 4.0.3 on 2022-04-08 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('Message', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='form.message')),
            ],
        ),
    ]