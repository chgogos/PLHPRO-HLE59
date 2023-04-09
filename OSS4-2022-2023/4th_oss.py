# -*- coding: utf-8 -*-
"""4th OSS.ipynb


##Slide 12
"""

# Για την δημιουργία του αρχείου
f = open('myfile.txt','w')
l1 = "Hello World!.\n"
f.write(l1)
f.close()

f = open("myfile.txt", "r")
txt = f.read()

print(type(txt))
print(txt)



"""## Slide 13"""

# Για την δημιουργία του αρχείου
f = open("countries.txt", "w")
f.write("Greece : Athens\nGermany : Berlin\nItaly : Rome")
f.close()

f = open("countries.txt", "r")
txt = f.read()
dictionary = {}
for line in txt.split('\n'):
    c = line.split(':')
    dictionary[c[0]] = c[1]
f.close()

print(dictionary)

f = open("countries.txt", "r")
dictionary2 = {}
txt = f.readlines()
for line in txt:
    c = line.split(':')
    dictionary2[c[0]] = c[1]
f.close()

print(dictionary2)



"""##Slide 14"""

f = open("myfile.txt", "a")
f.write("\nNew line")
f.close()

f = open("myfile.txt", "r")
print(f.read())

f = open("myfile.txt", "w")
print(f.write("New Text!"))
f.close()

f = open("myfile.txt", "r")
print(f.read())



"""## Slide 15"""
with open("countries.txt") as f:
   txt = f.read()


"""## Slide 16"""
import os
os.remove("myfile.txt")

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")



"""##Slide 18"""

#Δημιουργία αρχείων
fa = open("countriesΑ.txt", "w")
fa.write("Greece:Athens\nGermany:Berlin\nItaly:Rome")
fa.close()
fb = open("countriesΒ.txt", "w")
fb.write("France:Paris\nGermany:Berlin\nItaly:Amsterdam")
fb.close()

def readFiles(fileA, fileB):
  fa = open(fileA , "r")
  fb = open(fileB , "r")

  txtA = fa.read()
  txtB = fb.read()
  dictionaryA = {}
  dictionaryB = {}

  for line in txtA.split('\n'):
    c = line.split(':')
    dictionaryA[c[0]] = c[1]

  for line in txtB.split('\n'):
    c = line.split(':')
    dictionaryB[c[0]] = c[1]    

  return dictionaryA, dictionaryB

def compDicts(first_dict, second_dict):
  value = {}
  for item in second_dict.items():
    if item[0] not in first_dict.keys():
      value[item] = 'Does not exist in the countriesA.txt file.'
    else:
       if item[1] != first_dict[item[0]]:
          value[item] = 'Wrong capital. The correct is:', first_dict[item[0]]
  return value


dictA, dictB = readFiles('countriesΑ.txt', 'countriesΒ.txt')
res = compDicts(dictA, dictB)
print(res)



"""## Slide 22"""

import pickle
f = open("myfile","wb")
pickle.dump(3.14, f)
pickle.dump([1,2,3], f)
f.close()

import pickle
f = open("myfile","rb")
x = pickle.load(f)
print(x, type(x))
y = pickle.load(f)
print(y, type(y))
f.close()




"""## Slide 23"""

import pickle
dictionary = {'Greece':'Athens',
              'Germany':'Berlin',
              'Italy':'Rome'}
f = open('countries','wb')
pickle.dump(dictionary, f)
f.close()

import pickle
f = open('countries','rb')
mydict = pickle.load(f)
print(mydict, type(mydict))

f.close()




"""##Slide 24"""

import pickle
f = open('countries','ab')
pickle.dump(3.4,f)
f.close()

import pickle
f = open('countries','rb')
mydict = pickle.load(f)
print(mydict, type(mydict))
x = pickle.load(f)
print(x, type(x))
f.close()

import os
os.remove('countries')



""" Slide 31 """

import sqlite3

conn = sqlite3.connect('test.db')
print(sqlite3.version)

import sqlite3
from sqlite3 import Error

