from django.contrib.auth.models import User
from django.db import models

# Lista de Exercicios
class ExerciseGroup(models.Model):
    text  = models.CharField("Nome da Lista?", max_length=150)
    the_amount = models.IntegerField("Quant. de Exerc.", default=0)

    class Meta:
        verbose_name = 'Grupo de Exercicio'
        verbose_name_plural = 'Grupos de Exercicios'
        ordering = ['text']

    def __str__(self):
        return self.text

# Exercicio
class Exercise(models.Model):
    exercise_group = models.ForeignKey("ExerciseGroup",
                                       verbose_name="Lista de Exercício",
                                       related_name="exercises",
                                       on_delete=models.PROTECT,
                                       null=True)
    order_num   = models.CharField("Num. de Ordem", max_length=20)
    title       = models.CharField("Titulo", max_length=50)
    description = models.TextField("Descrição")
    question   = models.CharField("Pergunta", max_length=100)

    class Meta:
        verbose_name = 'Exercicio'
        verbose_name_plural = 'Exercicios'
        ordering = ['order_num']

    def __str__(self):
        return self.order_num
    

# Alternativas do exercicio
class Alternative(models.Model):
    LETTER_CHOICE = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),

    )

    letter   = models.CharField("Letra da Altern.", max_length=1, choices=LETTER_CHOICE)
    text     = models.CharField("Texto da Altern.", max_length=150)
    is_right = models.BooleanField("Afirmativa correta?", default=False)
    exercise = models.ForeignKey("Exercise", 
                                 on_delete=models.CASCADE,
                                 null=True)
    
    class Meta:
        verbose_name = 'Alternativa'
        verbose_name_plural = 'Alternativas'
        ordering = ['letter']

    def __str__(self):
        return self.text

# Respostas do usuario
class Answer(models.Model):
    user     = models.ForeignKey(User,
                                verbose_name="Usuário",
                                 on_delete=models.CASCADE)
    exercise = models.ForeignKey("Exercise",
                                 verbose_name="Exercicio",
                                 on_delete=models.CASCADE)
    answered = models.ForeignKey("Alternative",
                                 verbose_name="Escolha do usuário",
                                 related_name="answer",
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'
        ordering = ['user', 'exercise']

    def __str__(self):
        return self.answered.letter