from api.models import Answer

def list_answers():
    answers = Answer.objects.all()
    return answers
