from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from . import forms
from . import models


class IndexView(View):
    def get(self, request):
        return render(request, 'hotel/index.html')


class CustomerRegisterView(View):
    def get(self, request):
        return render(request, 'hotel/register.html', )

    def post(self, request):
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            customerId = register_form.cleaned_data['customerId']
            if not models.Customer.objects.filter(customerId=customerId).exists():
                customerName = register_form.cleaned_data['customerName']
                customerGender = register_form.cleaned_data['customerGender']
                customerStayTime = register_form.cleaned_data['customerStayTime']
                roomType = register_form.cleaned_data['roomType']
                customerPhoneNumber = register_form.cleaned_data['customerPhoneNumber']
                Customer = models.Customer(customerId=customerId, customerName=customerName,
                                           customerGender=customerGender,
                                           customerStayTime=customerStayTime, roomType=roomType,
                                           customerPhoneNumber=customerPhoneNumber)
                Customer.save()
                return render(request, 'hotel/register.html', {'success': True, 'msg': '登记成功'})
            else:
                return render(request, 'hotel/register.html', {'error': True, 'msg': '该旅客已住店，请先删除该旅客信息'})
        else:
            return render(request, 'hotel/register.html', {'error': True, 'msg': '输入信息不合法'})


class CustomerLogOutView(View):
    def get(self, request):
        return render(request, 'hotel/leave.html')

    def post(self, request):
        leave_form = forms.LeaveForm(request.POST)
        if leave_form.is_valid():
            customerId = leave_form.cleaned_data['customerId']
            if models.Customer.objects.filter(customerId=customerId).exists():
                customerName = leave_form.cleaned_data['customerName']
                if customerName != models.Customer.objects.get(customerId=customerId).customerName:
                    return render(request, 'hotel/leave.html', {'error': True, 'msg': '旅客信息不匹配'})
                else:
                    models.Customer.objects.get(customerId=customerId).delete()
                    return render(request, 'hotel/leave.html', {'success': True, 'msg': '删除成功'})
            else:
                return render(request, 'hotel/leave.html', {'error': True, 'msg': '该旅客不存在'})
        else:
            return render(request, 'hotel/leave.html', {'error': True, 'msg': '输入信息不合法'})


class RoomManageView(View):
    def get(self, request):
        customerInfo = models.Customer.objects.all()
        print(type(customerInfo))
        return render(request, 'hotel/manage.html', {"customerInfo": customerInfo})
