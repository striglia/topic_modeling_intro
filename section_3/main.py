"""
A script for loading our Yelp data and cleaning up the reviews.
"""
from load import load_data
from classify import naive_mexican_classifier


def main():
    business_reviews = load_data()

    # Find the first Mexican business
    for biz in business_reviews:
        if 'Mexican' in biz['categories']:
            sample_business = biz
            break

    # Let's see how we classify the first business...
    result = naive_mexican_classifier(sample_business['reviews'])
    print '\n'
    print 'First review: {0}'.format(sample_business['reviews'][0])
    print 'Categories: {0}'.format(sample_business['categories'])
    print '\nClassified as Mexican?: {0}'.format(result)


if __name__ == '__main__':
    """This gets called when we run this script!"""
    main()
