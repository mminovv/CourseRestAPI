from django.contrib import admin
from api.models import Course, Contact, Branch, Category
# Register your models here.

admin.site.register(Course)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Branch)
