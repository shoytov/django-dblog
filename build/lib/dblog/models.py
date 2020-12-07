from django.db import models
from django.utils.timezone import now


# Create your models here.
class ErrorLog(models.Model):
    """ возникшие ошибки с полным описанием """
    url = models.CharField(max_length=250, verbose_name='Url, где произошла ошибка')
    exception_name = models.CharField(max_length=250, verbose_name='Exception name')
    exception = models.TextField(verbose_name='Exception')
    referer = models.CharField(max_length=250, verbose_name='Referer', null=True, blank=True)
    traceback = models.TextField(verbose_name='Full Traceback')
    date_created = models.DateTimeField(default=now, verbose_name='Дата и время ошибки')
    
    def __str__(self):
        return '{} - {} ({})'.format(self.url, self.exception_name, str(self.date_created))
    
    class Meta:
        verbose_name = 'Лог ошибки'
        verbose_name_plural = 'Логи ошибок'
