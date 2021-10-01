from api.models import Exercise

def list_exercises():
    exercises = Exercise.objects.all()
    return exercises
