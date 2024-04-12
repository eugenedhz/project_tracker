from django.db import models

from tasks.models import Project, Task


class BugReport(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	STATUS_CHOICES = (
		('New', 'Новая'),
		('In_progress', 'В работе'),
		('Completed', 'Завершена')
	)
	status = models.CharField(
		max_length=50,
		choices=STATUS_CHOICES,
		default='New'
	)

	PRIORITY_CHOICES = (
		(1, 'Низкий'),
		(2, 'Ниже среднего'),
		(3, 'Средний'),
		(4, 'Высокий'),
		(5, 'Высший'),
	)
	priority = models.IntegerField(choices=PRIORITY_CHOICES)

	project = models.ForeignKey(
		Project,
		related_name='bug_reports',
		on_delete=models.CASCADE
	)

	task = models.ForeignKey(
		Task,
		related_name='bug_reports',
		on_delete=models.SET_NULL,
		null=True,
		blank=True
	)


	def __str__(self):
		return self.title


class FeatureRequest(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	STATUS_CHOICES = (
		('Reviewing', 'Рассмотрение'),
		('Accepted', 'Принято'),
		('Rejected', 'Отклонено')
	)
	status = models.CharField(
		max_length=50,
		choices=STATUS_CHOICES,
		default='Reviewing'
	)

	PRIORITY_CHOICES = (
		(1, 'Низкий'),
		(2, 'Ниже среднего'),
		(3, 'Средний'),
		(4, 'Высокий'),
		(5, 'Высший'),
	)
	priority = models.IntegerField(choices=PRIORITY_CHOICES)

	project = models.ForeignKey(
		Project,
		related_name='feature_requests',
		on_delete=models.CASCADE
	)

	task = models.ForeignKey(
		Task,
		related_name='feature_requests',
		on_delete=models.SET_NULL,
		null=True,
		blank=True
	)


	def __str__(self):
		return self.title