from django.db import models

# Create your models here.

class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=100, help_text="")
    job_title = models.CharField(max_length=100, help_text="")
    bio = models.TextField(help_text="")
    skills_summary = models.TextField(help_text="")
    experience_summary = models.TextField(help_text="")
    hobbies = models.TextField(help_text="", blank=True, null=True)
    contact_email = models.EmailField(help_text="", blank=True, null=True)
    # linkedin_url = models.URLField(blank=True, null=True)
    # github_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True, help_text="Mark this entry as the currently active primary information")
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - Profile"

    class Meta:
        verbose_name = "Personal Information"
        verbose_name_plural = "Personal Information"
        # Ensure only one record has is_active=True (if a singleton is strictly needed)
        # constraints = [
        #     models.UniqueConstraint(fields=['is_active'], condition=models.Q(is_active=True), name='unique_active_profile')
        # ]
