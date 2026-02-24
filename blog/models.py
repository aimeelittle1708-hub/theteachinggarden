from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from cloudinary.models import CloudinaryField


# ----------------------
# Custom User Manager
# ----------------------
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email=email, name=name, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# ----------------------
# Custom User Model
# ----------------------
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email


# ----------------------
# Resource Model
# ----------------------
class Resource(models.Model):
    SUBJECT_CHOICES = [
        ("Maths", "Maths"),
        ("Science", "Science"),
        ("English", "English"),
        ("History", "History"),
        ("Geography", "Geography"),
        ("Art", "Art"),
        ("Music", "Music"),
        ("PE", "PE"),
        ("Computing", "Computing"),
        ("Design & Technology", "Design & Technology"),
        ("MFL", "MFL"),
        ("Citizenship", "Citizenship"),
        ("Cookery", "Cookery"),
        ("Other", "Other"),
    ]

    YEAR_CHOICES = [
        ("Year 1", "Year 1"),
        ("Year 2", "Year 2"),
        ("Year 3", "Year 3"),
        ("Year 4", "Year 4"),
        ("Year 5", "Year 5"),
        ("Year 6", "Year 6"),
        ("KS3", "KS3"),
        ("KS4", "KS4"),
        ("KS5", "KS5"),
        ("Other", "Other"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    year_group = models.CharField(max_length=50, choices=YEAR_CHOICES)

    file = CloudinaryField("resource_file", resource_type="raw")

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="resources"
    )

    # Approval fields 
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="approved_resources"
    )
    approved_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
    
    @property
    def file_url(self):
        """
        Some viewers require https.
        """
        url = self.file.url
        if url and url.startswith("http://"):
            url = url.replace("http://", "https://")
        return url

    @property
    def file_ext(self):
        url = (self.file.url or "").split("?")[0].lower()
        if "." not in url:
            return ""
        return url.rsplit(".", 1)[-1]

    @property
    def is_image(self):
        return self.file_ext in {"jpg", "jpeg", "png", "gif", "webp"}

    @property
    def is_pdf(self):
        return self.file_ext == "pdf"

    @property
    def is_office(self):
        return self.file_ext in {"doc", "docx", "ppt", "pptx"}

    @property
    def office_viewer_url(self):
        """
        Office online viewer needs a public URL.
        """
        from urllib.parse import quote
        return f"https://view.officeapps.live.com/op/embed.aspx?src={quote(self.file_url)}"

    def __str__(self):
        return self.title


# ----------------------
# Post Model
# ----------------------
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    is_approved = models.BooleanField(default=True)  # or False if you want moderation
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="approved_posts"
    )
    approved_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

# ----------------------
# Comment Model
# ----------------------
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        null=True,
        blank=True
    )

    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
        related_name="comments",
        null=True,
        blank=True
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    content = models.TextField()

    # moderation
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="approved_comments"
    )
    approved_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment by {self.author}"