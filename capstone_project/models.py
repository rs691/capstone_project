import markdown
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager, Group,
                                        PermissionsMixin)
from django.db import models
from django.utils.text import slugify


class Attractions(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password_hash = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field is required")
        if not email:
            raise ValueError("The Email field is required")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    # Add these to resolve the reverse accessor clashes
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",  # A new, unique name
        blank=True,
        help_text="The groups this user belongs to.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions_set",  # Another unique name
        blank=True,
        help_text="Specific permissions for this user.",
    )


class Reservation(models.Model):
    reservation_id = models.CharField(max_length=10, unique=True, editable=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)
    guests = models.IntegerField()
    room_type = models.CharField(
        max_length=50,
        choices=[("single", "Single"), ("double", "Double"), ("suite", "Suite")],
    )
    check_in = models.DateField()
    check_out = models.DateField()
    reservation_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.reservation_id:
            self.reservation_id = self.generate_reservation_id()
        super().save(*args, **kwargs)

    def generate_reservation_id(self):
        import random
        import string

        letters = "".join(random.choices(string.ascii_uppercase, k=2))
        numbers = "".join(random.choices(string.digits, k=6))
        reservation_id = f"{letters}{numbers}"

        while Reservation.objects.filter(reservation_id=reservation_id).exists():
            letters = "".join(random.choices(string.ascii_uppercase, k=2))
            numbers = "".join(random.choices(string.digits, k=6))
            reservation_id = f"{letters}{numbers}"

        return reservation_id

    def __str__(self):
        return f"{self.reservation_id} - {self.first_name} {self.last_name} - {self.room_type} - {self.check_in} to {self.check_out} - {self.email}"


class Testimonial(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} - {self.message[:50]}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


class RestaurantReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
