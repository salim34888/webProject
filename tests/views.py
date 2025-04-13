from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Test, Question, Answer, TestResult


# tests/views.py
@login_required
def test_list(request):
    # Создаем тест если база пуста
    if not Test.objects.exists():
        create_sample_test()

    tests = Test.objects.all()
    return render(request, 'tests/list.html', {'tests': tests})

def create_sample_test():
    # Создаем тестовый тест если его нет
    test, created = Test.objects.get_or_create(
        title="Тест на коммуникацию",
        defaults={
            'description': "Базовый тест для проверки навыков общения",
            'difficulty': 'easy',
            'is_pro': False
        }
    )
    print(created)
    if not(created):
        questions_data = [
            {
                'text': "Как лучше поступить в конфликтной ситуации?",
                'answers': [
                    {'text': "Кричать", 'is_correct': False},
                    {'text': "Спокойно обсудить", 'is_correct': True},
                    {'text': "Игнорировать", 'is_correct': False},
                ]
            },
            {
                'text': "Что важно в деловом общении?",
                'answers': [
                    {'text': "Пунктуальность", 'is_correct': True},
                    {'text': "Эмоциональность", 'is_correct': False},
                    {'text': "Многословие", 'is_correct': False},
                ]
            },
            {
                'text': "Как показать что вы слушаете?",
                'answers': [
                    {'text': "Кивать головой", 'is_correct': True},
                    {'text': "Смотреть в телефон", 'is_correct': False},
                    {'text': "Перебивать", 'is_correct': False},
                ]
            }
        ]

        for q_data in questions_data:
            question = Question.objects.create(test=test, text=q_data['text'])
            for a_data in q_data['answers']:
                Answer.objects.create(
                    question=question,
                    text=a_data['text'],
                    is_correct=a_data['is_correct']
                )


@login_required
def take_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)

    # Принудительно создаем тест если вопросов нет
    if not test.question_set.exists():
        create_sample_test()
        test.refresh_from_db()

    if request.method == 'POST':
        # Обработка ответов
        score = 0
        total_questions = test.question_set.count()

        for question in test.question_set.all():
            answer_id = request.POST.get(f'question_{question.id}')
            if answer_id:
                answer = Answer.objects.get(id=int(answer_id))
                if answer.is_correct:
                    score += 1

        # Сохраняем результат
        TestResult.objects.create(
            user=request.user,
            test=test,
            score=score
        )

        return render(request, 'tests/result.html', {
            'test': test,
            'score': score,
            'total': total_questions,
            'questions': test.question_set.prefetch_related('answer_set').all(),
            'percent': int((score / total_questions) * 100)
        })

    questions = test.question_set.prefetch_related('answer_set')
    return render(request, 'tests/take.html', {
        'test': test,
        'questions': questions
    })