from django.db import models
from django.contrib.auth.models import User

import uuid


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    username = models.CharField(max_length = 25 , unique=True)
    email = models.EmailField(blank=True , null=True)
    name = models.CharField(max_length=30 , blank=True , null=True)
    profile_image = models.ImageField(blank=True , null=True, upload_to='profiles/', default='images/profiles/user-default.png')
    bio = models.TextField(blank=True , null=True)
    #followers = models.ForeignKey(User , on_delete=models.CASCADE)
    #following = models.ForeignKey(User , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , 
                        primary_key=True , editable=False)
    
    def __str__(self):
        return self.username


