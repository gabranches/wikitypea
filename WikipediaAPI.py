import requests
import json
import re


endpoint = 'https://en.wikipedia.org/w/api.php'


def get_random_article():

    params = '?action=query&format=json&generator=random&rnlimit=1&grnnamespace=0'
    r = json.loads(requests.get(endpoint + params).text)
    
    results = r['query']['pages']

    return next(iter(results))


def get_article(id):

    params = '?action=query&prop=extracts&exintro&format=json&pageids=' + id
    r = json.loads(requests.get(endpoint + params).text)

    return next(iter(r['query']['pages'].values()))['extract']


def remove_tags(text, tags):

    for tag in tags:
        text = text.replace('<{}>'.format(tag), '')
        text = text.replace('</{}>'.format(tag), '')

    return text


def remove_spans(text):
    regex = u'(\<span.*\<\/span\>)'
    matches = re.findall(regex, text)
    for match in matches:
        text = text.replace(match, '')

    return text


def clean_up_text(text):

    text = remove_tags(text, ['b', 'p', 'i', 'ul', 'li', 'br'])
    text = remove_spans(text)

    return text.strip()


def get_sentences(text, num):
    sentences = text.split('. ')
    if len(sentences) <= num:
        return text
    else:
        s = ''
        for i in range(0, num):
            s += sentences[i] + '. '
        return s.strip()


def get_random_summary():

    id = get_random_article()
    text = get_article(id)
    text = clean_up_text(text)
    text = get_sentences(text, 2)

    return text