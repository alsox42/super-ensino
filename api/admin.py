from django.contrib import admin
from django.contrib import admin
from api.models import Alternative, Exercise, ExerciseGroup, Answer

class ExerciseGroupAdmin(admin.ModelAdmin):
    list_display = ['text', 'the_amount']
    search_fields = ['text',]
    list_filter = ['text', 'the_amount']

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'exercise', 'answered']
    search_fields = ['user', 'exercise', 'answered']
    list_filter = ['user', 'exercise', 'answered']

class AlternativeInlineAdmin(admin.StackedInline):
    model = Alternative
    extra = 0
    max_num = 4


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['order_num', 'description', ]
    search_fields = ['order_num']
    list_filter = ['order_num']

    inlines = [
        AlternativeInlineAdmin,
    ]

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(ExerciseGroup, ExerciseGroupAdmin)
admin.site.register(Answer, AnswerAdmin )


