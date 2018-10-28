from ParseInput import ParseInput
    
def top10Occupation(certified_count, occupation_dict):
    global sep
    sorted_occ_tuple = sorted(occupation_dict.items(), key=lambda kv: (-kv[1],kv[0]))[:10]
    file = open('../output/top_10_occupations.txt','w')
    file.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE')
    for each in sorted_occ_tuple:
        percentage =  (each[1]/certified_count) * 100
        file.write('\n' + str(each[0]) + sep + str(each[1]) + sep + str("%.1f" % percentage) + "%")
    file.close()
    
def top10States(certified_count, states_dict):
    global sep
    sorted_state_tuple = sorted(states_dict.items(), key = lambda kv: (-kv[1],kv[0]))[:10]
    print(sorted_state_tuple)
    file = open('../output/top_10_states.txt','w')
    file.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE')
    for each in sorted_state_tuple:
        percentage =  (each[1]/certified_count) * 100
        file.write('\n' + str(each[0]) + sep + str(each[1]) + sep + str("%.1f" % percentage) + "%")
    file.close()
    
def main():
    global sep
    sep = ';'
    InputHolder = ParseInput('../input/H1B_FY_2015.csv')
    certified_count,occupation_dict, states_dict = InputHolder.getData() #parseInputFile()
    
    top10Occupation(certified_count, occupation_dict)
    top10States(certified_count, states_dict)

if __name__ == "__main__":
    main()