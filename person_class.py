import logging

name = "project"
logger = logging.getLogger("log in")
logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    format="'%(asctime)s - %(name)s - %(levelname)s - %(message)s' \n",
                    datefmt='%d-%b-%y %H:%M:%S')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('your name is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

class PersonClass():
  def __init__(self, name, family):
    self.name = name
    self.family = family
  
  def get_name(self):
    return self.name
  
  def get_family(self)
    return self.family
  
  def get_full_name(self)
    return self.name + " " + self.family
  
  def add_age(self, age):
    self.age = age
    
  def get_age(self):
    return self.age
  
