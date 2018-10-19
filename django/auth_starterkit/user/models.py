from django.db import models
import uuid

class User(models.Model):
    # once a user's profiles has been touched manually, we should no longer
    # update their infomation based on data attached to bounties
    public_address = models.TextField(max_length=500, blank=True, unique=True)
    nonce = models.UUIDField(default=uuid.uuid4, null=False, blank=False)
