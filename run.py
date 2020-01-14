#!/usr/local/bin/python3.7

from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint


style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


questions = [
    {
        'type': 'checkbox',
        'message': 'Usage:',
        'name': 'action',
        'choices': [
            Separator('= Health Check ='),
            {
                'name': 'Undercloud'
            },
            {
                'name': 'Overcloud'
            },
            {
                'name': 'Ceph Storage'
            },
            Separator('= Collect Logs ='),
            {
                'name': 'sosreport',
                'disabled': 'Administrator Only'
                # 'checked': True
            },
            Separator('= Nodes Information ='),
            {
                'name': 'Baremetal Node list'
            },
            {
                'name': 'Overcloud Node list'
            },
            {
                'name': 'List of VM\'s per Node'
            },
            {
                'name': 'List of VM\'s with their respective NUMA'
            },
            {
                'name': 'List of VM\'s with their vCPU'
            },
            {
                'name': 'List of VM\'s with their vNIC'
            },
            {
                'name': 'List of VM\'s with their RAMs info'
            }

        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

answers = prompt(questions, style=style)
pprint(answers)
