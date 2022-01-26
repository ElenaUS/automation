from os.path import dirname, join, abspath
from setuptools import setup
from setuptools.command.install import install


setup_args = {
    'cmdclass': {'install': install},
    'name': 'selenium',
    'version': "4.1.0",
    'license': 'Apache 2.0',
    'description': 'Python bindings for Selenium',
    'long_description': open(join(abspath(dirname(__file__)), "README.rst")).read(),
    'url': 'https://github.com/SeleniumHQ/selenium/',
    'python_requires': '~=3.7',
    'classifiers': ['Development Status :: 5 - Production/Stable',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: Apache Software License',
                    'Operating System :: POSIX',
                    'Operating System :: Microsoft :: Windows',
                    'Operating System :: MacOS :: MacOS X',
                    'Topic :: Software Development :: Testing',
                    'Topic :: Software Development :: Libraries',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 3.7',
                    'Programming Language :: Python :: 3.8',
                    'Programming Language :: Python :: 3.9'],
    'package_dir': {
        'selenium': 'selenium',
        'selenium.common': 'selenium/common',
        'selenium.webdriver': 'selenium/webdriver',
    },
    'packages': ['selenium',
                 'selenium.common',
                 'selenium.webdriver',
                 'selenium.webdriver.chromium',
                 'selenium.webdriver.chrome',
                 'selenium.webdriver.common',
                 'selenium.webdriver.common.html5',
                 'selenium.webdriver.support',
                 'selenium.webdriver.firefox',
                 'selenium.webdriver.ie',
                 'selenium.webdriver.edge',
                 'selenium.webdriver.opera',
                 'selenium.webdriver.remote',
                 'selenium.webdriver.support', ],
    'include_package_data': True,
    'install_requires': ['urllib3[secure]', "trio", "trio-websocket"],
    'zip_safe': False
}

setup(**setup_args)