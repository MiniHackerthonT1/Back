from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0005_alter_comment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='movie_id',
            new_name='movie',
        ),
    ]
