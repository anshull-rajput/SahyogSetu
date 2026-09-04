from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('core', '0001_initial')]
    operations = [
        migrations.AddField('worker', 'skills', models.TextField(blank=True, default='')),
        migrations.AddField('worker', 'member_id', models.CharField(default='COOP1000', max_length=30)),
        migrations.AddField('worker', 'welfare_accident', models.BooleanField(default=True)),
        migrations.AddField('worker', 'welfare_health', models.BooleanField(default=True)),
        migrations.AddField('booking', 'description', models.TextField(blank=True)),
        migrations.AddField('booking', 'estimated_cost', models.PositiveIntegerField(default=450)),
        migrations.AddField('booking', 'payment_status', models.CharField(default='unpaid', max_length=20)),
        migrations.AddField('booking', 'review', models.TextField(blank=True)),
        migrations.AddField('booking', 'transaction_id', models.CharField(blank=True, max_length=40)),
        migrations.AlterField('booking', 'status', models.CharField(choices=[
            ('pending', 'Pending Worker Approval'), ('accepted', 'Confirmed'),
            ('progress', 'Service In Progress'), ('rejected', 'Rejected'), ('completed', 'Completed')
        ], default='pending', max_length=20)),
    ]
