from django.db import models

# Create your models here.


class Job(models.Model):
    """
    A job with information found externally. Can be
    created by an Admin or a SiteUser with Emoployer
    account type.
    """
    EDUCATION_CHOICES = (
        ('HS', 'High School/GRE'),
        ('BA/BS', 'Bachelor of Art and Science'),
        ('MA/MS', 'Master of Art and Science'),
        ('PHD', 'Doctor of Philosophy')
    )
    JOB_CATEGORY_CHOICES = (
        ('TECHNICIAN', 'Technician'),
        ('CHEMIST', 'Chemist'),
    )
    JOB_TYPE_CHOICES = (
        ('FT', 'Full-Time'),
        ('PT', 'Part-Time'),
        ('1099', 'Contract'),
    )
    description = models.TextField()
    expiry = models.DateField()
    post_date = models.DateField(auto_now_add=True)
    job_category = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        choices=JOB_CATEGORY_CHOICES,
    )
    job_type = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        choices=JOB_TYPE_CHOICES,
    )
    education = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        choices=EDUCATION_CHOICES,
    )
    experience = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    headline = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    skills = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    city = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    state = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    salary = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    benefits = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    link = models.URLField(
        blank=True,
        null=True,
        max_length=255,
    )
