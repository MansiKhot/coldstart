from django import forms

from .models import Users,Movies,Ratings

# class Uform(forms.ModelForm):

#     class Meta:
#         model = Users
#         fields = ('user_id',)

class NameForm(forms.Form):
  your_id = forms.CharField(label='Your id', max_length=100)
  def clean(self):
    cleaned_data = super(NameForm, self).clean()
    your_id = cleaned_data.get("your_id")
    try:
        p = Users.objects.get(id=your_id)
    except Users.DoesNotExist:
        raise forms.ValidationError("User not exist.")