def dbconnect(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn



"""## Slide 32"""

my_conn = dbconnect ('users_database.db')

sql_query = "CREATE TABLE users (id INTEGER PRIMARY KEY, username VARCHAR(128), password VARCHAR(128), name TEXT);"
c = my_conn.cursor()
c.execute(sql_query)

my_conn.close()




"""## Slide 33"""

my_conn = dbconnect ('users_database.db')

sql_query = "INSERT INTO users (id, username, password, name) VALUES ('1','kostas', 'pass123', 'Kώστας');"
c = my_conn.cursor()
c.execute(sql_query)

my_conn.commit()

my_conn.close()



"""##Slide 34"""

my_conn = dbconnect ('users_database.db')

sql_query = "SELECT * FROM users;"
c = my_conn.cursor()
result = c.execute(sql_query)
for rec in result.fetchall():
  print(rec)

my_conn.close()




"""##Slide 35"""

my_conn = dbconnect ('users_database.db')

sql_query = "SELECT username FROM users;"
c = my_conn.cursor()
records = c.execute(sql_query)
for rec in records.fetchall():
  print(rec)
my_conn.close()

my_conn = dbconnect ('users_database.db')

sql_query = "SELECT name FROM users WHERE id=2;"
c = my_conn.cursor()
records = c.execute(sql_query)
for rec in records.fetchall():
  print(rec)
my_conn.close()




"""## Slide36"""

my_conn = dbconnect ('users_database.db')

sql_query = "DELETE FROM users WHERE id='3';"
c = my_conn.cursor()
res = c.execute(sql_query)

my_conn.commit()

my_conn.close()




"""##Slide 37"""

my_conn = dbconnect ('users_database.db')

sql_query = "UPDATE users SET username = 'username_2x', password = 'password_2x' WHERE id='2';"
c = my_conn.cursor()
res = c.execute(sql_query)
my_conn.commit()

my_conn.close()



"""##Slide 38"""

my_conn = dbconnect ('users_database.db')

sql_query = "PRAGMA table_info('Users')"
c = my_conn.cursor()
res = c.execute(sql_query)
for item in res.fetchall():
  print(item)

my_conn.close()



"""Slide 54"""

import pandas as pd

a = [1, 7, 2]
myvar1 = pd.Series(a)

print(myvar1.to_string())

import pandas as pd

a = [1, 7, 2]
myvar2 = pd.Series(a, index = ["x", "y", "z"])

print(myvar2.to_string())



"""##Slide 56"""

import pandas as pd
dictionary = {'Greece':'Athens',
              'Germany':'Berlin',
              'Italy':'Rome'}
data1 = pd.Series(dictionary)
print(data1)

import pandas as pd

mydataset = {
  'countries': ["Greece", "Germany", "France"],
  'population': [ 10720000, 83240000, 67390000],
  'dialing_code': [ '+30', '+49', '+33']
}

data = pd.DataFrame(mydataset)

print(data)




"""##Slide 58"""

import pandas as pd

mydataset = {
  'countries': ["Greece", "Germany", "France"],
  'population': [ 10720000, 83240000, 67390000],
  'dialing_code': [ '+30', '+49', '+33']
}

data = pd.DataFrame(mydataset)

print(data['countries'],'\n')
print(data[['countries','dialing_code']],'\n')
print(data[1:2])


"""##Slide 59"""

import pandas as pd

mydataset = {
  'countries': ["Greece", "Germany", "France"],
  'population': [ 10720000, 83240000, 67390000],
  'dialing_code': [ '+30', '+49', '+33']
}

data = pd.DataFrame(mydataset)

myvar = data.loc[1:2 ,['countries', 'population']]
print(myvar)
print(type(myvar))


"""##Slide 61"""

import pandas as pd

mydataset = {
  'countries': ["Greece", "Germany", "France"],
  'population': [ 10720000, 83240000, 67390000],
  'dialing_code': [ '+30', '+49', '+33']
}

data = pd.DataFrame(mydataset)
data_sorted = data.sort_values(by='population')
print(data_sorted)

import pandas as pd

mydataset = {
  'countries': ["Greece", "Germany", "France"],
  'population': [ 10720000, 83240000, 67390000],
  'dialing_code': [ '+30', '+49', '+33']
}

data = pd.DataFrame(mydataset)
data_sorted = data.sort_values(by=['population','countries'], ascending = [False, True])
print(data_sorted)



"""##Slide 62"""
import pandas as pd
fdata = 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
df = pd.read_csv(fdata)
print(df)



"""##Slide 63"""
# εκτύπωση δεδομένων ως συμβολοσειρά
import pandas as pd
fdata = 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
df = pd.read_csv(fdata)

#print(df.to_string(),'\n') 
print(df.head(10),'\n')
print(df.tail(10),'\n') 
print(df.info(),'\n')
print(df.sort_values(by='sepal.length'),'\n')
print(df.describe(),'\n')
print(df.dtypes,'\n')
print(df.sample(8))



"""## Slide 66"""

import pandas as pd
data = {'sepal.length':[5.1, 4.9, None, 4.6, 5.0],
           'sepal.width':[3.5, 3.0, 3.4, 3.2, 2.5],
           'petal.length':[1.4, 1.4, 1.3, 1.5, None],
           'petal.width':[0.2, 0.2, 0.2, 0.2, 1.9],
           'variety':['Setosa', None, 'Setosa', 'Virginica', 'Virginica']
           }
df = pd.DataFrame(data)
print(df)



"""## Slide 67"""
import pandas as pd
data = {'sepal.length':[5.1, 4.9, None, 4.6, 5.0],
           'sepal.width':[3.5, 3.0, 3.4, 3.2, 2.5],
           'petal.length':[1.4, 1.4, 1.3, 1.5, None],
           'petal.width':[0.2, 0.2, 0.2, 0.2, 1.9],
           'variety':['Setosa', None, 'Setosa', 'Virginica', 'Virginica']
           }
df = pd.DataFrame(data)

df_1 = df.dropna()
print(df_1,'\n')

df.dropna(inplace = True)# για να μην φτιάξει καινούριο dataframe
print(df,'\n')



"""##Slide 68"""

import pandas as pd
data = {'sepal.length':[5.1, 4.9, None, 4.6, 5.0],
           'sepal.width':[3.5, 3.0, 3.4, 3.2, 2.5],
           'petal.length':[1.4, 1.4, 1.3, 1.5, None],
           'petal.width':[0.2, 0.2, 0.2, 0.2, 1.9],
           'variety':['Setosa', None, 'Setosa', 'Virginica', 'Virginica']
           }
df = pd.DataFrame(data)

df_1 = df.fillna(1.5)
print(df_1,'\n')



"""## Slide 69"""

import pandas as pd
data = {'sepal.length':[5.1, 4.9, None, 4.6, 5.0],
           'sepal.width':[3.5, 3.0, 3.4, 3.2, 2.5],
           'petal.length':[1.4, 1.4, 1.3, 1.5, None],
           'petal.width':[0.2, 0.2, 0.2, 0.2, 1.9],
           'variety':['Setosa', None, 'Setosa', 'Virginica', 'Virginica']
           }
df = pd.DataFrame(data)

x = df["petal.length"].mean() #.median() .mode()
print(x)

df["petal.length"].fillna(x, inplace = True)
print(df,'\n')



"""##Slide 70"""

import pandas as pd
data = {'sepal.length':[5.1, 4.9, None, 4.6, 5.0],
           'sepal.width':[3.5, 3.0, 3.4, 3.2, 2.5],
           'petal.length':[1.4, 1.4, 1.3, 1.5, None],
           'petal.width':[0.2, 0.2, 0.2, 0.2, 1.9],
           'variety':['Setosa', None, 'Setosa', 'Virginica', 'Virginica']
           }
df = pd.DataFrame(data)

res = df[['petal.length','sepal.width']].agg(['min','max', 'mean'])
print(res)



"""##Slide 71"""

import pandas as pd
import matplotlib.pyplot as plt

fdata = 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
df = pd.read_csv(fdata)

df2 = df[['sepal.length','sepal.width','petal.length','petal.width']].mean()
df2.plot(kind='barh')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

fdata = 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
df = pd.read_csv(fdata)

df3 = df[['sepal.length','sepal.width','petal.length','petal.width']].std()
df3.plot(kind='hist')
plt.show()




"""##Slide 76"""

import numpy as np
mylist = [1,2,3,4]
mytuple = (5,6,7,8)
array1 = np.array(mylist)
print(array1,'\n',type(array1))

array2 = np.array(mytuple)
print(array2,'\n',type(array2))



"""## Slide 77"""

import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
print(arr.itemsize)
print(arr.data)


"""##Slide 78"""

import numpy as np

arr = np.array(12)

print(arr)
print(arr.ndim)

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])

