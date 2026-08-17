# Notes
#### 17/08

- There's a rate limit of 100 requests per day, so each time we run the test code, it becomes 20 requests per run.
- Solutions:
    - Save API responses that were already retrieved to a json file
    - Insted of retrieving every single competition, let's aim to pick out the main ones that we want.