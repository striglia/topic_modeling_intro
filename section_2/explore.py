"""
A starter script for exploring the types of words individual businesses use.
"""
import gzip
import json
import os
import string


def main():
    project_root_directory = os.path.join(os.path.dirname(__file__), '../')
    data_file = os.path.join(project_root_directory, 'sample_data.json.gz')
    print 'The data file path is {0}'.format(data_file)

    business_reviews = read_data_file(data_file)
    sample_business = business_reviews[0]

    # Let's look at the first business just to get an idea of what we're
    # working with...
    print sample_business['reviews'][0]
    print sample_business['categories']
    print 'Reviews summary:'
    print interesting_words(sample_business['reviews'])


def interesting_words(reviews):
    # TODO: Make me better!
    # ...this isn't a very useful definition of "interesting"
    return reviews[0].split()[:5]


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


def clean_biz(biz):
    """Clean up a business's text data so we can do further processing."""
    return {
        'name': biz['name'],
        'id': biz['business_id'],
        'categories': biz['categories'],
        'reviews': [clean_review(r) for r in biz['reviews']],
    }


def read_data_file(data_file):
    """Take a filepath and load the business review data."""
    with gzip.open(data_file, 'r') as input_file:
        data = [json.loads(line) for line in input_file]

    # For each business, do basic data cleanup.
    return [clean_biz(biz) for biz in data]


if __name__ == '__main__':
    """This gets called when we run this script!"""
    main()
