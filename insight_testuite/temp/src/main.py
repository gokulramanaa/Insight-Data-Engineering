from ParseInput import ParseInput
from Top10list import Top10list
import sys
    
def main():
    #print(sys.argv)
    #try:
    #    filename, separator = sys.argv[1],';'
    #except:
    #    print("Please give the valid input file name from input folder")
    #    return 
    separator = ';' 
    inputfile, outputoccupation, outputstate = sys.argv[1],sys.argv[2],sys.argv[3]
    InputHolder = ParseInput(inputfile, separator)
    certified_count,occupation_dict, states_dict = InputHolder.getData()
    Toppers = Top10list(certified_count,occupation_dict, states_dict,separator, outputstate,outputoccupation)
    Toppers.top10Occupation()
    Toppers.top10State()

if __name__ == "__main__":
    main()