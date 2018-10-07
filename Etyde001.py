import os
import sys

class Etyde:


def help(self):
      print "\n Usage: python etydes.py [seed] [-sphv]"
      print "       -s, --seed        Seed "
      print "       -p, --play        Play "  
      print "       -h, --help        This help "
      print "       -v, --verbose     Verbose"
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
      except getopt.GetoptError:
        print '\nSyntax Error'
        self.help()
      for index, opt in enumerate(args):
        if opt in ("-s", "--seed"):
          #something
        elif opt in ("-p", "--play"):
          self.no_marc = False
          MAKE = True
        elif opt in ("-h", "--help"):
          self.help()
        elif opt in ("-v", "--verbose"):
        elif index == 0:
          if ( args[0] == 'seed' ):
            print GREEN +  "\nRun all!!" + NC
            self.apps = 'all'
            self.test_all_apps = True
        else:
          assert False, "Wrong attribute"
          self.help()
      return None

  def initialize(self,argv):
    self.parseOnlineArgs(argv)
  def main(self,argv):
    self.initialize(argv)
    #test
  def __init__(self):
    self.configure = SafeConfigParser() #see self.autotest_ini file
    self.configure.read(self.autotest_ini)
    #paths
    self.output_path = self.configure.get('PATHS','SELF_PATH') 
    #test

  

if __name__ == "__main__":
  myclass = Etyde()
  myclass.main(sys.argv[1:])