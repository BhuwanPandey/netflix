from django import template

register = template.Library()

@register.filter(name='num_to_word')
def num_to_word(value):
    num_words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    return num_words.get(value, value)
