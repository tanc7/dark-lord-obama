from termcolor import colored
import os
import socket
import sys
import operator


def save_solution(save_name, solution):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    document_name = '/root/Documents/wmv_to_mp4_converter/Chapter_14_15/solutions/%s_%s.csv' % (save_name, timestr)
    w = open(document_name,'a+')
    w.write(solution + '\n')
    string = "Your solution is saved as: %s" % document_name
    print yellow(string)
    w.close()
    return
    # timestr = time.strftime("%Y%m%d-%H%M%S")

def red(string):
    string = colored(string,'red',attrs=['bold'])

    return string
def green(string):
    string = colored(string,'green',attrs=['bold'])

    return string
def yellow(string):
    string = colored(string,'yellow',attrs=['bold'])

    return string
def cyan(string):
    string = colored(string,'cyan',attrs=['bold'])

    return string

def go_back_main_menu_module():
    os.system('python /root/Documents/wmv_to_mp4_converter/main.py')
    return
    # timestr = time.strftime("%Y%m%d-%H%M%S")
    return

def open_in_new_window(command):
    command = str(command)
    cmd_str = "gnome-terminal -e 'bash -c \"{0}; exec bash\"'".format(
        command
    )
    os.system(cmd_str)
    # os.system("gnome-terminal -e 'bash -c \"{0}; exec bash\"'").format(
    #     command
    # )
    return

def video_converter(wordlist):
    import socket
    import StringIO
    import operator
    import os
    import sys
    sys.path.append("/root/Documents/wmv_to_mp4_converter")
    import toolkits
    # 1:

    list_of_strings = "{0}".format(
        str(wordlist)
    )
    r = open(list_of_strings,'r')
    # line = r.readline()
    row_number = 1

    r = open(list_of_strings,'a+')
    with open(list_of_strings,'a+') as r:
        line = r.readline()
        sentence = str(line.strip())
        row_number = 1
        for sentence in r:
            if sentence != "":
                try:
                    
                    sentence = sentence.replace('(','\(').replace(')','\)')
                    converted_filename = sentence.replace('.wmv','.mp4')
                    # converted_filename = """{0}.mp4
                    # """.format(str(sentence))
                    cmd_str = "ffmpeg -i {0} {1}".format(
                        str(sentence.strip()),
                        str(converted_filename.strip())
                    )
                    # cmd_str_one = "ffmpeg -i {0}".format(str(sentence))
                    # cmd_str_two = " {0}".format(str(converted_filename))
                    # cmd_str = cmd_str_one + cmd_str_two
                    print yellow(cmd_str)
                    os.system(cmd_str)
                except:
                    print yellow("All files converted")

def list_writer(wordlist):
    def open_all_lists():
        os.chdir('/root/Desktop') # Changes directory to where the generated lists are created

        open_in_new_window('leafpad elif_list')
        open_in_new_window('leafpad dictionary_scripts')
        open_in_new_window('leafpad defined_functions')
        open_in_new_window('leafpad UI_list')
        return
    import socket
    import StringIO
    import operator
    import os
    import sys
    sys.path.append("/root/Documents/wmv_to_mp4_converter")
    import toolkits
    # 1:

    list_of_strings = "{0}".format(
        str(wordlist)
    )
    os.chdir("/root/Desktop")
    os.system("echo '' > UI_list")
    os.system("echo '' > elif_list")
    os.system("echo '' > defined_functions")
    os.system("echo '' > dictionary_scripts")
    r = open(list_of_strings,'r')
    # line = r.readline()
    row_number = 1

    r = open(list_of_strings,'a+')
    with open(list_of_strings,'a+') as r:
        line = r.readline()
        sentence = str(line)
        row_number = 1
        for sentence in r:
            if sentence != "":
                row_string = """# {0}: """.format(
                    str(row_number)
                )
                sentence = sentence.replace("./",'')
                sentence = sentence.strip()
                ui_sentence = row_string + sentence

                w = open("./UI_list","a+")
                w.write(ui_sentence + '\n')
                w.close()

                row_string = """elif opt_choice == {0}: """.format(
                    str(row_number)
                )

                elif_sentence = row_string + '\n'
                function_string = sentence + "()"
                function_string = "\t" + function_string + "\n"
                w = open("./elif_list","a+")
                w.write(elif_sentence)
                w.write(function_string)
                w.close()

                function_define_string = "def " + sentence + "():\n"
                return_string = "\treturn\n"
                w = open("./defined_functions","a+")
                w.write(function_define_string)
                w.write(return_string)
                w.close()

                dictionary_scripts = """{0}: "{1}",""".format(
                    str(row_number),
                    sentence
                )
                dictionary_scripts = dictionary_scripts + '\n'
                w = open("./dictionary_scripts","a+")
                w.write(dictionary_scripts)
                w.close()

                row_number = row_number + 1


    open_all_lists()

    def write_elif_list():
        os.chdir("/root/Desktop")


        r = open(list_of_strings,'r+b')
        read_r = r.read()
        buf = StringIO.StringIO(read_r)
        row_number = 1

        while True:
            line = buf.readlines().strip()
            if line != '':
                row_string = """elif opt_choice == {0}: """.format(
                    str(row_number)
                )
                sentence = sentence.replace("./",'').replace(".nse",'')
                sentence = row_string + sentence
                row_number = row_number + 1


                w = open("./elif_list","a+")
                w.write(sentence + '\n')
                w.close()


            else:
                print "WRITING COMPLETE"
                # exit(0)
        open_all_lists()
        return

    def main():
        write_UI_list()
        return

    return
