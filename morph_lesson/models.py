from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Page(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='pages', on_delete=models.CASCADE)
    page = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    file_url = models.URLField(max_length=500)

    class Meta:
        unique_together = ('lesson', 'page')
        ordering = ['page']

    def __str__(self):
        return f"{self.lesson.title} - Page {self.page}: {self.title}"
