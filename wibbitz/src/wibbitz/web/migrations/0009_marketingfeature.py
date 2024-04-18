# Generated by Django 4.2.6 on 2023-10-13 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_rename_company_name_testimonial_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketingFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='marketingfeature/')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'web_marketing_feature',
                'ordering': ['-id'],
            },
        ),
    ]
