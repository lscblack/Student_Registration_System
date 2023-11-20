from connection import db, con
from prettytable import PrettyTable
import re


class Student:

    def __init__(self, choice):  # Constructor To  Catch Every Request and assign them
        self.choice = choice
        if self.choice == "1":
            self.register(self)
        elif self.choice == "2":
            self.view_student(self, "")
        elif self.choice == "3":
            self.delete_student(self)
        elif self.choice == "4":
            self.update_student(self)
        elif self.choice == "5":
            print("\033[34mThanks For\033[0m \033[31mUsing\033[0m\033[32m Our App\033[0m")
            con.close()
            exit()
        else:
            print("\033[36m\033[1m Enter Valid Choice \033[0m\033[0m \033[34m\031[1m(1-2): \033[0m\033[0m \n\n")
            main()

    @staticmethod  # Register New Student
    def register(self):
        # get data
        while True:
            fname = input("\033[34m\033[1mEnter First Name Here: \033[0m\033[0m")
            lname = input("\033[34m\033[1mEnter Second Name: \033[0m\033[0m")
            trade = input("\033[34m\033[1mEnter Combination: \033[0m\033[0m")
            level = input("\033[34m\033[1mEnter Level: \033[0m\033[0m")
            email = input("\033[34m\033[1mEnter Email: \033[0m\033[0m")
            if re.search(r"@.*\..*", email):
                data = (fname, lname, trade, level, email)
                sql = "INSERT INTO `student`(`fname`, `lname`, `trade`, `level`, `email`) VALUES (%s,%s,%s,%s,%s)"
                try:
                    db.execute(sql, data)
                    con.commit()
                    if db.rowcount > 0:
                        print("\033[32m Successfully Registered ! \033[0m")
                    else:
                        print("\033[31m Error : Failed To Register \033[0m")
                except Exception as e:
                    print("\033[31m Error: ", e, " \033[0m")
                    con.rollback()
                    raise
                finally:
                    pass
                self.view_student(self, "")
                break
            else:
                print("\033[31m Enter A Valid Email Format \033[0m")

    @staticmethod
    def view_student(self, normal):
        sql = "SELECT * FROM student"
        db.execute(sql)
        col = [head[0] for head in db.description]
        table = PrettyTable(col)
        rows = db.fetchall()
        if len(rows) > 0:
            for row in rows:
                table.add_row(row)
            print(table)
        else:
            print("\n\033[31m\033[1m *** No Data Found In The System *** \033[0m\033[0m\n")
        if normal == "":
            main()
        else:
            pass

    @staticmethod
    def delete_student(self):
        self.view_student(self, "From Delete")
        student_id = input("\033[36m\033[1m Enter Student Id To Delete:  \033[0m\033[0m")
        if student_id.isnumeric():
            sql = f"DELETE FROM `student` WHERE id = {student_id}"
            db.execute(sql)
            con.commit()
            try:
                if db.rowcount > 0:
                    print("\n\033[31m\033[1mStudent Deleted Successfully  \033[0m\n")
                    self.view_student(self, "From Delete")
                else:
                    print("\033[31m\033[1m Student Not Deleted Check Your id \033[0m\033[0m")
            except Exception as e:
                print("\033[31m\033[1m Error: ", e, " \033[0m\033[0m")
                con.rollback()
            finally:
                pass
            self.view_student(self, "")
        else:
            print("\033[31m\033[1mStudent Id Must Be Numbers\033[0m\033[0m")

    @staticmethod
    def update_student(self):
        self.view_student(self, "From Update")
        id = input("\033[36m\033[1m Enter Student Id To Update:  \033[0m\033[0m")
        if id.isnumeric():
            fname = input("\033[34m\033[1mEnter First Name Here: \033[0m\033[0m")
            lname = input("\033[34m\033[1mEnter Second Name: \033[0m\033[0m")
            trade = input("\033[34m\033[1mEnter Combination: \033[0m\033[0m")
            level = input("\033[34m\033[1mEnter Level: \033[0m\033[0m")
            email = input("\033[34m\033[1mEnter Email: \033[0m\033[0m")
            if re.search(r"@.*\..*", email):
                data = (fname, lname, trade, level, email)
                sql = f"UPDATE `student` SET `fname` = %s,`lname`= %s,`trade`= %s,`level`=%s,`email`= %s WHERE id={id}"
                try:
                    db.execute(sql, data)
                    con.commit()
                    if db.rowcount > 0:
                        print("\033[32m Successfully Updated ! \033[0m")
                    else:
                        print("\033[31m Error : Failed To Register \033[0m")
                except Exception as e:
                    print("\033[31m Error: ", e, " \033[0m")
                    con.rollback()
                    raise
                finally:
                    pass
                self.view_student(self, "")
        else:
            print("\033[31m\033[1mStudent Id Must Be Numbers\033[0m\033[0m")


def main():
    print("\033[32m\033[1m ** - Welcome To Student Registration System - ** \033[0m\033[0m")
    print("\033[31m\033[1m[1]\033[0m\033[0m \033[32m\033[1mRegister Student\033[0m\033[0m")
    print("\033[31m\033[1m[2]\033[0m\033[0m \033[32m\033[1mView All Students\033[0m\033[0m")
    print("\033[31m\033[1m[3]\033[0m\033[0m \033[32m\033[1mDelete Student\033[0m\033[0m")
    print("\033[31m\033[1m[4]\033[0m\033[0m \033[32m\033[1mUpdate Student\033[0m\033[0m")
    print("\033[31m\033[1m[5]\033[0m\033[0m \033[32m\033[1mExit\033[0m\033[0m")
    get_as = Student(input("\033[36m\033[1mEnter Choice : \033[0m\033[0m"))


main()
