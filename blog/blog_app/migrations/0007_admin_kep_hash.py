# Generated by Django 3.1.6 on 2021-02-20 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_auto_20210218_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='kep_hash',
            field=models.CharField(default='test.png', max_length=255),
            preserve_default=False,
        ),
    ]
