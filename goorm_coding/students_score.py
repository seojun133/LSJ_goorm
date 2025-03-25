scores_data = '''
학생1: 홍길동, 성적: 85
학생2: 김철수, 성적: 90
학생3: 이영희, 성적: 78
학생4: 박민지, 성적: 92
학생5: 최준호, 성적: 88
'''

students = []
scores = []

for i in scores_data.strip().split("\n"):
    lines = i.split(", 성적: ")
    name = lines[0].split(": ")[1]
    score = int(lines[1])

    students.append(name)
    scores.append(score)

print(students)
print(scores)

average_score = sum(scores) / len(scores)
print("성적 평균:", average_score)
