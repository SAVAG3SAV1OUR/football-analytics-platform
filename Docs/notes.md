# Notes
#### 17/08

- There's a rate limit of 100 requests per day, so each time we run the test code, it becomes 20 requests per run.
- Solutions:
    - Save API responses that were already retrieved to a json file
    - Insted of retrieving every single competition, let's aim to pick out the main ones that we want.
- Created a raw/ folder for the API responses
- Make the pipeline read from raw files when they already exist
- Logic:
Does raw file exist?
       │
   ┌───┴───┐
  YES      NO
   │        │
   ▼        ▼
Read file  API request
   │        │
   │        ▼
   │     Save raw file
   │        │
   └────┬───┘
        ▼
   Normalize
        ▼
   Processed data

- Built a cache/raw-file check
    - It checks if the json file exists in the folder
    - If it exists then it will read data from that json file, if not then it will collect raw data from the api and save it to a json file.


#### 25/08
- We could save the failed comps/seasons as json file that can be updated when something fails.
    - Then when the next pipeline runs, then we can start off with them before extracting the new data
- There may be a limitation in the API itself:
    - For the Premier League specifically, it seems like there's no data from 2015 going backwards