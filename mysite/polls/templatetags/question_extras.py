from django import template
from django.utils.safestring import mark_safe

import markdown2

from polls.models import Question

register = template.Library()


@register.simple_tag
def newest_question():
    ''' Gets the most recent question that was added to the library. '''
    return Question.objects.latest('pub_date')

# the long way. we use a decorator instead
#register.simple_tab('newest_question')


@register.inclusion_tag('polls/question_nav.html')
def nav_questions_list():
    '''Returns dictionary of questions to display as navigation pane'''
    questions = Question.objects.all()
    return {'questions': questions}

# the long way again
#register.inclusion_tag('polls/question_nav.html')(nav_questions_list)


@register.filter('time_estimate')
def time_estimate(word_count):
    ''' Estimates the number of minutes that it will take to complete a step 
    based on the passed-in wordcount'''
    minutes = round(word_count/20)
    return minutes


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''Converts markdown text to HTML'''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
