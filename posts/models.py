from django.db import models

class post(models.model):
    title = models.CharField(max_length=50);
    context = models.TextField();
    write_date = models.DateField(auto_now_add=True);
    update_date = models.DateTimeField(auto_now=True);
    
    
    


