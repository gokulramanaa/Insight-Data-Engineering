class ParseInput():
    def __init__(self, file):
        self.filename = file
        self.occupations, self.states,self.certified_count = {},{},0
        self.sep = ';'
        self.content = None
        self.status_ind, self.socname_ind, self.state_ind = None, None, None
        
    def readfile(self):
        with open(self.filename, encoding="utf8") as f:
            s = f.read()
        self.content = s.split("\n")
       
    def headerIndex(self):
        for i,j in enumerate(self.content[0].split(';')):
            if j == "CASE_STATUS":
                self.status_ind = i
            if j == "SOC_NAME":
                self.socname_ind = i
            if j == "EMPLOYER_STATE":
                self.state_ind = i
    
    def parseRow(self, line):
        if line == "":
            return None
        fields = line.split(self.sep)
        status = fields[self.status_ind].strip()
        status = status.upper()
        occupation = fields[self.socname_ind].strip()
        occupation = occupation.upper()
        state = fields[self.state_ind].strip()
        state = state.upper()

        if status == 'CERTIFIED':
            if occupation in self.occupations:
                tmpsoc = self.occupations[occupation]
                tmpsoc +=1
                self.occupations[occupation] = tmpsoc
            else:
                self.occupations[occupation] = 1 
            if state in self.states:
                tmpsoc = self.states[state]
                tmpsoc +=1
                self.states[state] = tmpsoc
            else:
                self.states[state] = 1 
            self.certified_count +=1
            
    def getData(self):
        self.readfile()
        self.headerIndex()
        list(map(self.parseRow,self.content))
        return  self.certified_count, self.occupations, self.states