from django.contrib import admin
from . models import Student

@admin.register(Student)
class PersonAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('timestamp','ic_no','name',  'address1', 'address2', 'city', 'mukim', 'parlimen', 'state', 'poskod','income',)
        return self.readonly_fields
    pass




#admin.site.register(Student)

