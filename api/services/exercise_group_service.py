from api.models import ExerciseGroup

def list_exercise_group():
    exercise_groups = ExerciseGroup.objects.all()
    return exercise_groups
