# Generated by Django 5.1 on 2024-08-13 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dataset",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("short_name", models.CharField(max_length=255)),
                ("long_name", models.CharField(max_length=255)),
                ("data_type", models.CharField(max_length=255)),
                ("data_provider", models.CharField(max_length=255)),
                ("data_source_url", models.CharField(max_length=255)),
                ("data_download_url", models.CharField(max_length=255)),
                ("login_credentials_required", models.BooleanField()),
                ("username", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
                ("API_key", models.CharField(max_length=255)),
                ("download_method", models.CharField(max_length=255)),
                ("download_file_prefix", models.CharField(max_length=255)),
                ("download_file_infix", models.CharField(max_length=255)),
                ("download_file_suffix", models.CharField(max_length=255)),
                ("download_file_type", models.CharField(max_length=255)),
                ("download_to_local_dir", models.BooleanField()),
                ("local_directory_path", models.CharField(max_length=255)),
                ("scp", models.BooleanField()),
                ("scp_server_path", models.CharField(max_length=255)),
                ("frequency_minutes", models.IntegerField()),
                ("frequency_hours", models.IntegerField()),
                ("frequency_days", models.IntegerField()),
                ("frequency_months", models.IntegerField()),
                ("frequency_years", models.IntegerField()),
                ("check_minutes", models.IntegerField()),
                ("check_hours", models.IntegerField()),
                ("check_days", models.IntegerField()),
                ("check_months", models.IntegerField()),
                ("check_years", models.IntegerField()),
                ("has_variables", models.BooleanField()),
                ("variables", models.CharField(max_length=255)),
                ("subset", models.BooleanField()),
                ("xmin_xmax", models.CharField(max_length=255)),
                ("ymin_ymax", models.CharField(max_length=255)),
                ("create_latest", models.BooleanField()),
                ("force_forecast", models.BooleanField()),
                ("force_days", models.IntegerField()),
            ],
        ),
    ]
