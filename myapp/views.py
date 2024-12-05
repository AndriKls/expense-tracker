from django.shortcuts import render
from .forms import ExpenseForm
from .models import Expense
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.db.models import Sum
import datetime

# Create your views here.


def index(request):
    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount'))
    #logic to calculate 365 days expenses
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year)
    yearly_sum = data.aggregate(Sum('amount'))
    #logic to calculate last month expenses
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = data.aggregate(Sum('amount'))
    #logic to calculate last week expenses
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = data.aggregate(Sum('amount'))

    daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))

    category_sums = Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))


    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
        return render(request, 'myapp/index.html', {
            'expense_form': expense_form, 'expenses': expenses, 'total_expenses': total_expenses, 'yearly_sum': yearly_sum, 'monthly_sum': monthly_sum,'weekly_sum': weekly_sum, 'daily_sums': daily_sums, 'category_sums': category_sums})
    else:
        expense_form = ExpenseForm()
        return render(request, 'myapp/index.html', {
            'expense_form': expense_form, 'expenses': expenses, 'total_expenses': total_expenses, 'yearly_sum': yearly_sum, 'monthly_sum': monthly_sum,'weekly_sum': weekly_sum, 'daily_sums': daily_sums, 'category_sums': category_sums})

class UpdateExpenseView(UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'myapp/expense_form.html'
    context_object_name = 'expense_form'
    success_url = reverse_lazy('index')


class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name ='myapp/expense_delete.html'
    success_url = reverse_lazy('index')

    
      
