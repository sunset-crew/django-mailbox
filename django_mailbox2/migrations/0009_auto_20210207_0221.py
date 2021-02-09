# Generated by Django 3.1.6 on 2021-02-07 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_mailbox2", "0008_auto_20190219_1553"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="message_id",
            field=models.CharField(
                blank=None,
                max_length=255,
                null=None,
                unique=True,
                verbose_name="Message ID",
            ),
        ),
    ]