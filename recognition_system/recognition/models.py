from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    batch = models.IntegerField()
    academic_score = models.FloatField()
    consistency_score = models.FloatField()
    core_engineering_score = models.FloatField()
    hackathon_participation = models.IntegerField()
    paper_presentations = models.IntegerField()
    teacher_assistance = models.IntegerField()

    def __str__(self):
        return self.name

class PerformanceRanking(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_score = models.FloatField()
    rank = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - Rank: {self.rank}"

