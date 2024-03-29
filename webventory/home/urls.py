"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    # Home page.
    path('', views.home),
    # Home page.
    path('home/', views.home),
    # Login page.
    path('login', views.user_login),
    # User Landing page.
    path('userHome', views.user_landing_page),
    # Logout redirect.
    path('logout', views.user_logout),
    # Inventory page.
    path('userInventory/', views.user_inventory),
    path('userInventory/deleteError/<int:delError>', views.user_inventory),
    # Inventory Insights page.
    path('userInsights/', views.user_insights),
    path('userInsights/<int:item_id>/', views.user_insights),
    # Specific Inventory Information given id number.
    path('userInventory/<int:item_id>/', views.user_inventory),
    # Edit Item in Inventory page.
    path('userInventory/<int:item_id>/edit', views.user_inventory_edit),
    # Sign-up Page
    path('signup', views.user_signup),
    path('create', views.create_item),
    path('userInventory/<int:item_id>/delete', views.delete_item),
    path('userInventory/<int:item_id>/<int:item_range>/delete', views.delete_item),
    # Range
    path('userInventory/<int:item_id>/<int:item_range>/edit',
         views.user_inventory_edit),
    path('userInventory/<int:item_id>/<int:item_range>/', views.user_inventory),
    path('userInventory/<int:item_id>/<int:item_range>/edit',
         views.user_inventory_edit),
    path('userInsights/<int:item_id>/<int:item_range>/', views.user_insights),
    path('userVisibility/', views.user_users),
    path('userVisibility/<int:item_id>/<int:item_range>/', views.user_users),
    path('userVisibility/<int:item_id>/', views.user_users),
]
