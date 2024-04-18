# Generated by Django 4.2.6 on 2023-10-12 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_feature_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='videoblog/image')),
                ('title', models.CharField(max_length=128)),
                ('logo', models.FileField(upload_to='videoblog/logo')),
            ],
            options={
                'db_table': 'web_vide_blog',
                'ordering': ['-id'],
            },
        ),
    ]
