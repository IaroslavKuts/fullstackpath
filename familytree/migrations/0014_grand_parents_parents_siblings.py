# Generated by Django 3.1.1 on 2020-10-08 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('familytree', '0013_auto_20201008_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siblings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=128)),
                ('person_surname', models.CharField(max_length=128)),
                ('person_age', models.IntegerField()),
                ('person_sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10)),
                ('person_family_status', models.CharField(choices=[('none', 'No information'), ('single', 'single'), ('engaged', 'engaged'), ('married', 'married')], max_length=10)),
                ('person_country', models.CharField(max_length=128)),
                ('sibling_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=128)),
                ('person_surname', models.CharField(max_length=128)),
                ('person_age', models.IntegerField()),
                ('person_sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10)),
                ('person_family_status', models.CharField(choices=[('none', 'No information'), ('single', 'single'), ('engaged', 'engaged'), ('married', 'married')], max_length=10)),
                ('person_country', models.CharField(max_length=128)),
                ('parent_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grand_Parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=128)),
                ('person_surname', models.CharField(max_length=128)),
                ('person_age', models.IntegerField()),
                ('person_sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10)),
                ('person_family_status', models.CharField(choices=[('none', 'No information'), ('single', 'single'), ('engaged', 'engaged'), ('married', 'married')], max_length=10)),
                ('person_country', models.CharField(max_length=128)),
                ('grand_parent_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
