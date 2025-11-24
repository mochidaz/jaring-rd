from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('journal', '0004_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='post_covers/'),
        ),
    ]
