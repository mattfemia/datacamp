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
        
        
        
        
#2 Non-Public methods  "_method"
    
class Document:
  def __init__(self, text):
    self.text = text
    # Tokenize the document with non-public tokenize method
    self.tokens = self._tokenize()
    # Perform word count with non-public count_words method
    self.word_counts = self._count_words()

  def _tokenize(self):
    return tokenize(self.text)
	
  # non-public method to tally document's word counts with Counter
  def _count_words(self):
    return Counter(self.tokens)



#3 Class inheritance

# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)




#4 Creating a grandchild class with super()
        
# Define a Tweet class that inherits from SocialMedia
class Tweets(SocialMedia):
    def __init__(self, text):
        # Call parent's __init__ with super()
        super.__init__(SocialMedia)
        # Define retweets attribute with non-public method
        self.retweets = self._process_retweets()

    def _process_retweets(self):
        # Filter tweet text to only include retweets
        retweet_text = filter_lines(self.text, first_chars='RT')
        # Return retweet_text as a SocialMedia object
        return SocialMedia(retweet_text)

