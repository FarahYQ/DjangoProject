from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell
# from todo.models import TodoItem
# TodoItem.objects.all()
# a = TodoItem(title="Organize", content="Put away books and clothes")
# a.save()
# TodoItem.objects.get(id=1) --> creates a query for object with id 1

