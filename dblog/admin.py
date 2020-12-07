from django.contrib import admin

from .models import ErrorLog


class ErrorLogAdmin(admin.ModelAdmin):
    """ logs """
    model = ErrorLog
    list_display = ('url', 'exception_name', 'exception', 'referer', 'traceback', 'date_created')
    list_display_links = ('url', 'exception_name')
    search_fields = ['url']
    

# Register your models here.
admin.site.register(ErrorLog, ErrorLogAdmin)