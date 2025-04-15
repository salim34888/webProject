from .models import UserActivity

def log_activity(user, activity_type, content_id, content_title):
    UserActivity.objects.create(
        user=user,
        activity_type=activity_type,
        content_id=content_id,
        content_title=content_title
    )