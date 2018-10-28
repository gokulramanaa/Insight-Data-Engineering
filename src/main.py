
def parseInputFile():
    occupations, states = {},{}
    with open('../input/H1B_FY_2015.csv', encoding="utf8") as f:
        s = f.read()
    content = s.split("\n")
    
    for i,j in enumerate(content[0].split(';')):
        if j == "CASE_STATUS":
            status_ind = i
        if j == "SOC_CODE":
            socode_ind = i
        if j == "SOC_NAME":
            socname_ind = i
        if j == "EMPLOYER_STATE":
            state_ind = i
            
    def parseRow(line):
        global certified_count, sep
        if line == "":
            return None
        fields = line.split(sep)
        status = fields[status_ind].strip()
        status = status.upper()
        occupation = fields[socname_ind].strip()
        occupation = occupation.upper()
        state = fields[state_ind].strip()
        state = state.upper()

        if status == 'CERTIFIED':
            if occupation in occupations:
                tmpsoc = occupations[occupation]
                tmpsoc +=1
                occupations[occupation] = tmpsoc
            else:
                occupations[occupation] = 1 
            if state in states:
                tmpsoc = states[state]
                tmpsoc +=1
                states[state] = tmpsoc
            else:
                states[state] = 1 
            certified_count +=1
        
    list(map(parseRow,content))
    return  certified_count, occupations, states
    
def top10Occupation(certified_count, occupation_dict):
    global sep
    sorted_occ_tuple = sorted(occupation_dict.items(), key=lambda kv: kv[1], reverse=True)[:11]
    file = open('../output/top_10_occupations.txt','w')
    file.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE')
    for each in sorted_occ_tuple:
        percentage =  (each[1]/certified_count) * 100
        file.write('\n' + str(each[0]) + sep + str(each[1]) + sep + str("%.1f" % percentage) + "%")
    file.close()
    
def top10States(certified_count, states_dict):
    global sep
    sorted_state_tuple = sorted(states_dict.items(), key = lambda kv: kv[1], reverse=True)[:11]
    file = open('../output/top_10_states.txt','w')
    file.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE')
    for each in sorted_state_tuple:
        percentage =  (each[1]/certified_count) * 100
        file.write('\n' + str(each[0]) + sep + str(each[1]) + sep + str("%.1f" % percentage) + "%")
    file.close()
    
def main():
    global certified_count, sep
    certified_count = 0
    sep = ';'
    certified_count,occupation_dict, states_dict = parseInputFile()
    top10Occupation(certified_count, occupation_dict)
    top10States(certified_count, states_dict)

if __name__ == "__main__":
    main()