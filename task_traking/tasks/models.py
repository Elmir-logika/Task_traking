from django.db import models

# ////////////////
from django.contrib.auth.models import User


class Task(models.Model):

    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("Done", "Done"),
    ]

    PRIORITY_SHOICES = [
        ("low","Low"),
        ("medium","Medium"),
        ("high","High"),
    ]

    title = models.CharField(max_length=256)
    descriptions = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=20, choices=PRIORITY_SHOICES, default="medium")
    due_date = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "creator")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title
    
class Comment(models.Model):
    task = models.ForeignKey(Task, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.task}'