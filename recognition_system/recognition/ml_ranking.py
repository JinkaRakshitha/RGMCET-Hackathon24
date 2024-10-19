import numpy as np
from sklearn.linear_model import LinearRegression

def calculate_ranking(students):
    # Input data: academic_score, consistency_score, core_engineering_score, etc.
    X = np.array([[student.academic_score, student.consistency_score, student.core_engineering_score, 
                   student.hackathon_participation, student.paper_presentations, student.teacher_assistance]
                  for student in students])
    
    # Example weights: these can be dynamic using a machine learning model
    weights = np.array([0.4, 0.2, 0.2, 0.1, 0.05, 0.05])
    
    # Calculate total score using weighted sum
    total_scores = np.dot(X, weights)

    # Rank students based on the total score
    rankings = np.argsort(total_scores)[::-1]  # Sort in descending order

    return [(students[idx], total_scores[idx], rank + 1) for rank, idx in enumerate(rankings)]
