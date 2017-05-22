from __future__ import unicode_literals

from django.db import models

# Create your models here.

from payments.lexers import get_all_lexers
from payments.styles import get_all_styles

LEXER = [item in item for get_all_lexers() if item [1]]
LANGUAGE_CHOICE = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class snippets(models.Model)
