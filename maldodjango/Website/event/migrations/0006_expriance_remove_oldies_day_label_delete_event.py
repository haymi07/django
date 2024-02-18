# Generated by Django 5.0.2 on 2024-02-18 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_oldies_day_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expriance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('Thumbnail', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='oldies_day',
            name='label',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
