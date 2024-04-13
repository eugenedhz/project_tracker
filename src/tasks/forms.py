from django.forms import (
    ModelForm, CharField, EmailField, Form, Textarea
)

from .models import Project, Task


class FeedbackForm(Form):
    name = CharField(label='Ваше имя', max_length=100)
    email = EmailField(label='Электронная почта')
    message = CharField(widget=Textarea, label='Сообщение')


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'assignee']