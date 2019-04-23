''' Python Script to run Ansible Playbook, providing a key word to
execute the Playbook on - Project LLDP Mermaid App '''

# Import argv to provide an argument in python script
from sys import argv
# Using "subprocess" to run commands (i.e. "ansible-playbook nameofplay.yml")
import subprocess

# Variable to use throughout script
net_grp = argv
p = subprocess

# Testing via Ansible ad-hoc command:
play_output = p.call(["ansible", "td-juniper", "-m", "ping"])



# Prettify Ansible Playbook output (in JSON)
# and convert to Python Lists/Dictionary
# Guide: https://www.w3schools.com/python/python_json.asp
play_clean_json = ''
