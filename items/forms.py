from django import forms 
from . import models

class CreateNewItem(forms.ModelForm):
    class Meta():
        model = models.Item
        fields = ('name','description','image','sell_date','sell_date','min_price')
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.fields['name'].label = "Enter a name for your item!"
        self.fields['description'].label = 'Give your item a description for users to see!'
        self.fields['sell_date'].label = "Enter the date you want this auction to end! (Format: M/D/YYYY H/M/S)"
        self.fields['min_price'].label = 'Enter a minimum price for this item, in dollars.'

class CreateNewBid(forms.ModelForm):
    class Meta():
        model = models.Bid
        fields = ('amount','curr_item')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.fields['amount'].label = "Enter an amount! (Must be higher than highest current bid)"
        self.fields['curr_item'].label = 'Which item would you like to bid on?'

    
    def clean(self):
        curr_item = self.cleaned_data['curr_item']
        if curr_item.highest_bid >= self.cleaned_data['amount']:
            raise forms.ValidationError(f"Sorry, you must enter an amount higher than the current highest bid, {curr_item.highest_bid}")        

        return super().clean()
