# Generated by Django 2.2 on 2019-10-07 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20191007_1846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event_model',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AddField(
            model_name='event_model',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
