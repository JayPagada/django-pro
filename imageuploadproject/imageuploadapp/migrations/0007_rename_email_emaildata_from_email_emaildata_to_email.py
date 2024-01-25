# Generated by Django 5.0.1 on 2024-01-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageuploadapp', '0006_rename_to_email_emaildata_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emaildata',
            old_name='email',
            new_name='from_email',
        ),
        migrations.AddField(
            model_name='emaildata',
            name='to_email',
            field=models.EmailField(default='exit', max_length=254),
            preserve_default=False,
        ),
    ]
