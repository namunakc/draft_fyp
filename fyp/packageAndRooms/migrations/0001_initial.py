# Generated by Django 4.0.2 on 2022-04-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=500, null=True)),
                ('price', models.FloatField(null=True)),
            ],
        ),
    ]
