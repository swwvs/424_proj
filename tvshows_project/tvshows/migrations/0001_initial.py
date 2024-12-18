# Generated by Django 5.0.1 on 2024-11-26 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TVShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
    ]
