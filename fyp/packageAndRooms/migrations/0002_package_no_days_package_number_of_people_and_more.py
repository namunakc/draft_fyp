# Generated by Django 4.0.2 on 2022-04-14 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packageAndRooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='no_days',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='number_of_people',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='package_desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='package_name',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
