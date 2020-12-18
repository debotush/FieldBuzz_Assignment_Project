# Generated by Django 3.1.4 on 2020-12-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecruitmentInfoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('phoneNumber', models.CharField(max_length=14)),
                ('fullAddress', models.CharField(max_length=512)),
                ('nameOfUniversity', models.CharField(max_length=256)),
                ('graduationYear', models.IntegerField()),
                ('cgpa', models.FloatField()),
                ('experienceInMonths', models.IntegerField()),
                ('currentWorkPlaceName', models.CharField(max_length=256)),
                ('applyingIn', models.CharField(choices=[('ANDROID', 'Android'), ('BACKEND', 'Backend')], max_length=10)),
                ('expectedSalary', models.IntegerField()),
                ('fieldBuzzReference', models.CharField(max_length=256)),
                ('githubProjectUrl', models.CharField(max_length=2083)),
                ('cvFile', models.FileField(upload_to='document/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
