
import os
import threading

from problems.models import InputOutput
from codingcompetition.settings import UPLOAD_DESTINATION, TIME_LIMIT



def do_magic(file, user, problem_id):
    '''
        Does magic and returns the list of boolean
        for each test case as ``True`` or ``False``

        :param file: file name of the submission
        :param user: user object from request
        :param problem_id: id of the problem to test code against
        
    '''

    # Save file on server
    file_path = handle_file_upload(file,user, problem_id)

    # Compile the code
    executable_path = compile(file_path)

    # Get list of all test cases
    test_cases = get_all_testcases(problem_id)

    # For each test case create thread
    threads = []
    for test_case in test_cases:
        threads.append(threading.Thread(test_on_case, args=(executable_path, test_case)))


        


def handle_file_upload(file, user, problem_id):
    '''
        Saves the file and returns path to it
        file paht is as 
        ``UPLOAD_DESTINATION`` +``username``+``problem_id``+``file name``

        :param file: uploaded file
        :param user: user object from request
        :param problem_id: problem id for which solution file is uploaded for
    '''

    file_path = UPLOAD_DESTINATION+user.username+str(problem_id)

    with open(file_path, 'wb+') as f:
        for chunks in file.chunks():
            f.write(chunks)
    
    return file_path


def compile(file_path):
    '''
        Compiles the source code and forms same name output file.o
        returns compiled executable file path

        :param file_path: source code file path
    '''
    pass

def test_on_case(executable_path, input_output):
    '''
        executes the executable's path given and provides input to it
        returns final output

        :param executable_path: Path to executable
        :param input: Input ``string`` to be given to executable
    '''
    pass

def is_correct_output(actual_ouput, user_output):
    '''
        returns true if both match else false
    '''

    return actual_ouput == user_output


def get_all_testcases(problem_id):
    '''
        returns the list of test cases of the problem
    '''

    return InputOutput.objects.filter(problem_id = problem_id).all()

def get_output_file_path(input_file_path):
    '''
        Returns the file path, remove the extension of input file
        .cpp .c 
        and replace it with output executable file extension
        .o
    '''
    pass