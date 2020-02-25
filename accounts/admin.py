from django.contrib import admin
from accounts.models import User
from accounts.forms import UserChangeForm,UserCreationForm


class myAdmin(admin.ModelAdmin):
    search_fields=['email','username','first_name','last_name']
    list_display=('username','first_name','last_name','email','is_admin','is_staff','is_active')
    list_filter=('is_admin','is_staff','is_active')
    form=UserChangeForm
    add_form=UserCreationForm

admin.site.register(User,myAdmin)
