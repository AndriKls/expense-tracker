from django.shortcuts import render
from .forms import ExpenseForm
from .models import Expense
# Create your views here.


def index(request):
    expenses = Expense.objects.all()
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
        return render(request, 'myapp/index.html', {'expense_form': expense_form, 'expenses': expenses})
    else:
        expense_form = ExpenseForm()
        return render(request, 'myapp/index.html', {'expense_form': expense_form, 'expenses': expenses})

    
      
