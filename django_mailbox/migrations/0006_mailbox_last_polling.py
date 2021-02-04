# Generated by Django 1.9.8 on 2016-08-15 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_mailbox", "0005_auto_20160523_2240"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailbox",
            name="last_polling",
            field=models.DateTimeField(
                blank=True,
                help_text="The time of last successful polling for messages.It is blank for new mailboxes and is not set for mailboxes that only receive messages via a pipe.",
                null=True,
                verbose_name="Last polling",
            ),
        ),
    ]
