from django.db import models

class Advertisement (models.Model):
    ad_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()
    target_demographics = models.JSONField()
    target_behavior = models.JSONField()
    vendor = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.title

class AdCampaigns(models.Model):
    campaign_id = models.AutoField(primary_key=True)
    campaign_name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    target_audience = models.JSONField()
    vendor = models.CharField(max_length=255, blank=False, null=False)
    advertisement_id = models.ManyToManyField(Advertisement)

    def __str__(self):
        return self.campaign_name
    

class AdImpresssions(models.Model):
    impression_id = models.AutoField(primary_key=True)
    ad = models.ForeignKey('Advertisement', on_delete=models.CASCADE, null=True)
    campaign = models.ForeignKey('AdCampaigns', on_delete=models.CASCADE, null=True)
    user_identifier = models.CharField(max_length=255, null=True)
    impression_time = models.DateTimeField(auto_now_add=True)
    click_time = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"Impression ID: {self.impression_id}"
    


