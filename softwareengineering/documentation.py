#1 Generating docstrin for function

# Complete the function's docstring
def tokenize(text, regex=r'[a-zA-z]+'):
  """Split text into tokens using a regular expression

  :param text: text to be tokenized
  :param regex: regular expression used to match tokens using re.findall 
  :return: a list of resulting tokens

  >>> tokenize('the rain in spain')
  ['the', 'rain', 'in', 'spain']
  """
  return re.findall(regex, text, flags=re.IGNORECASE)

# Print the docstring
help(tokenize)




# Tools
    # Sphinx generates html pages of docstrings
    
# Documenting classes for Sphinx: 
    
from text_analyzer import Document

class SocialMedia(Document):
"""Analyze text data from social media

:param text: social media text to analyze

:ivar hashtag_counts: Counter object containing counts of hashtags used in text
:ivar mention_counts: Counter object containing counts of @mentions used in text
"""
def __init__(self, text):
    Document.__init__(self, text)
    self.hashtag_counts = self._count_hashtags()
    self.mention_counts = self._count_mentions()
