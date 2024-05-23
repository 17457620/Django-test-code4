from django.contrib import admin
from .models import Employee, PerformanceReview, Branch
#from .models import Product, Category

admin.site.register(Employee)
admin.site.register(PerformanceReview)
admin.site.register(Branch)
# admin.site.register(Product)
# admin.site.register(Category)