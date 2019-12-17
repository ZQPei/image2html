from setuptools import setup

setup(
    name='image2html',
    version='0.0.1',
    author='ZQPei',
    author_email='peiziqiang@gmail.com',
    packages=['image2html'],
    install_requires=["huster"],
    # scripts=['utils/build_server_scripts'],
    entry_points = {
              'console_scripts': [
                  'image2html = image2html.image2html:image2html',
                  'make_flist = image2html.flist:make_flist',
              ],
          },
    url='https://github.com/ZQPei/image2html',
    description='Display images with html file.',
    # long_description=open('./README.md', 'r').read(), 
    # long_description_content_type="text/markdown",
    platforms=["all"],
    license='MIT',
)