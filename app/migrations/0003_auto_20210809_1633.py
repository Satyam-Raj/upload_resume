# Generated by Django 3.2.5 on 2021-08-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210808_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='Address',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='College',
            field=models.CharField(max_length=115, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Currently_or_was_working_for',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Email',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Fifth_Experience',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Fifth_Skill',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='professional',
            name='First_Experience',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AlterField(
            model_name='professional',
            name='First_Name',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='First_Skill',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Fist_Language',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Fourth_Experience',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Fourth_Skill',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Last_Name',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='School',
            field=models.CharField(max_length=115, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Second_Experience',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Second_Language',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Second_Skill',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Seventh_Skill',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Sixth_Skill',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Third_Experience',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Third_Language',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Third_Skill',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
