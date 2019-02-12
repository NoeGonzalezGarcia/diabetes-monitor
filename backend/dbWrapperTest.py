from backend.dbWrapper import *
import json


def main():
    wrapper = dbWrapper("root", "Kreme1_%")
    wrapper.add_patient(0, "I live horribly", 1, "admin", "1234", "Joe", "R", "Smith")
    date = datetime.date(1987, 5, 21)
    datestr = date.strftime("%Y-%m-%d")
    wrapper.add_smbg_data("admin", datestr, "breakfast", 25, 83, 1500)
    print(wrapper.get_smbg_data("admin", datestr, "breakfast"))


if __name__ == '__main__':
    main()
