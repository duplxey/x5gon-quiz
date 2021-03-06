from django.shortcuts import render, redirect

from accounts.models import ProfileStatistics
from quiz.models import DocumentStatistics, Quiz, QuizUserResult
from x5quiz.errors import search_failed, unknown_document, quiz_not_generated_yet
from x5quiz.x5gon import search_documents, get_document, get_document_content, get_document_url


def index_view(request):
    return render(request, "quiz/index.html", {})


def search_view(request):
    query = None
    if request.method == 'POST':
        query = request.POST['query']

    if query is None or len(query) < 2:
        return search_failed(request)

    query = query.replace(" ", "")
    return render(request, "quiz/search.html", {'keyword': query, 'results': search_documents(query)})


def learn_view(request, document_id):
    statistics = None

    document = get_document(document_id)

    if not DocumentStatistics.objects.filter(document_id=document_id).exists():
        statistics = DocumentStatistics.objects.create(document_id=document_id, views=1, title=document["title"])
    else:
        statistics = DocumentStatistics.objects.get(document_id=document_id)
        statistics.increase_views()

    if request.user.is_authenticated:
        ProfileStatistics.objects.get(user=request.user).increase_documents_read()

    return render(request, "quiz/learn.html", {
        'document': document,
        'content': get_document_content(document_id),
        'url': get_document_url(document_id),
        'statistics': statistics,
    })


def quiz_view(request, document_id):
    if not DocumentStatistics.objects.filter(document_id=document_id).exists():
        return unknown_document(request)

    return render(request, "quiz/quiz.html", {
        'document': get_document(document_id),
        'content': get_document_content(document_id),
        'quiz': Quiz.objects.get(document_id=document_id),
    })


def quiz_submit_view(request, quiz_pk):
    if not Quiz.objects.filter(pk=quiz_pk).exists():
        return quiz_not_generated_yet(request)

    quiz = Quiz.objects.get(pk=quiz_pk)
    correct = 0
    buffer = ""

    for element in request.POST:
        if element == "csrfmiddlewaretoken": continue
        question = quiz.get_quiz_question(int(element[0])-1)
        buffer = buffer + str(int(element[2])-1) + "-"
        if question.correct == int(element[2])-1:
            correct = correct + 1

    wrong = quiz.get_quiz_questions().count() - correct

    results = QuizUserResult.objects.create(quiz=quiz, user=request.user, correct=correct, wrong=wrong, data=buffer[:-1])
    results.save()

    stats = ProfileStatistics.objects.get(user=request.user)
    stats.add_points(correct)
    stats.increase_quizzes_played()

    return render(request, "quiz/results.html", {
        'quiz': quiz,
        'results': results,
        'data': buffer[:-1],
        'leaderboard': QuizUserResult.objects.filter(quiz=quiz).order_by("-correct")
    })


def rate_view(request, document_id, rating):
    if not DocumentStatistics.objects.filter(document_id=document_id).exists():
        return unknown_document(request)

    document_id = int(document_id)
    s = DocumentStatistics.objects.get(pk=document_id)
    s.rating = rating

    return redirect("quiz-learn", document_id=document_id)