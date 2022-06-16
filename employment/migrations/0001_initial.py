# Generated by Django 4.0.5 on 2022-06-15 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('number', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('position', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=20)),
                ('logo', models.ImageField(upload_to='logos')),
                ('description', models.TextField()),
                ('proficiency', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=110)),
                ('logo', models.ImageField(upload_to='logos')),
                ('date_start', models.DateField(null=True)),
                ('date_end', models.DateField(null=True)),
                ('description', models.TextField()),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employment.contact')),
                ('skills_used', models.ManyToManyField(to='employment.skills')),
            ],
        ),
    ]