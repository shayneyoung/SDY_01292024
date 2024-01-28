# SDY_01292024

# Command-Line Program

This is command-line program that reads input from STDIN line by line and executes the database functions SET/GET/DELETE/COUNT/BEGIN/ROLLBACK/COMMIT/END

## How to Run

1. Open terminal. Navigate to your directory where you want to save the scripts.
Option1:
  Clone the repository inside the directory: 
    ```git clone https://github.com/shayneyoung/SDY_01292024```
Option2:
  Create a python file, and copy the code from SDY_01292024.py

2. Navigate to the path where you have clone the repository or manually created the python file:

    ```cd <path>```

4. Run the python script:

    ```python SDY_01292024.py```

5. Enter commands:

    - To set a value: `SET [name] [value]`
    - To get a value: `GET [name]`
    - To delete a value: `DELETE [name]`
    - To count values: `COUNT [value]`
    - To begin a transaction: `BEGIN`
    - To rollback a transaction: `ROLLBACK`
    - To commit transactions: `COMMIT`
    - To exit the database: `END`

    Example:

    ```plaintext
    SET foo bar
    GET foo
    DELETE foo
    COUNT bar
    ```

    Output:

    ```plaintext
    bar
    NULL
    0
    ```

## Notes

- All data is lost when the program terminates.
- FORMAT
  ```plaintext
  -`SET [name] [value]`
  -`GET [name]`
  -`DELETE [name]`
  -`COUNT [value]`
    ```
- Transactions can be started with `BEGIN`, rolled back with `ROLLBACK`, and committed with `COMMIT`.

- `END` to exit the program
