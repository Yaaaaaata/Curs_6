from django.contrib import admin

from newsletter.models import Newsletter, Message, Client, Log


admin.site.register(Client)
admin.site.register(Log)
admin.site.register(Message)
admin.site.register(Newsletter)
