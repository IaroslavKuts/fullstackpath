# Generated by Django 3.1.1 on 2020-10-08 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familytree', '0012_grand_parents_parents_siblings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parents',
            name='parent_of',
        ),
        migrations.RemoveField(
            model_name='siblings',
            name='sibling_of',
        ),
        migrations.DeleteModel(
            name='Grand_Parents',
        ),
        migrations.DeleteModel(
            name='Parents',
        ),
        migrations.DeleteModel(
            name='Siblings',
        ),
    ]
