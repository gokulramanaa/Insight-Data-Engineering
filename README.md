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
              |   ├── input
              |   │   └── h1b_input.csv
              |   |__ output
              |   |   └── top_10_occupations.txt
              |   |   └── top_10_states.txt
```
### Running the Script

*python ./src/h1b_counting.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt*

We can trigger the python script by running ./run.sh shell script which passes the necessary main python script location(./src/h1b_counting.py), input(./input/h1b_input.csv) and output(./output/*) folders paths as arugments. 

### Libraries Imported
**sys:** To parse the command line system arguments, imported sys library

### Algorithm 
1. [Problem]
2. [Input Dataset]
3. [Instructions]
4. [Output]
