"""
A module which loads our business reviews from file.
"""
import os


def load_data():
    project_root_directory = os.path.join(__file__, '../')
    data_file = os.path.join(project_root_directory, 'sample_data.json.gz')
    print 'The data file path is {0}'.format(data_file)

    return read_data_file(data_file)


def read_data_file(data_file):
    """Take a filepath and load the business review data."""
    # FIXME!
    return [{
        'reviews': ['foo'],
        'categories': ['Restaurants', 'Breakfast/Brunch'],
        'name': "Scott's Waffle House",
    }]
