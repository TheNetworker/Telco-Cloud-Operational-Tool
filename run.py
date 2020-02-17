from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
import json
import sys
import os
import re
import emoji


style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


def questionsList():
    questions = [
        {
            'type': 'input',
            'name': 'RC',
            'message': emoji.emojize('OpenStack RC path file: '),
        },
        {
            'type': 'list',
            'message': 'select item',
            'name': 'tasks',
            'choices': [
                Separator('<<>><<>> Cloud Menu (OpenStack) <<>><<>>'),
                {
                    'name': 'Director Health-check + status'
                },
                {
                    'name': 'Openstack services status'
                },
                {
                    'name': 'Ceph Storage status'
                },
                {
                    'name': 'Controllers status'
                },
                {
                    'name': 'Check OpenStack Host Aggregate (HA)'
                },
                {
                    'name': 'Computes status'
                },
                {
                    'name': 'VM\'s Status'
                },
                {
                    'name': 'Check for Errors per OpenStack Service'
                },
                {
                    'name': 'Check Baremetal List and status'
                },
                {
                    'name': 'Show Servers List'
                },
                {
                    'name': 'Show Projects List'
                },
                {
                    'name': 'Show Users List'
                },
                {
                    'name': 'Show Networks List'
                },
                {
                    'name': 'Show Volumes List'
                },
                {
                    'name': 'Show Images List'
                },
                {
                    'name': 'Not Listed'
                },
                Separator('<<>><<>> SOSREPORT (RHEL/Centos)<<>><<>>'),
                {
                    'name': 'sosreport',
                    # 'disabled': 'Administrator Only'
                    # 'checked': True
                },
                Separator('<<>><<>> Customized Requests <<>><<>>'),
                {
                    'name': 'PMR',
                    'disabled': 'NFVI Team BO Only',
                    'checked': True
                },
                Separator('<<>><<>> OS Menu (RHEL/Centos)<<>><<>>'),
                {
                    'name': 'Disk status'
                },
                {
                    'name': 'Memory status'
                },
                {
                    'name': 'CPU status'
                },
                {
                    'name': 'Check Capabilities of OS'
                },
                {
                    'name': 'Check for Hardware Errors'
                },
                {
                    'name': 'Check Hardware Information'
                },
                {
                    'name': 'heck Service status'
                },
                {
                    'name': 'Check Neighbors reachability'
                },
                {
                    'name': 'Check grub parameter'
                },
                {
                    'name': 'NUMA Status'
                },
                {
                    'name': 'Number of running VM (KVM)'
                },
                {
                    'name': 'Number of virtual interfaces (VIF)'
                },
                {
                    'name': 'Check SRIOV status'
                },
                {
                    'name': 'Other Not Listed'
                },

            ],
            'validate': lambda answer: 'You must choose at least one item.' \
            if len(answer) == 0 else True
        }
    ]
    return questions


def healthCheck():
    print('run ansible health check ....')

def runCommand(cmd):
    os.system(cmd)

def selection():
    answers = prompt(questionsList(), style=style)
    if answers['tasks'] == 'Not Listed':
        cmd = input("Type your command here: ")
        runCommand(cmd)
    if len(answers['RC']) > 0:
        cmd = ('source ' + answers['RC'])
        runCommand(cmd)
    if len(answers['RC']) == 0:
        print('Please Insert the RC full path and try again!')
        #print(answers['RC'])


    else:
        print('The selected Task/Tasks Not available at this time.')

selection()



