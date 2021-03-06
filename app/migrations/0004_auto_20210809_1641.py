# Generated by Django 3.2.5 on 2021-08-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210809_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='Address',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='College',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Email',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Fifth_Experience',
            field=models.CharField(blank=True, max_length=126),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Fifth_Skill',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AlterField(
            model_name='professional',
            name='First_Experience',
            field=models.CharField(blank=True, max_length=126),
        ),
        migrations.AlterField(
            model_name='professional',
            name='First_Skill',
            field=models.CharField(max_length=115, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Fist_Language',
            field=models.CharField(max_length=115, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Fourth_Experience',
            field=models.CharField(blank=True, max_length=126),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Fourth_Skill',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AlterField(
            model_name='professional',
            name='School',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Second_Experience',
            field=models.CharField(blank=True, max_length=126),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Second_Language',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Second_Skill',
            field=models.CharField(max_length=115, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Seventh_Skill',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Sixth_Skill',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Third_Experience',
            field=models.CharField(blank=True, max_length=126),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Third_Language',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AlterField(
            model_name='professional',
            name='Third_Skill',
            field=models.CharField(max_length=115, null=True),
        ),
    ]
