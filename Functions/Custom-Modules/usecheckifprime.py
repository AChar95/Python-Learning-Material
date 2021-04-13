import prime
 
answer = prime.checkIfPrime(13)
print(answer)

'''
If the imported python script (in this case prime.py) is in a separate folder
Then follow should be added at the top of the script
import sys
if '<path to modules folder>' not in sys.path:
    sys.path.append('<path to modules folder>')
'''