from django.contrib import admin
from .models import PersonalInfo

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'is_active', 'last_updated')
    list_filter = ('is_active',)
    search_fields = ('full_name', 'job_title', 'bio', 'skills_summary', 'experience_summary')
    # Consider making the is_active field editable directly in the list view
    # list_editable = ('is_active',)

    # For TextField, the default widget might be small, consider customizing it
    # from django.db import models
    # from django.forms import Textarea
    # formfield_overrides = {
    #     models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    # }

# Or the simpler registration method:
# admin.site.register(PersonalInfo)
