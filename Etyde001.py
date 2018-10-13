import os
import sys
import getopt
import configparser

#color constants
RED ="\033[0;31m"
GREEN ="\033[0;32m"
BLUE ="\033[0;34m"
YELLOW ="\033[1;33m"
NC ="\033[0m" #No color


class Etyde:  
  global AUX
  etydes_ini = 'etydes.ini'
  output_path = ''
  
  def help(self):
      print ("\n Usage: python etydes.py [seed] [-sphv]")
      print ("       -s, --seed        Seed ")
      print ("       -p, --play        Play ")  
      print ("       -h, --help        This help ")
      print ("       -v, --verbose     Verbose")
      sys.exit(2)
      return None
    
  def parseOnlineArgs(self, argv):
      
      #switches
      global MAKE #make autotest
      #show help if no arguments
      if len(sys.argv[1:]) == 0:
        self.help()

      #online arguments
    
      try:
        opt, args = getopt.getopt(sys.argv[1:],"-sphv",["seed="])
      except getopt.GetoptError as err:
        print ('\nErr Syntax Error')
        usage()
        self.help()
        sys.exit(2)
      for index, opt in enumerate(args):
        if opt in ("-s", "--seed"):
          #something
          MAKE=False
        elif opt in ("-p"):
          MAKE = True
        elif opt in ("-h", "--help"):
          self.help()
        elif opt in ("-v", "--verbose"):
          MAKE=True
        elif index == 0:
          if ( args[0] == 'seed' ):
            print (GREEN + "\nRun all!!" + NC)
            self.apps = 'all'
            self.test_all_apps = True
        else:
          assert False, "Wrong attribute"
          self.help()
      return None

  def initialize(self,aux):
    if aux:
      print ('AUX')
    
  def main(self,argv):
    global AUX
    self.parseOnlineArgs(argv)
    self.initialize(AUX)
    AUX = 'This is Museru'
    print (RED + AUX + NC)
    return None
    #test
  def __init__(self):
    global etydes_ini
    self.etydes_ini = 'etydes.ini'
    parser = configparser.ConfigParser() #see self.autotest_ini file
    #ini_file = parser.read( self.etydes_ini )
    ini_file = parser.read( './etydes.ini' )
    #paths
    #pathsis = ini_file['DEFAULT']
    self.output_path = parser.get('DEFAULT','SELF_PATH')
    #test

  

if __name__ == "__main__":
  myclass = Etyde()
  myclass.main(sys.argv[1:])