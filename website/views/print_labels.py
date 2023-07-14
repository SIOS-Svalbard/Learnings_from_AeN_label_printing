from flask import Blueprint, render_template, flash, request
from website import CONFIG

print_labels = Blueprint('print_labels', __name__)

@print_labels.route('/print_medium_labels', methods=['GET', 'POST'])
def print_medium_labels():

    size = 'medium'
    ribbon = 'Zebra 5095, 84 mm'
    labels = 'CILS Eppendorf, 81000TN'
    ip = CONFIG['medium_label_printer']['ip']

    increment3 = False
    increment4 = False
    number_labels = 1

    text = {
        1: { # Line 1
            'max_number_of_characters': 18,
            'content': ''
        },
        2: { # Line 2
            'max_number_of_characters': 18,
            'content': ''
        },
        3: { # Line 3
            'max_number_of_characters': 18,
            'content': ''
        },
        4: { # Line 4
            'max_number_of_characters': 18,
            'content': ''
        }
    }

    if request.method == "POST":

        (
            number_labels,
            ip,
            text,
            increment3,
            increment4,
        ) = get_values_from_form(text)


    return render_template(
    "/print_labels.html",
    size=size,
    ribbon=ribbon,
    labels=labels,
    ip=ip,
    text=text,
    increment3=increment3,
    increment4=increment4,
    number_labels=number_labels
    )

@print_labels.route('/print_large_labels', methods=['GET', 'POST'])
def print_large_labels():

    size = 'large'
    ribbon = 'BRADY R-6400, 65 mm'
    labels = 'BRADY 48.26 × 25.4 mm ,THT-156-492-1.5-SC'
    ip = CONFIG['large_label_printer']['ip']

    increment3 = False
    increment4 = False
    number_labels = 1

    text = {
        1: { # Line 1
            'max_number_of_characters': 20,
            'content': ''
        },
        2: { # Line 2
            'max_number_of_characters': 20,
            'content': ''
        },
        3: { # Line 3
            'max_number_of_characters': 20,
            'content': ''
        },
        4: { # Line 4
            'max_number_of_characters': 26,
            'content': ''
        },
        5: { # Line 5
            'max_number_of_characters': 26,
            'content': ''
        }
    }

    if request.method == "POST":

        (
            number_labels,
            ip,
            text,
            increment3,
            increment4,
        ) = get_values_from_form(text)

    return render_template(
    "/print_labels.html",
    size=size,
    ribbon=ribbon,
    labels=labels,
    ip=ip,
    text=text,
    increment3=increment3,
    increment4=increment4,
    number_labels=number_labels
    )

def get_values_from_form(text):
    '''
    Retrieve values from form.
    These values are preserved after the user hits print.
    '''
    form_input = request.form.to_dict(flat=False)
    number_labels = form_input['number_labels'][0]
    ip = form_input['ip'][0]
    for line, criteria in text.items():
        text[line]['content'] = form_input[f'line{line}'][0]
    if 'increment3' in form_input and form_input['increment3'] == ['on']:
        increment3 = True
    else:
        increment3 = False
    if 'increment4' in form_input and form_input['increment4'] == ['on']:
        increment4 = True
    else:
        increment4 = False
    return number_labels, ip, text, increment3, increment4
