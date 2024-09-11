import os
import django
import sys
import json

# Django 설정 파일 지정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kmu_quiz.settings')
django.setup()

from quiz.models import Test, Question, Selection

def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def create_test_from_json(file_path):
    data = load_json_data(file_path)
    
    quiz_title = data.get('title', '')
    quiz_description = data.get('description', '')
    
    test = Test.objects.create(
        title=quiz_title,
        description=quiz_description,
        engagement=0,
        likes=0
    )

    for index, question_data in enumerate(data.get('questions', []), start=1):
        question = Question.objects.create(
            test=test,
            content=question_data.get('content', ''),
            index=question_data.get('index', index),
            seconds=20,
            score=1
        )
        
        for selection_data in question_data.get('selections', []):
            Selection.objects.create(
                question=question,
                content=selection_data.get('content', ''),
                is_correct=selection_data.get('is_correct', False),
                index=selection_data.get('index', 1)
            )

    print(f"{quiz_title} 퀴즈가 성공적으로 생성되었습니다. 퀴즈 ID: {test.id}")

def main():
    dataset_dir = 'dataset'
    for filename in os.listdir(dataset_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(dataset_dir, filename)
            create_test_from_json(file_path)

if __name__ == "__main__":
    main()

# 생성된 모든 퀴즈 확인
for test in Test.objects.all():
    print(f"\n퀴즈 제목: {test.title}")
    print(f"문제 수: {test.question.count()}")

    for question in test.question.all().order_by('index'):
        print(f"\n문제 {question.index}: {question.content}")
        for selection in question.selection.all().order_by('index'):
            print(f"  - {selection.content} ({'정답' if selection.is_correct else '오답'})")
