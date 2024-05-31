from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.conf import settings

class OtherInfo(models.Model):
    alumni = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='other_info')  # Temporary default
    current_job_title = models.CharField(max_length=100)
    current_company = models.CharField(max_length=100)
    responsibilities = models.TextField()
    skills = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='media/resumes', blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.current_job_title} at {self.current_company}"

class History(models.Model):
    other_info = models.ForeignKey(OtherInfo, on_delete=models.CASCADE, related_name='histories')
    job_title = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name} ({self.start_year}-{self.end_year})"

class Achieve(models.Model):
    other_info = models.ForeignKey(OtherInfo, on_delete=models.CASCADE, related_name='achievements')
    achievement_title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    attachment = models.FileField(upload_to='media/achievements', blank=True, null=True)

    def __str__(self):
        return self.achievement_title


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import date

class CustomUserManager(BaseUserManager):
    def create_user(self, registration_no=None, username=None, password=None, **extra_fields):
        if not registration_no and not username:
            raise ValueError('The Registration Number or Username must be set')
        if registration_no:
            user = self.model(registration_no=registration_no, **extra_fields)
        else:
            user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not extra_fields.get('birthdate'):
            raise ValueError('Superusers must have a birthdate.')
        return self.create_user(username=username, password=password, **extra_fields)

class UniversityBranch(models.Model):
    BRANCH_CHOICES=(
        ('Tunguu Campus','Tunguu'),
        ('Maruhubi Campus','Maruhubi'),
        ('Kilimani Campus','Kilimani'),
        ('Kizimbani Campus','Kizimbani'),
        ('Vuga Campus','Vuga'),
        ('Chwaka Campus','Chwaka')
    )
    
    name = models.CharField(max_length=100, choices=BRANCH_CHOICES)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(UniversityBranch, related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Alumni(AbstractBaseUser, PermissionsMixin):
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=7)
    fiv_index = models.CharField(max_length=20)
    fvi_index = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    course_name = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    registration_no = models.CharField(max_length=50, unique=True, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=50)
    branch = models.ForeignKey(UniversityBranch, on_delete=models.SET_NULL, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'birthdate', 'surname', 'first_name']

    def __str__(self):
        return self.registration_no if self.registration_no else self.username

    def save(self, *args, **kwargs):
        if self.birthdate:
            today = date.today()
            self.age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        super(Alumni, self).save(*args, **kwargs)


class EducationalBackground(models.Model):
    alumni = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='educational_background')  # Temporary default
    # Primary School Details
    primary_school_name = models.CharField(max_length=255)
    primary_school_year_attended = models.CharField(max_length=50)
    primary_school_address = models.CharField(max_length=255)
    
    # Secondary School Details
    secondary_school_name = models.CharField(max_length=255)
    secondary_school_year_attended = models.CharField(max_length=50)
    secondary_school_address = models.CharField(max_length=255)
    
    # VETA Details (Vocational Education and Training Authority)
    veta_name = models.CharField(max_length=255, blank=True, null=True)
    veta_program = models.CharField(max_length=255, blank=True, null=True)
    veta_year_attended = models.CharField(max_length=50, blank=True, null=True)
    veta_address = models.CharField(max_length=255, blank=True, null=True)
    
    # College Details
    college_name = models.CharField(max_length=255, blank=True, null=True)
    college_program = models.CharField(max_length=255, blank=True, null=True)
    college_year_attended = models.CharField(max_length=50, blank=True, null=True)
    college_address = models.CharField(max_length=255, blank=True, null=True)
    
    # university Details
    university_name = models.CharField(max_length=255)
    university_course_title= models.CharField(max_length=255)
    university_relevant_course = models.TextField()
    university_graduation_year = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f'{self.primary_school_name} - {self.secondary_school_name}'
