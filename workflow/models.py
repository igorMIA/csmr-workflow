from django.db import models


class Workflow(models.Model):
    api_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=255)
    instruction = models.TextField()
    judgment = models.TextField()
    prediction = models.TextField()


class Rater(models.Model):
    api_id = models.PositiveIntegerField(unique=True)
    age = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    workflow = models.ForeignKey('Workflow', on_delete=models.CASCADE)


class Item(models.Model):
    api_id = models.PositiveIntegerField(unique=True)
    url = models.URLField()
    category = models.CharField(max_length=255)


class ItemWorkflow(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    workflow = models.ForeignKey('Workflow', on_delete=models.CASCADE)
    raters_desired = models.PositiveIntegerField()
    raters_actual = models.PositiveIntegerField()


class Answer(models.Model):
    rater = models.ForeignKey('Rater', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    workflow = models.ForeignKey('Workflow', on_delete=models.CASCADE)
    answer_start = models.DateTimeField()
    answer_end = models.DateTimeField()
    rater_answer_judgment = models.TextField(blank=True, null=True)
    rater_answer_predict_a = models.TextField(blank=True, null=True)
    rater_answer_predict_b = models.TextField(blank=True, null=True)
    rater_answer_predict_c = models.TextField(blank=True, null=True)
    evidence_url = models.URLField(null=True, blank=True)
