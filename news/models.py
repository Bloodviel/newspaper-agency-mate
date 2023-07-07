from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from newspaper_agency import settings


class Topic(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=63)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="newspapers"
    )
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="newspapers"
    )

    class Meta:
        ordering = ["published_date"]

    def __str__(self):
        return f"{self.title}"


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("news:redactor-detail", kwargs={"pk": self.pk})
