from setuptools import setup

######################################################################################################
################ You May Remove All the Comments Once You Finish Modifying the Script ################
######################################################################################################

setup(

    name = 'markiyan-test-todo-cli', 
    

    version = '0.1.3',
    

    description = 'Global package for creating todo files',
    

    py_modules = ["test_todo"],
    

    package_dir = {'':'src'},
    

    author = 'MarkiyanPyts',
    author_email = 'markiyan.pyts@gmail.com',
    
    
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",
    
    
    url='https://github.com/MarkiyanPyts/python-click-cli',

    entry_points={
        'console_scripts': [
            'markiyan-test-todo-cli = test_todo:mycommands',
        ]
    },
    

    include_package_data=True,
    
    classifiers  = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: BSD License",
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Text Processing',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
    ],
    
    install_requires = [
        'click ~= 8.1.3',
    ],
    
    keywords = ['Todo', 'Test CLI']
    
)
