# Django модуль для логирования ошибок в базу данных

Модуль создан для удобства просмотра логов сервера через админ-панель Django.    

Каждая запись лога содержит следущую информацию:
1. часть url страницы сайта, на которой возникла ошибка (в случае, когда ошибка возникла на главной, то значение поля будет "/");
1. название исключения;
1. описание исключения;
1. текст traceback;
1. url перехода на страницу, на которой возникла ошибка;
1. дата и время возникновения ошибки.

-----

## Настройка и запуск

В setting.py    
- добавить в INSTALLED_APPS `'dblog.apps.DblogConfig'`
- добавить в MIDDLEWARE `'dblog.middleware.ExceptionLoggingMiddleware'`

## Использование loguru
```
logger.configure(handlers=[{'sink': LoguruDbHandler('id_place_of_log')}])
logger.warning('message')
```

Выполнить `python3 manage.py migrate`

