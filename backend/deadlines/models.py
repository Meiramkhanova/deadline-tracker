from django.db import models


class Deadline(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    due_at = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["due_at"]

    def __str__(self):
        return f"{self.subject}: {self.title}"
