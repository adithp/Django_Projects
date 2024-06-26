# Generated by Django 4.2.6 on 2023-10-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_alter_marketingfeature_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/images')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('logo', models.FileField(upload_to='product/logo')),
            ],
            options={
                'db_table': 'web_product',
                'ordering': ['-id'],
            },
        ),
    ]
