from api.models import Alternative


def list_alternatives():
    alternatives = Alternative.objects.all()
    return alternatives
