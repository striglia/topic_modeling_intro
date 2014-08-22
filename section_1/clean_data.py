"""
A starter script for reading our Yelp data and cleaning up the reviews.
"""
import os


def main():
    project_root_directory = os.path.join(__file__, '../')
    data_file = os.path.join(project_root_directory, 'sample_data.json.gz')
    print 'The data file path is {0}'.format(data_file)

    business_reviews = read_data_file(data_file)
    sample_business = business_reviews[0]

    # Let's look at the first business just to get an idea of what we're
    # working with...
    print sample_business['reviews'][0]
    print sample_business['categories']
    print sample_business['name']


def read_data_file(data_file):
    """Take a filepath and load the business review data."""
    # FIXME!
    return [{
        'reviews': ['foo'],
        'categories': ['Restaurants', 'Breakfast/Brunch'],
        'name': "Scott's Waffle House",
    }]


if __name__ == '__main__':
    """This gets called when we run this script!"""
    main()
