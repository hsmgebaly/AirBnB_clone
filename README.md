# 0x00. AirBnB clone - The console

# This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

# Command interpreter:-
# It’s exactly the same of Shell but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

# Create a new object (ex: a new User or a new Place)
# Retrieve an object from a file, a database etc…
# Do operations on objects (count, compute stats, etc…)
# Update attributes of an object
# Destroy an object.

# Execution

Interactive mode

''' bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
'''

In non-interactive mode

'''bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
'''
