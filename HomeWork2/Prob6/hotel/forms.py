from django import forms


class RegisterForm(forms.Form):
    customerName = forms.CharField(max_length=30)
    customerId = forms.CharField(max_length=5, min_length=5)
    customerGender = forms.CharField(max_length=5)
    customerStayTime = forms.IntegerField()
    customerPhoneNumber = forms.CharField(max_length=11,min_length=11)
    roomType = forms.CharField(max_length=8)


class LeaveForm(forms.Form):
    customerName = forms.CharField(max_length=30)
    customerId = forms.CharField(max_length=5, min_length=5)
