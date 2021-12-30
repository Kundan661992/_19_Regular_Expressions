"""

                               Regular Expressions

If we want to represent a group of Strings according to a particular format/pattern then we should go for
Regular Expressions.


i.e RE is a declarative mechanism to represent a group of Strings accroding to particular format/pattern.


Eg 1: We can write a regular expression to represent all mobile numbers
Eg 2: We can write a regular expression to represent all mail ids.
Eg 3: we can write a regular expression for serching or for finding.


The main important application areas of RE are
 1. To develop validation frameworks/validation logic
 2. To develop Pattern matching applications (ctrl-f in windows, grep in UNIX etc)
 3. To develop Translators like compilers, interpreters etc
 4. To develop digital circuits
 5. To develop communication protocols like TCP/IP, UDP etc.
We can develop Regular Expression Based applications by using python module: re
This module contains several inbuilt functions to use Regular Expressions very easily in our
applications


1. compile()
re module contains compile() function to compile a pattern into RegexObject.

"""
import re
pattern = re.compile("ab")
print(pattern)

"""
2. finditer():
Returns an Iterator object which yields Match object for every Match

"""
matcher = pattern.finditer("abaababa")
print(matcher)

"""
On Match object we can call the following methods.
1. start() --> Returns start index of the match
2. end() --> Returns end+1 index of the match
3. group() --> Returns the matched string
"""

# Eg:
import re
count = 0
pattern = re.compile('ab')
matcher = pattern.finditer('abaababa')
for match in matcher:
    count += 1
print(match.start(), '...', match.end(), '...', match.group())
print('The number of occurrences: ', count)


# Note: We can pass pattern directly as argument to finditer() function.
# Eg:
import re
count=0
matcher=re.finditer('ab','abaababa')
for match in matcher:
    count+=1
print(match.start(),'......',match.end(),'.....',match.group())
print('The number of occurrences: ',count)


"""
Character classes:
We can use character classes to search a group of characters
1. [abc] --> Either a or b or c
2. [^abc] -->Except a and b and c
3. [a-z]-->Any Lower case alphabet symbol
4. [A-Z]-->Any upper case alphabet symbol
5. [a-zA-Z]-->Any alphabet symbol
6. [0-9] Any digit from 0 to 9
7. [a-zA-Z0-9]-->Any alphanumeric character
8. [^a-zA-Z0-9]-->Except alphanumeric characters(Special Characters)

"""

# Eg:
import re
matcher=re.finditer('x','a7b@k9z')
for match in matcher:
    print(match.start(),'.......',match.group())

"""
Pre defined Character classes:
\s --> Space character
\S--> Any character except space character
\d --> Any digit from 0 to 9
\D --> Any character except digit
\w--> Any word character [a-zA-Z0-9]
\W --> Any character except word character (Special Characters)
.--> Any character including special characters

    
"""

# Eg:
import re
matcher=re.finditer('x','a7b k@9z')
for match in matcher:
    print(match.start(),'......',match.group())

# Qunatifiers:We canuse quantifiers to specify the number of occurrences to match.
# a --> Exactly one 'a'
# a + --> Atleast one 'a'
# a * --> Any number of a's including zero number
# a? --> Atmost one 'a' ie either zero number or one number
# a{m} --> Exactly m number of a's
# a{m, n} --> Minimum m number of a's and Maximum n number of a's
# Eg:
import re
matcher=re.finditer('x','abaabaaab')
for match in matcher:
    print(match.start(),'.........',match.group())