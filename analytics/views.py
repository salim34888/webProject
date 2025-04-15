from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tests.models import TestResult
from django.db import models
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse


@login_required
def dashboard(request):
    test_results = TestResult.objects.filter(user=request.user)
    test_stats = {
        'total_tests': test_results.count(),
        'avg_score': test_results.aggregate(models.Avg('score'))['score__avg'] or 0
    }

    return render(request, 'analytics/dashboard.html', {
        'test_stats': test_stats
    })


def generate_pdf_report(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(100, 800, "FUCK YOU LETHER MAN")

    p.drawString(100, 780, f"SLAVE: {request.user.username}")

    p.drawString(100, 700, "              .-. ")
    p.drawString(100, 690, "        .-'``(|||) ")
    p.drawString(100, 680, "     ,`\ \    `-`.                 88                         88 ")
    p.drawString(100, 670, "    /   \ '``-.   `                88                         88 ")
    p.drawString(100, 660, "  .-.  ,       `___:      88   88  88,888,  88   88  ,88888, 88888  88   88 ")
    p.drawString(100, 650, " (:::) :        ___       88   88  88   88  88   88  88   88  88    88   88 ")
    p.drawString(100, 640, "  `-`  `       ,   :      88   88  88   88  88   88  88   88  88    88   88 ")
    p.drawString(100, 630, "    \   / ,..-`   ,       88   88  88   88  88   88  88   88  88    88   88 ")
    p.drawString(100, 620, "     `./ /    .-.`        '88888'  '88888'  '88888'  88   88  '8888 '88888' ")
    p.drawString(100, 610, "        `-..-(   ) ")
    p.drawString(100, 600, "              `-` ")

    p.showPage()
    p.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')