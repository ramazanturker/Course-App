from django.contrib import admin
from .models import Course, Category

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "isActive", "isHome", "slug", "category_list",)
    list_display_links = ("title", "slug",)
    prepopulated_fields = { "slug": ("title",), }
    list_filter = ("title", "isActive", "isHome",)
    list_editable = ("isActive", "isHome",)
    search_fields = ("title", "description",)
    
    def category_list(self, object):
        html = ""
        for category in object.categories.all():
            html += category.name + " "
        return html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "course_count")
    prepopulated_fields = { "slug": ("name",), }
    
    def course_count(self, object):
        return object.course_set.count()