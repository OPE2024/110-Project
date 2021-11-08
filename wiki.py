from constants import ADVANCED, ADVANCED_TO_QUESTION, BASIC, YEARS, METADATA
import json
import re
import requests

threshold = 6

def _find_keywords(article):
  keywords = []
  count = {}
  final_count = {}

  article = re.sub('\W+',' ', article).split(' ')

  for word in article:
    count[word.lower()] = count[word.lower()] + 1 if word.lower() in count.keys() else 1

  for key, value in count.items():
    if value > threshold and len(key) > 2:
      keywords.append(key)
      final_count[key] = value

  return keywords

def _create_id_to_metadata(info):
  """Creates a dictionary of article ID to title, author, timestamp, num_characters, and list of keywords

  Args:
    info - JSON of information from BigQuery
  """
  id_to_metadata = {}
  id_set = set()
  
  for item in info:
    article_id = item.get('id')
    #if article_id in id_set:
    #  print(article_id)
    id_set.add(article_id)
    # Delete the id from the dict
    del item['id']
  

def _metadata_list(info):
  """Creates a list of title, author, timestamp, num_characters, and list of keywords

  Args:
    info - JSON of information from BigQuery
  """

def states_names():
  """ Returns a list of article titles
  """
  return list(map(lambda article: article.get('state'), YEARS))

def year_metadata():
  """ Returns a list of article metadata (list of lists)
  """
  return METADATA

def _count_for_titles():
  """ Returns titles that have words in other titles
  """
  count = {}
  titles = states_names()
  for title in titles:
    title_split = title.split(' ')
    for word in title_split:
      count[word] = count[title] + 1 if title in count.keys() else 1

  for key, value in count.items():
    if value > 1:
      print(key)
  return count

def ask_search():
  return input(BASIC)

def ask_advanced_search():
  request = int(input(ADVANCED))
  answer = input(ADVANCED_TO_QUESTION[request]) if request != 0 and request != 5 else ''
  return [request, answer if request >= 1 else int(answer)]