from django.contrib import admin

from . import models


class GroupMemberInline(admin.TabularInline):   # Allows Group Members to be viewed in Group Admin Pane
    model = models.GroupMember

admin.site.register(models.Group)
