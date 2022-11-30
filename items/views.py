from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from . import models
from . import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
import time

# Create your views here.


class ListItems(generic.ListView, LoginRequiredMixin):
    model = models.Item
    context_object_name = 'my_items'
    template_name = 'items/list_items.html'





class DetailItem(generic.DetailView, LoginRequiredMixin):
    model = models.Item 

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curr_time = str(datetime.now()).split(" ")
        sell_time = str(models.Item.objects.get(pk=self.kwargs['pk']).sell_date).split(" ")
        if sell_time[0] < curr_time[0]:
            context['has_passed'] = True
        elif sell_time[0] > curr_time[0]:
            context['has_passed'] = False
        else:
            curr_hours = curr_time[1].split(".")
            sell_hours = sell_time[1].split("+")
            curr_hours = curr_hours[0]
            sell_hours = sell_hours[0]
            curr_hours = curr_hours.split(":")
            curr_hours[0] = str(int(curr_hours[0])-6)
            curr_hours = ":".join(curr_hours)
            if sell_hours < curr_hours:
                context['has_passed'] = True
            else:
                context['has_passed'] = False
        

            

        return context

    template_name = 'items/item_detail.html'

class CreateItem(generic.CreateView, LoginRequiredMixin):
    form_class = forms.CreateNewItem
    template_name = 'items/create_item.html'

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        my_form = form.save(commit=False)
        my_form.user = self.request.user
        my_form.highest_bid = my_form.min_price
        my_form.save()

        return super().form_valid(form)

class DeleteItem(generic.DeleteView, LoginRequiredMixin):
    model = models.Item 
    template_name = 'items/delete_item.html'
    success_url = reverse_lazy('items:all-items')


class UpdateItem(generic.UpdateView, LoginRequiredMixin):
    model = models.Item 
    template_name = 'items/update_item.html'

class CreateBid(generic.CreateView,LoginRequiredMixin):
    models = models.Bid
    template_name = 'items/create_bid.html'
    form_class = forms.CreateNewBid

    def form_valid(self, form):
        my_form = form.save(commit=False)
        my_form.user = self.request.user
        item = models.Item.objects.filter(pk=my_form.curr_item.pk).update(highest_bid=my_form.amount)
        item = models.Item.objects.filter(pk=my_form.curr_item.pk).update(highest_bid_user=self.request.user.username)
        my_form.save()
        return super().form_valid(form)
    

    def get_success_url(self) -> str:

        return reverse('items:item-detail',kwargs={'pk':self.object.curr_item.pk})



def user_profile(request):
    
    context = {

    }
    return render(request,'user_profile.html',context=context)
