import uuid
from django.db import models

class Advisor(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=False)
    profile_pic = models.URLField(max_length = 200)


    class Meta:
        db_table = "advisor"