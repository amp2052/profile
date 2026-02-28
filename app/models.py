from django.db import models

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    path = models.CharField(max_length=500, null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)

    visit_count = models.IntegerField(default=1)
    first_visit = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ip_address} - {self.path}"
