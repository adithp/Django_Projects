# Generated by Django 4.2.5 on 2023-09-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_testimonial_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='designation',
            field=models.CharField(default='Software Enginer', max_length=225),
        ),
    ]
