from setuptools import setup

setup(
    name='img2html',
    version='0.0.1',
    author='ZQPei',
    author_email='peiziqiang@gmail.com',
    packages=['img2html'],
    # scripts=['utils/build_server_scripts'],
    entry_points = {
              'console_scripts': [
                  'build_server = img2html:img2html',
              ],              
          },
    url='https://github.com/ZQPei/Huster',
    description='Display images with html file.',
    long_description=open('./README.md', 'r').read(), 
    long_description_content_type="text/markdown",
    platforms=["all"],
    license='MIT',
)