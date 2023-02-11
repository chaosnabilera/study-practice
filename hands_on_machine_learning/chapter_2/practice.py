import matplotlib.pyplot

import pandas
import sklearn
import sys

import urllib.request

from packaging import version

def check_version():
    print('sys.version_info: ', sys.version_info)
    print('sklearn.__version__: ', sklearn.__version__)
    assert sys.version_info >= (3, 7)
    assert version.parse(sklearn.__version__) >= version.parse("1.0.1")



if __name__ == '__main__':
    check_version()
    housing = load_housing_data()
    print(housing.head())
    print(housing.info())
    print(housing['ocean_proximity'].value_counts())
    print(housing.describe())
    
    # pandas.DataFrame.hist calls matplotlib.pyplot.hist
    # higher bins result in finer graph (more bin = more resolution)
    # 12 inch x 8 inch (x dpi)
    housing.hist(bins=200, figsize=(12, 8))

    matplotlib.pyplot.show()