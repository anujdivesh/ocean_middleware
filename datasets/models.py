from django.db import models
from download_method.models import DownloadMethod
from data_type.models import DataType
# Create your models here.
class Dataset(models.Model):
    short_name = models.CharField(max_length=255)
    long_name = models.CharField(max_length=255)
    data_type = models.OneToOneField(
        DataType,
        on_delete=models.CASCADE
    )
    data_provider = models.CharField(max_length=255)
    data_source_url = models.CharField(max_length=255)
    data_download_url = models.CharField(max_length=255)
    login_credentials_required = models.BooleanField()
    username = models.CharField(max_length=255,null=True,blank=True)
    password = models.CharField(max_length=255,null=True,blank=True)
    API_key = models.CharField(max_length=255,null=True,blank=True)
    download_method = models.OneToOneField(
        DownloadMethod,
        on_delete=models.CASCADE
    )
    download_file_prefix = models.CharField(max_length=255)
    download_file_infix = models.CharField(max_length=255)
    download_file_suffix = models.CharField(max_length=255)
    download_file_type = models.CharField(max_length=255)
    download_to_local_dir = models.BooleanField()
    local_directory_path = models.CharField(max_length=255)
    scp = models.BooleanField()
    scp_server_path = models.CharField(max_length=255,null=True,blank=True)
    frequency_minutes = models.IntegerField(default=0)
    frequency_hours = models.IntegerField(default=0)
    frequency_days = models.IntegerField(default=0)
    frequency_months = models.IntegerField(default=0)
    frequency_years = models.IntegerField(default=0)
    check_minutes = models.IntegerField(default=0)
    check_hours = models.IntegerField(default=0)
    check_days = models.IntegerField(default=0)
    check_months = models.IntegerField(default=0)
    check_years = models.IntegerField(default=0)
    has_variables = models.BooleanField()
    variables = models.CharField(max_length=255,null=True,blank=True)
    subset = models.BooleanField()
    xmin_xmax = models.CharField(max_length=255,null=True,blank=True)
    ymin_ymax = models.CharField(max_length=255,null=True,blank=True)
    create_latest = models.BooleanField()
    force_forecast = models.BooleanField()
    force_days = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.short_name}"