# Generated by Django 2.2.1 on 2019-07-05 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campaign', '0011_auto_20190705_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='teams',
            field=models.ManyToManyField(blank=True, null=True, related_name='campaign_campaign_teams', related_query_name='campaign_campaigns', to='Campaign.CampaignTeam', verbose_name='Teams'),
        ),
    ]
