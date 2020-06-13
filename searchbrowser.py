import googlesearch  #Command to install module: pip3 install google-search
import webbrowser #This is the part where I need your help.I need it to open the "finalans" in webbrowser using chrome driver.

class Gsearch_python:
   def __init__(self,name_search):
      self.name = name_search
   def Gsearch(self):
      count = 0
      try :
         from googlesearch import search
      except ImportError:
         print("No Module named 'google' Found")   #This error message is caused when you haven't imported google-search
      for i in search(query=self.name,tld='co.in',lang='en',num=10,stop=1,pause=2):    #You can change the language by editing lang='en'
         count += 1
         print (count)
         print(i + '\n')
if __name__=='__main__':
   suspect = input("Who do you want to track:")  #Custom message
   gs = Gsearch_python(suspect)
   finalans = (gs.Gsearch())  #It encodes the suspect string into a URL.Do not Panic if it looks stuck because it takes a few seconds to encode a URL.