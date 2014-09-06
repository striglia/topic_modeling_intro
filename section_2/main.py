"""
A script for loading our Yelp data and cleaning up the reviews.
"""
from load import load_data
from explore import interesting_words


def main():
    business_reviews = load_data()
    sample_business = business_reviews[0]

    # Let's look at the first business just to get an idea of what we're
    # working with...
    print '\n'
    print 'First review: {0}'.format(sample_business['reviews'][0])
    print 'Categories: {0}'.format(sample_business['categories'])
    summary = interesting_words(sample_business['reviews'])
    print '\nReviews summary: {0}'.format(summary)


if __name__ == '__main__':
    """This gets called when we run this script!"""
    main()
