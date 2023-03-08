from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.church import Church
from .models.wing import Wing
from .models.user import User
from .models.due import Due

# Register your models here.

admin.site.register(Church)
admin.site.register(Wing)
admin.site.register(User)
admin.site.register(Due)