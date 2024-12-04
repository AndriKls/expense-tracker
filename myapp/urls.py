from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:pk>', views.UpdateExpenseView.as_view(), name='update'),
    path('expense/<int:pk>/delete/', views.ExpenseDeleteView.as_view(), name='expense_delete'),
]