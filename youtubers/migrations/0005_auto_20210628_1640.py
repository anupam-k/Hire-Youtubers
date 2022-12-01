# Generated by Django 3.2.4 on 2021-06-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0004_auto_20210628_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('Others', 'Others'), ('Sony', 'Sony'), ('Nikon', 'Nikon'), ('Red', 'Red'), ('Panasonic', 'Panasonic'), ('Fuji', 'Fuji'), ('Canon', 'Canon')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('VLOGS', 'VLOGS'), ('COOKING', 'COOKING'), ('CODE', 'CODE'), ('SELF-IMPROVEMENT', 'SELF-IMPROVEMENT'), ('MOBILE_REVIEW', 'MOBILE_REVIEW'), ('FILM_MAKING', 'FILM_MAKING'), ('COMEDY', 'COMEDY'), ('GAMING', 'GAMING')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('small', 'small'), ('large', 'large'), ('solo', 'solo')], max_length=255),
        ),
    ]