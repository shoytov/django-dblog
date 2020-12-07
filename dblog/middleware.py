import traceback

from .models import ErrorLog


class ExceptionLoggingMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response    
        
    def __call__(self, request):
        return self.get_response(request)        
    
    def process_exception(self, request, exception):
        new_error = ErrorLog()
        
        new_error.url = request.get_full_path()
        new_error.exception_name = exception.__class__.__name__
        new_error.exception = str(exception)
        new_error.referer = request.META.get('HTTP_REFERER')
        new_error.traceback = traceback.format_exc()
        
        new_error.save()
