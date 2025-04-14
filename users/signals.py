from django.db.models.signals import post_save
from django.dispatch import receiver
from tests.models import TestResult
from users.models import UserRanking

@receiver(post_save, sender=TestResult)
def update_ranking(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        ranking, created = UserRanking.objects.get_or_create(user=user)
        ranking.total_score += instance.score
        ranking.tests_completed += 1
        ranking.save()