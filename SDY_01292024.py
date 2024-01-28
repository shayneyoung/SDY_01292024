# db_program.py

#import os

class db_func:
    def __init__(self):
        self.data = {}
        self.txn = []

    def set_val(self, func, value):
        self.data[func] = value

    def get_val(self, func):
        return self.data.get(func, "NULL")

    def delete_val(self, func):
        if func in self.data:
            del self.data[func]

    def count_val(self, value):
        count = sum(1 for v in self.data.values() if v == value)
        return str(count)

    def begin_txn(self):
        self.txn.append(self.data.copy())
        #os.system('cls' if os.name == 'nt' else 'clear')
        #self.txn.clear()

    def rollback_txn(self):
        if not self.txn:
            print("TRANSACTION NOT FOUND.")
            return
        self.data = self.txn.pop()

    def commit_txn(self):
        if not self.txn:
            return
        #self.txn.commit()
        self.txn.clear()

def main():
    db = db_func()

    while True:
        try:
            stdin = input().split()
            if not stdin:
                continue

            if stdin[0].upper() == "SET":
                if len(stdin) != 3:
                    print("Invalid. Format: SET [func] [value]")
                else:
                    func, value = stdin[1], stdin[2]
                    db.set_val(func, value)
            elif stdin[0].upper() == "GET":
                if len(stdin) != 2:
                    print("Invalid. Format: GET [func]")
                else:
                    func = stdin[1]
                    result = db.get_val(func)
                    print(result)
            elif stdin[0].upper() == "DELETE":
                if len(stdin) != 2:
                    print("Invalid. Format:: DELETE [func]")
                else:
                    func = stdin[1]
                    db.delete_val(func)
            elif stdin[0].upper() == "COUNT":
                if len(stdin) != 2:
                    print("Invalid. Format: COUNT [value]")
                else:
                    value = stdin[1]
                    result = db.count_val(value)
                    print(result)
            elif stdin[0].upper() == "BEGIN":
                db.begin_txn()
            elif stdin[0].upper() == "ROLLBACK":
                db.rollback_txn()
            elif stdin[0].upper() == "COMMIT":
                db.commit_txn()
            elif stdin[0].upper() == "END":
                break
            else:
                print("Invalid. Please use: SET/GET/DELETE/COUNT/BEGIN/ROLLBACK/COMMIT/END")
        except EOFError:
            break

if __name__ == "__main__":
    main()
