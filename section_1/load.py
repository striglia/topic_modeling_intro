"""
A module which loads our business reviews from file.
"""
import os


def load_data():
    project_root_directory = os.path.join(os.path.dirname(__file__), '../')
    data_file = os.path.join(project_root_directory, 'sample_data.json.gz')
    print 'The data file path is {0}'.format(data_file)

    return read_data_file(data_file)


def read_data_file(data_file):
    """Take a filepath and load the business review data."""
    # FIXME! This code doesn't load the data at all! We want to make sure we
    # load the business data from our file and also run each business through
    # the clean_biz_data function.
    return [{
        'reviews': ['foo'],
        'categories': ['Restaurants', 'Breakfast/Brunch'],
        'name': "Scott's Hot Dog Shack",
    }]


def clean_biz_data(biz):
    """Clean up a business's text data so we can do further processing."""
    # TODO: how do we want to store a business's information? We will
    # definitely care about the following fields:
    #   name
    #   id
    #   categories
    #   reviews
    #
    # What data structure is best?
    return {}
