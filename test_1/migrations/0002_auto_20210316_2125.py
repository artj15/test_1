# Generated by Django 3.1.7 on 2021-03-16 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='main_p_1',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='about',
            name='main_p_2',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='about',
            name='main_p_3',
            field=models.ImageField(upload_to=''),
        ),
    ]
