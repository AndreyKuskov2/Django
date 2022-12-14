# Generated by Django 4.1 on 2022-08-12 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_group_alter_project_name_alter_project_other_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='images/company/', verbose_name='Логотип')),
                ('name', models.CharField(max_length=100, verbose_name='Название компании')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('description', models.CharField(max_length=255, verbose_name='Описание компании')),
                ('city', models.CharField(max_length=50, null=True, verbose_name='Город')),
                ('hire_date', models.DateField(verbose_name='Дата приема на работу')),
                ('day_of_dismissal', models.DateField(blank=True, null=True, verbose_name='Дата увольнения')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'db_table': 'Company',
            },
        ),
        migrations.CreateModel(
            name='Responsibilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.company')),
            ],
            options={
                'verbose_name': 'Обязанность',
                'verbose_name_plural': 'Обязанности',
                'db_table': 'Responsibilities',
            },
        ),
    ]
