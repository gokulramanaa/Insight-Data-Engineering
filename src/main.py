
def parseInputFile():
    global certified_count
    occupations, states = dict(), dict()
    with open('../input/test.csv') as f: s = f.read()
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
            
    def parseRow():
        fields = line.split(sep)
        status = fields[status_ind].strip()
        status = status.upper()
        occupation = fields[socode_ind].strip()
        occupation = occupation.upper()
        state = fields[state_ind].strip()
        state = state.upper()

        if status == 'CERTIFIED':
            if occupations.has_key(occupation):
                tmpsoc = occupations[occupation]
                tmpsoc +=1
                occupations[occupation] = tmpsoc
            else:
                occupations[occupation] = 1 
            if states.has_key(state):
                tmpsoc = states[state]
                tmpsoc +=1
                states[state] = tmpsoc
            else:
                states[state] = 1 
            certified_count +=1
        
    list(map(opr,l[:5]))

    return  certified_count, occupation_dict, states_dict
    
def main():
    global certified_count
    certified_count = 0
    certified_count,occupation_dict, states_dict = parseInputFile()
    print(certified_count,occupation_dict, states_dict)

if __name__ == "__main__":
    main()