print(arr1)
print(arr1.ndim)

import numpy as np

arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr2)
print(arr2.ndim)

import numpy as np

arr3 = np.array([[
                 [1, 2, 3], 
                 [4, 5, 6]
                 ], 
                [[1, 2, 3], 
                 [4, 5, 6]
                 ]
                ]
               )
print(arr3)
print(arr3.ndim)



"""##Slide 79"""

import numpy as np
arr = np.array( [1.0, 2.0, 3.0, 4.0, 5.0])#πίνακας δεκαδικών αριθμών
print(arr)

import numpy as np
#Δημιουργία πίνακα διάστασης 4x4 με ανάθεση τιμών από 0 ως 15 ανά γραμμή
arr = np.arange(16).reshape(4,4)
print(arr)

import numpy as np
arr = np.zeros((2,4), dtype=np.float64)
#αρχικοποίηση μηδενικού πίνακα 3x4
print(arr)

import numpy as np

arr = np.empty([2,4])
print(arr)

import numpy as np
arr = np.fromfunction(lambda i, j: i + j, (4, 3))
#Πίνακας 4x3 όπου κάθε στοιχείο προκύπτει από το άθροισμα των δεικτών γραμμής και στήλης
print(arr)

import numpy as np
arr1 = np.random.randint(1,10,[3,3])
print(arr1,'\n')

