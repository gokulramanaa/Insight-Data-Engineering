class Top10list():
    def __init__(self,count,occupations, states,sep,stateop,occop):
        self.certified_count = count
        self.states_dict = states
        self.occupation_dict = occupations
        self.sep = sep
        self.statesoutput = stateop
        self.occupationoutput = occop
        
    def top10Occupation(self):
        sorted_occ_tuple = sorted(self.occupation_dict.items(), key=lambda kv: (-kv[1],kv[0]))[:10]
        file = open(self.occupationoutput,'w')
        file.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE' + '\n')
        for each in sorted_occ_tuple:
            percentage =  (each[1]/self.certified_count) * 100
            file.write(str(each[0]) + self.sep + str(each[1]) + self.sep + str("%.1f" % percentage) + "%" + '\n')
        file.close()
        
    def top10State(self):
        sorted_state_tuple = sorted(self.states_dict.items(), key = lambda kv: (-kv[1],kv[0]))[:10]
        file = open(self.statesoutput,'w')
        file.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE' + '\n')
        for each in sorted_state_tuple:
            percentage =  (each[1]/self.certified_count) * 100
            file.write(str(each[0]) + self.sep + str(each[1]) + self.sep + str("%.1f" % percentage) + "%" + '\n')
        file.close()