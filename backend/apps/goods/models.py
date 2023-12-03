from django.db import models
from django.contrib.auth import get_user_model
        
class Good(models.Model):
    username=models.CharField(
        max_length=128,
    )
    Good_name=models.CharField(
        max_length=32,
    )
    Good_price=models.IntegerField(
        default=1228
    )

    created_at = models.DateTimeField(
        auto_now_add=True
        )
    
    def __str__(self):
        return f"Good add to {self.user.username}"