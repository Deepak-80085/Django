<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User

class LoginActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_datetime = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Login Activities"
    
    def __str__(self):
        return f"{self.user.username} - {self.login_datetime}"
=======
from django.db import models
from django.contrib.auth.models import User

class LoginActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_datetime = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Login Activities"
    
    def __str__(self):
        return f"{self.user.username} - {self.login_datetime}"
>>>>>>> 1d2a47fef390eff824b3bc7cf2ea9d7e421b8492
