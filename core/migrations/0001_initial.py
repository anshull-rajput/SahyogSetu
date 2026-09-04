from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name='Worker', fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('name', models.CharField(max_length=100)), ('service', models.CharField(max_length=50)),
            ('area', models.CharField(max_length=100)), ('experience', models.PositiveIntegerField(default=1)),
            ('rating', models.FloatField(default=4.5)), ('recent_jobs', models.PositiveIntegerField(default=0)),
            ('verified', models.BooleanField(default=True)), ('availability', models.BooleanField(default=True)),
            ('phone', models.CharField(blank=True, max_length=20)),
            ('cooperative', models.CharField(default='Sahyog Labour Cooperative', max_length=150)),
        ]),
        migrations.CreateModel(name='Booking', fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('customer_name', models.CharField(max_length=100)), ('service', models.CharField(max_length=50)),
            ('area', models.CharField(max_length=100)), ('date', models.CharField(max_length=20)),
            ('time', models.CharField(max_length=20)), ('status', models.CharField(choices=[('pending','Pending'),('accepted','Accepted'),('rejected','Rejected'),('completed','Completed')], default='pending', max_length=20)),
            ('rating', models.PositiveIntegerField(blank=True, null=True)), ('created_at', models.DateTimeField(auto_now_add=True)),
            ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='core.worker')),
        ]),
    ]
