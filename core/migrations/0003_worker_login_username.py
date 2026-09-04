from django.db import migrations, models


def fill_usernames(apps, schema_editor):
    Worker = apps.get_model('core', 'Worker')
    for worker in Worker.objects.all().order_by('id'):
        worker.login_username = f'worker{worker.id}'
        worker.save(update_fields=['login_username'])


class Migration(migrations.Migration):
    dependencies = [('core', '0002_prototype_fields')]
    operations = [
        migrations.AddField('worker', 'login_username', models.CharField(default='worker', max_length=50, unique=True)),
        migrations.RunPython(fill_usernames, migrations.RunPython.noop),
    ]
