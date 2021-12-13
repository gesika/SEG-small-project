# Generated by Django 3.2.5 on 2021-12-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_auto_20211212_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='USERTYPE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'Applicant'), (2, 'Member'), (3, 'Officer'), (4, 'Owner')])),
            ],
        ),
    ]
