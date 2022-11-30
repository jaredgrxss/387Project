from django.db import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from PIL import Image
# Create your models here.
User = get_user_model()


class Item(models.Model):
    name = models.CharField(max_length=256,unique=True)
    image = models.ImageField(upload_to='images/',blank=True)
    description = models.TextField(blank=False)
    date_listed = models.DateTimeField(auto_now_add=True)
    sell_date = models.DateTimeField()
    min_price = models.IntegerField(blank=False)
    highest_bid = models.IntegerField(default=0)
    highest_bid_user = models.CharField(max_length=256,default='Creator')
    user = models.ForeignKey(User, related_name='users_items',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self):
        if not self.image:
            return
            
        super(Item,self).save()
        image = Image.open(self.image.path)
        new_img = (300,300)
        image.thumbnail(new_img)
        image.save(self.image.path)


    def get_absolute_url(self):
        return reverse("items:item-detail", kwargs={"pk": self.pk})

class Bid(models.Model):
    user = models.ForeignKey(User, related_name='user_bids',on_delete=models.CASCADE)
    curr_item = models.ForeignKey(Item, related_name='item_bids',on_delete=models.CASCADE)
    amount = models.IntegerField()


    class Meta():
        ordering = ['-amount']
        

    
