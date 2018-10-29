## Repo directory structure
```
      ├── README.md 
      ├── run.sh
      ├── src
      │   └──h1b_counting.py
      │   └──ParseInput.py
      │   └──Top10list.py
      ├── input
      │   └──h1b_input.csv
      ├── output
      |   └── top_10_occupations.txt
      |   └── top_10_states.txt
      ├── insight_testsuite
          └── run_tests.sh
          └── tests
              └── test_1
                 ├── input
                 │   └── h1b_input.csv
                 |__ output
                    └── top_10_occupations.txt
                    └── top_10_states.txt
```
### Running the Script

*python ./src/h1b_counting.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt*

We can trigger the python script by running ./run.sh shell script which passes the necessary main python script location(./src/h1b_counting.py), input(./input/h1b_input.csv) and output(./output/*) folders paths as arugments. 

### Libraries Imported
**sys:** To parse the command line system arguments, imported sys library

### Algorithm 
1. Read the raw content of the input csv and stored as string variable. Split the string variable as row by row by new line char ('\n').
2. Since each line has to be parsed and extracted specific set of fields, instead of for loop, I used map function which does the feature extraction faster than plain for loop 
3. Once features are extracted appropriate top 10 list are calculated by sorting the features
4. Wrote the top 10 list to appropriate output files.
