from backend.dbWrapper import *
import json


def main():
    wrapper = dbWrapper("root", "Kreme1_%")
    wrapper.add_patient(0, "I live horribly", 1, "admin", "1234", "Joe", "R", "Smith")
    id = wrapper.get_patient_info("admin")
    print(id)


if __name__ == '__main__':
    main()
