# Base files required:
    # package folder
        # --> __init__.py (file)
        
        

# Portability for package file structure:
    
    # Package Folder
        # --> __init__.py (file)
    # requirements.txt
    # setup.py
    
    
# Requirements.txt file syntaxx
    matplotlib
    numpy==1.15.4 
    pycodestyle>=2.4.0
    

# setup.py file syntax
    from setuptools import setup
    
    setup(name="my_package",
          version="0.0.1",
          description="An example package",
          author="Matt Femia"
          author_email="blah
          packages=["my_package"],   #where are the init files
          intall_requires=["matplotlib",
                           "numpy==1.15.4",
                           "pycodestyle>=2.4.0"])

# "pip install -r requirements.txt" from its parent directory

# "pip install ." from inside directory will install package








#1 Class example

# Define Document class **** working in document.py ****
class Document:
    """A class for text analysis
    
    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """
    # Method to create a new instance of MyClass
    def __init__(self, text):
        # Store text parameter to the text attribute
        self.text = text
        
        
# to import this into other python file in same directory:
        # from .document import Document
        
        
# Non-Public methods
    _method