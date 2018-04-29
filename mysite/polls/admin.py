from django.contrib import admin

from .models import Question, Choice


#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #can define the order of the fields
#    fields = ['pub_date', 'question_text']
    #or define fieldsets
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Keywords',         {'fields': ['description']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}), 
    ]
    inlines = [ChoiceInline,]
    list_display = ('question_text', 'description', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text', 'description']


admin.site.register(Question, QuestionAdmin)