arr2 = np.random.choice([3, 5, 7, 9], [3,3])
print(arr2,'\n')

arr3 = np.random.rand(2,3)
print(arr3)

arr4 = np.random.uniform([0,10], [3,3])
print(arr4)



"""## Slide 80"""

import numpy as np
arr1 = np.array([1,3,2,4,6,5])
res = np.sort(arr1)
print(res)

import numpy as np
arr1 = np.array([1,3,2,4,6,5])
res = np.where(arr1==1)
print(res)

import numpy as np
arr1 = np.array([1,3,2,4,6,5])
arr2 = np.array([7,8,9,10,11,12])
res = np.concatenate((arr1, arr2))
print(res)

import numpy as np
arr1 = np.array([1,3,2,4,6,5])
res = np.array_split(arr1,3)
print(res)

import numpy as np
arr1 = np.array([1,3,2,4,6,5])
arr2 = np.array([7,8,9,10,11,12])
res = np.dot(arr1, arr2)
print(res)



"""## Slide 81"""

import numpy as np
arr1 = np.array([1,3,2,4,6,5])
res = arr1.reshape(2,3)
print(res)

import numpy as np
arr = np.array([[0, 1], [2, 3]])
arr.resize((1, 2))
print(arr)

arr.resize((2, 3))
print(arr)

import numpy as np
arr1 = np.array([1,3,2,4,6,5])
res = arr1.copy()
arr1[2] = 10
print(arr1)
print(res)

import numpy as np
arr1 = np.array([1,3,2,4,6,5])
res = arr1.view()
arr1[2] = 10
print(arr1)
print(res)

import numpy as np
arr1 = np.array([[1,3,2,4,6,5],[7,8,9,10,11,12]])
res0 = arr1.min(axis=0)
res1 = arr1.min(axis=1)
resx = arr1.min()
print(res0)
print(res1)
print(resx)

import numpy as np
arr1 = np.array([[1,3,2,4,6,5],[7,8,9,10,11,12]])
res0 = arr1.max(axis=0)
res1 = arr1.max(axis=1)
resx = arr1.max()
print(res0)
print(res1)
print(resx)

import numpy as np
arr1 = np.array([[1,3,2,4,6,5],[7,8,9,10,11,12]])
res0 = arr1.sum(axis=0)
res1 = arr1.sum(axis=1)
resx = arr1.sum()
print(res0)
print(res1)
print(resx)

import numpy as np
arr1 = np.array([[1,3,2,4,6,5],[7,8,9,10,11,12]])
res0 = arr1.argmax(axis=0)
res1 = arr1.argmax(axis=1)
resx = arr1.argmax()
print(res0)
print(res1)
print(resx)



