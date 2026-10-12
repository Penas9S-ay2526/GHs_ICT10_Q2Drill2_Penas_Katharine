# finding students
from pyscript import display, document


def name_finder(e):
    document.getElementById('result').innerHTML = ' '
    first_name = document.getElementById('name').value.title().strip() # first name input
    last_name = document.getElementById('surname').value.title().strip() # last name input
    full_name = first_name + ' ' + last_name # concatenating first and last name
    listed_candidates = ['Jaena Ambata', 'Adrianna Allas', 'Frances Torculas', 'Aldrich Samar', 'Antonio Soliman'] # list of candidates
    student_checker = full_name in listed_candidates # checking of student name

    display_message = (f'Sorry {full_name}, your name is not on the list.', f'Congratulations {full_name}! You are now part of the ICT club.') # message output


    display(display_message[student_checker], target='result') # display message