# Generated by Django 5.1.7 on 2025-04-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariods16',
            name='animais',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
