def defineAList():
    local_list = ['1', '2', '3']
    print "For checking purposes: in defineAList, list is", local_list
    return local_list


def useTheList(passed_list):
    print "For checking purposes: in useTheList, list is", passed_list


def main():
    useTheList(defineAList())

main()