"""##Slide 82"""

import numpy as np
arr = np.array( [1.0, 2.0, 3.0, 4.0, 5.0]) #πίνακας δεκαδικών αριθμών
print(arr)

import numpy as np
#Δημιουργία πίνακα διάστασης 4x4 με ανάθεση τιμών από 0 ως 15 ανά γραμμή
arr = np.arange(16).reshape(4,4)
print(arr)




"""##Slide 83"""

import numpy as np
arr = np.zeros((2,4), dtype=np.float64)
#αρχικοποίηση μηδενικού πίνακα 2x4
print(arr)

import numpy as np
arr = np.fromfunction(lambda i, j: i + j, (4, 3))
#Πίνακας 4x3 όπου κάθε στοιχείο προκύπτει από το άθροισμα των δεικτών γραμμής και στήλης
print(arr)




"""##Slide 84"""

import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8])
print(arr1)

arr2 = arr1.reshape(2,4)
print(arr2)

arr3 = arr2.reshape(-1)
print(arr3)



"""##Slide 85"""

import numpy as np

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
print(arr1,'\n',arr2,'\n')

print(np.dot(arr1,arr2))



"""##Slide 86"""

import numpy as np

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
print(arr1,'\n',arr2,'\n')
print(np.multiply(arr1,arr2))



"""##Slide 88"""

import numpy as np
def myFun(x,y):
  return 2+x+y

arr1 = np.fromfunction(myFun,(3,3), dtype=int)
print(arr1,'\n')
print('Άθροισμα, ανα γραμμή:',arr1.sum(axis=1),' | ανα στήλη:',arr1.sum(axis=0),'\n')
print('Μέγιστο, ανα γραμμή:',arr1.max(axis=1),' | ανα στήλη:',arr1.max(axis=0),'\n')
print('Ελάχιστο, ανα γραμμή:',arr1.min(axis=1),' | ανα στήλη:',arr1.min(axis=0),'\n')

arr2 = arr1*1/2
print(arr2)



"""##Slide 89"""

import numpy as np

arr = np.array([[5, 1, 1],
                [4, -2, 5],
                [2, 8, 8]
                ]
               )

print("Τάξη:", np.linalg.matrix_rank(arr))

print(np.linalg.det(arr),'\n')#Ορίζουσα πίνακα

print(np.linalg.inv(arr),'\n')#Αντίστροφος πίνακας

idiotimes, idiodianismata = np.linalg.eigh(arr) # Ιδιοτιμές και ιδιοδιανύσματα
print(idiotimes,idiodianismata,'\n')




"""##Slide 90"""

#Επίλυση γραμμικού συστήματος
#2x+y-2z=-3
#3x+z=5
#x+y-z=-2
import numpy as np

A = np.array([[2,1,-2],[3,0,1],[1,1,-1]])
Β = np.transpose(np.array([[-3,5,-2]]))
print(np.linalg.solve(A,Β))



"""##Slide 93 """

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.show()



"""##Slide 94"""

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.title("ΤΙΤΛΟΣ ΔΙΑΓΡΑΜΜΑΤΟΣ")
plt.xlabel("Περιγραφή άξονα x")
plt.ylabel("Περιγραφή άξονα y")
plt.xticks(fontsize=8, rotation=20)
plt.show()



"""##Slide 95"""

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [2, 4, 6, 8], label="Σειρά-1")
plt.plot([1, 2, 3, 4], [3, 5, 7, 9], label="Σειρά-2")
plt.xlabel("Περιγραφή άξονα x")
plt.ylabel("Περιγραφή άξονα y")
plt.legend(fontsize=8)
plt.show()



"""#Slide 102"""

import tkinter
w1 = tkinter.Tk() #Δημιουργία παραθύρου w1
w1.title("Παράδειγμα 1")
L1 = tkinter.Label(w1, text="   Hello World!  ", font="Arial 40")
L1.pack() # τοποθέτηση label L1 στο παράθυρο w1
w1.mainloop() # έναρξη βρόχου



