"""
A module which loads our business reviews from file.
"""
import gzip
import json
import os
import string


def load_data():
    project_root_directory = os.path.join(os.path.dirname(__file__), '../')
    data_file = os.path.join(project_root_directory, 'sample_data.json.gz')
    print 'The data file path is {0}'.format(data_file)

    return read_data_file(data_file)


def read_data_file(data_file):
    """Take a filepath and load the business review data."""
    with gzip.open(data_file, 'r') as input_file:
        data = [json.loads(line) for line in input_file]

    # For each business, do basic data cleanup.
    return [clean_biz_data(biz) for biz in data]


def clean_review(review):
    """Removes simple stopwords, lowercases, fixes punctuation."""
    review = review.lower()
    # Remove punctuation!
    review = ''.join(c for c in review.strip() if c not in string.punctuation)
    # Remove stopwords!
    stopwords = set(['and', 'or', 'but', 'the', 'a', 'an', 'is', 'not', 'in',
        'by'])
    return ' '.join(
        word
        for word in review.split()
        if word not in stopwords
    )


def clean_biz_data(biz):
    """Clean up a business's text data so we can do further processing."""
    return {
        'name': biz['name'],
        'id': biz['business_id'],
        'categories': biz['categories'],
        'reviews': [clean_review(r) for r in biz['reviews']],
    }
