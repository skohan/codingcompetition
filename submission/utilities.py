from io import StringIO
import os
import threading
from concurrent.futures import ThreadPoolExecutor 
from subprocess import PIPE, Popen

from django.db import transaction

from problems.models import InputOutput
from codingcompetition.settings import UPLOAD_DESTINATION, TIME_LIMIT, COMPILE_DESTINATION


_COMPILER = "python3"
_COMPILER_FLAGS = ""


def do_magic(file, user, problem_id):
    '''
        Does magic and returns the list of boolean
        for each test case as ``True`` or ``False``

        :param file: file name of the submission
        :param user: user object from request
        :param problem_id: id of the problem to test code against
        
    '''

    # Save file on server
    file_path, output_path = handle_file_upload(file,user, problem_id)

    # Compile the code
    executable_path = compile(file_path, output_path)

    # print(executable_path)

    # Get list of all test cases
    test_cases = get_all_testcases(problem_id)

    # For each test case create thread
    # threads = []
    # for test_case in test_cases:
    #     # print(test_case.input_data, test_case.output_data)
    #     threads.append(threading.Thread(target=test_on_case, args=(executable_path, test_case,)))

    # for thread in threads:
    #     thread.start()

    # for thread in threads:
    #     thread.join()

    verdicts = []

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(test_on_case, executable_path, test_case ) for test_case in test_cases]
        verdicts = [ f.result() for f in futures]

    return verdicts

def handle_file_upload(file, user, problem_id):
    '''
        Saves the file and returns path to it
        file paht is as 
        ``UPLOAD_DESTINATION`` +``username``+``problem_id``+``file name``

        :returns ``file_path``: Uploaded file path
        :returns ``output_path``: For c compilers to produce ``.o`` file extention

        :param file: uploaded file
        :param user: user object from request
        :param problem_id: problem id for which solution file is uploaded for
    '''

    file_path = UPLOAD_DESTINATION+user.username+str(problem_id) +".py"
    output_path = get_output_file_path(user, problem_id)

    with open(file_path, 'wb+') as f:
        for chunks in file.chunks():
            f.write(chunks)
    
    return file_path, output_path


def compile(file_path, out):
    '''
        Compiles the source code and forms same name output file.o
        returns compiled executable file path

        :param file_path: source code file path
    '''
    # print("input file")
    # print(file_path)
    # os.system(
    #     command=_COMPILER + " " + _COMPILER_FLAGS +
    #     " " + file_path + " " + "-o" + " " + out,
    # ) 
    out = _COMPILER + " " + _COMPILER_FLAGS + " " + file_path
    
    return out

@transaction.atomic
def test_on_case(executable_command, test_cases):
    '''
            executes the command given and provides input to it
        returns final standard output

        :param executable_command: Command to execute
        :param input: Input ``string`` to be given to executable
    '''

    sp = Popen(executable_command.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    # sp.wait(1)
    # print(test_cases.input_data)
    # print(test_cases.output_data)
    verdict = True

    output_file = test_cases.output_data
    output_data = output_file.read()
    input_file = test_cases.input_data
    input_data = input_file.read()
    
    # sp.stdin(bytes(input_file.read(), 'utf-8'))
    # sp.stdin(bytes(input_data))
    try:
        std_out, std_error = sp.communicate(input=input_data, timeout=TIME_LIMIT)
        # print(std_out)
        # print(std_error)
    except Exception as e:
        print(e)

    # sleep(3)
    if is_correct_output(std_out, output_data):
        print("RIGHT!!!!!!!!!!!!!!!")
        verdict = True

    if std_error:
        verdict = False
        # print("there was a error", std_error)


    sp.kill()
    
    return (str(std_error.decode('utf-8')), verdict)



def is_correct_output(actual_ouput:bytes, user_output:bytes):
    '''
        returns true if both match else false
    '''

    ao = actual_ouput.decode('utf-8')
    uo = user_output.decode('utf-8')
    ao = ao.rstrip() # remove trailing whitespaces
    uo = uo.rstrip() # remove trailing whitespaces

    return ao == uo


def get_all_testcases(problem_id):
    '''
        returns the list of test cases of the problem
    '''

    return InputOutput.objects.filter(problem_id = problem_id).all()

def get_output_file_path(user, problem_id) -> str:
    '''
        Returns the file path, remove the extension of input file
        .cpp .c 
        and replace it with output executable file extension
        .o
    '''
    
    output_file =  COMPILE_DESTINATION + user.username + str(problem_id) + ".o"
    
    return output_file
