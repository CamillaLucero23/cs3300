# Generated by Django 4.2 on 2024-02-25 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('contact_email', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('about', models.CharField(blank=True, max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, verbose_name='UCCS Email')),
                ('major', models.CharField(blank=True, choices=[('CSCI-BS', 'BS in Computer Science'), ('CPEN-BS', 'BS in Computer Engineering'), ('BIGD-BI', 'BI in Game Design and Development'), ('BICS-BI', 'BI in Computer Science'), ('BISC-BI', 'BI in Computer Security'), ('CSCI-BA', 'BA in Computer Science'), ('DASE-BS', 'BS in Data Analytics and Systems Engineering')], max_length=200)),
                ('portfolio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('porfolio', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio')),
            ],
        ),
    ]