"""##Slide 103"""
# Μηχανή γεωμετρίας pack()
import tkinter as tk
root = tk.Tk()
root.geometry('200x200+200+200')
# case 1
tk.Label(root, text='Label', bg='green').pack()
tk.Label(root, text='Label2', bg='red').pack()
# case 2
#tk.Label(root, text='Label', bg='green').pack(expand=1, fill ='y')
#tk.Label(root, text='Label2', bg='red').pack(fill = 'both')
# case 3
#tk.Label(root, text='Label', bg='green').pack(expand=1)
#tk.Label(root, text='Label2', bg='red').pack(fill = 'both')
# case 4
#tk.Label(root, text='Label', bg='green').pack(fill='both', expand=1, side='left')
#tk.Label(root, text='Label2', bg='red').pack(fill='both', expand=1, side='right')
# case 5
#tk.Label(root, text='Label', bg='green').pack(fill = 'both', expand=1)
#tk.Label(root, text='Label2', bg='red').pack(fill = 'both', expand=1)
root.mainloop()



"""##Slide 104"""

# Παράδειγμα με χρήση κλάσης
import tkinter as tk
class MyApp():
    def __init__(self, root, case):
        root.geometry('200x200+200+200')
        if case==1:
            tk.Label(root, text='Label', bg='green').pack()
            tk.Label(root, text='Label2', bg='red').pack()
        elif case==2:
            tk.Label(root, text='Label', bg='green').pack(expand=1, fill ='y')
            tk.Label(root, text='Label2', bg='red').pack(fill = 'both')
        elif case==3:
            tk.Label(root, text='Label', bg='green').pack(expand=1)
            tk.Label(root, text='Label2', bg='red').pack(fill = 'both')
        elif case==4:
            tk.Label(root, text='Label', bg='green').pack(fill='both', expand=1, side='left')
            tk.Label(root, text='Label2', bg='red').pack(fill='both', expand=1, side='right')
        else: # case 5
            tk.Label(root, text='Label', bg='green').pack(fill = 'both', expand=1)
            tk.Label(root, text='Label2', bg='red').pack(fill = 'both', expand=1)
w1 = tk.Tk()
MyApp(w1,4)
w2 = tk.Tk()
MyApp(w2,5)
w1.mainloop()
w2.mainloop()



"""## Slide 105"""

# Button Widget
import tkinter

def b1pushed():
    print("Button 1 was pressed.")
    return

def b2pushed():
    w1.destroy()
    return

w1 = tkinter.Tk()
tkinter.Label(w1,text="Hello there!").pack()
tkinter.Button(w1,text="Button1",command=b1pushed).pack()
tkinter.Button(w1,text="Button2",command=b2pushed).pack()
w1.mainloop()



"""##Slide 106"""

import tkinter

def b1pushed():
    name = e1.get()
    print("Hello",name)
    return

w1 = tkinter.Tk()
tkinter.Label(w1,text="Type your name:").pack()
e1 = tkinter.Entry(w1)
e1.pack()
tkinter.Button(w1,text="OK",command=b1pushed).pack()
w1.mainloop()



"""##Slide 107"""

import tkinter

def b1pushed():
    name = e1.get()
    myText.set("User: "+name)
    return

w1 = tkinter.Tk()
tkinter.Label(w1,text="Type your name:").pack()
e1 = tkinter.Entry(w1)
e1.pack()
tkinter.Button(w1,text="OK",command=b1pushed).pack()
myText = tkinter.StringVar()
myText.set("Unknown user")
tkinter.Label(w1,textvariable=myText).pack()
w1.mainloop()



"""##Slide 115"""

import sys, os

def run_terminal(command, mdf="my_dummy_file.txt"):
    os.system(command+" > "+mdf)
    f=open(mdf, "r")
    cont=f.read()
    f.close()
    print(cont)
    if os.path.exists(mdf): os.remove(mdf)
    else: print("ERROR: Cannot delete "+mdf+" File does not exist")

def IDLE_pip(command):
    run_terminal(sys.executable + " -m pip " + command)

IDLE_pip("list")
IDLE_pip("show pip")
IDLE_pip("install πακέτο")
IDLE_pip("uninstall πακέτο")



"""##Slide 118"""

import time

L=[]
start_time = time.perf_counter() # αρχή μέτρησης
for i in range(10000):
    L.append(i)
finish_time = time.perf_counter() # τέλος μέτρησης
print(len(L))
print(finish_time - start_time) # διαφορά χρόνου