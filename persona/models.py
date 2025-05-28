from django.db import models
from django.utils import timezone

# Create your models here.

class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    job_title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Job Title")
    bio = models.TextField(verbose_name="Biography")
    skills_summary = models.TextField(blank=True, null=True, verbose_name="Skills Summary")
    experience_summary = models.TextField(blank=True, null=True, verbose_name="Experience Summary")
    hobbies = models.TextField(blank=True, null=True, verbose_name="Hobbies & Interests")
    contact_email = models.EmailField(blank=True, null=True, verbose_name="Contact Email")
    additional_info = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Additional Information",
        help_text="A place for more detailed Q&A, personality traits, beliefs, and lifestyle details."
    )
    is_active = models.BooleanField(default=True, verbose_name="Is Active", help_text="Is this the currently active persona information?")
    last_updated = models.DateTimeField(default=timezone.now, verbose_name="Last Updated")

    def save(self, *args, **kwargs):
        self.last_updated = timezone.now() # Ensure last_updated is set on each save
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Personal Information"
        verbose_name_plural = "Personal Infos"
        ordering = ['-last_updated']
        # Ensure only one record has is_active=True (if a singleton is strictly needed)
        # constraints = [
        #     models.UniqueConstraint(fields=['is_active'], condition=models.Q(is_active=True), name='unique_active_profile')
        # ]
