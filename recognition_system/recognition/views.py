from django.shortcuts import render
from .models import Student, PerformanceRanking
from .ml_ranking import calculate_ranking

def generate_rankings():
    students = Student.objects.all()
    rankings = calculate_ranking(students)
    
    # Clear previous rankings
    PerformanceRanking.objects.all().delete()
    
    # Save new rankings
    for student, score, rank in rankings:
        PerformanceRanking.objects.create(student=student, total_score=score, rank=rank)

def display_rankings(request):
    generate_rankings()
    rankings = PerformanceRanking.objects.all().order_by('rank')
    return render(request, 'rankings.html', {'rankings': rankings})

