from typing import Optional
from django.core.handlers.wsgi import WSGIRequest
from django.contrib import admin
from . models import Account
from . models import Student
from . models import Group

 
# Register your models here.
class AccountAdmin (admin.ModelAdmin):
    readonly_fields = ()
    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Account] = None
        ) -> tuple:
        if obj:
            return self.readonly_fields + ('description',)
        return self.readonly_fields

admin.site.register(
    Account, AccountAdmin
)

class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ()
    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Account] = None
    ) -> tuple:
        if obj :
            return self.readonly_fields + ('age',)
        return self.readonly_fields 


admin.site.register(
    Student, StudentAdmin
)

class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ()
    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Account] = None
    ) -> tuple:
        if obj:
            return self.readonly_fields + ('description',)
        return self.readonly_fields

admin.site.register(
    Group, GroupAdmin
)