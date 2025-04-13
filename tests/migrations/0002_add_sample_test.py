from django.db import migrations


def create_sample_test(apps, schema_editor):
    Test = apps.get_model('tests', 'Test')
    Question = apps.get_model('tests', 'Question')
    Answer = apps.get_model('tests', 'Answer')

    # Ваш код из функции create_sample_test() здесь


class Migration(migrations.Migration):
    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_test),
    ]