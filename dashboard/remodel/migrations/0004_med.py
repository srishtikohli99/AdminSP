# Generated by Django 3.0.2 on 2020-05-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remodel', '0003_auto_20200502_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Med',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('sup', models.FloatField()),
            ],
        ),
    ]