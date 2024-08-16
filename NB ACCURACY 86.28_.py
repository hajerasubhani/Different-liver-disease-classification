Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\9701239167\Desktop\m.tech project\datasets\2.Acute Liver Failure\naive bayes.py 
   Age Gender Region ...   Family Hepatitis  Chronic Fatigue  ALF
0   65      M   east ...                  0                0    0
1   36      M  south ...                  0                0    0
2   66      M   east ...                  0                0    0
3   54      M   east ...                  0                0    0
4   63      M  north ...                  0                0    0

[5 rows x 30 columns]
(8785, 30)
Traceback (most recent call last):
  File "C:\Users\9701239167\Desktop\m.tech project\datasets\2.Acute Liver Failure\naive bayes.py", line 24, in <module>
    gnb.fit(X_train, y_train)
  File "C:\Users\9701239167\AppData\Local\Programs\Python\Python36\lib\site-packages\sklearn\naive_bayes.py", line 190, in fit
    X, y = check_X_y(X, y)
  File "C:\Users\9701239167\AppData\Local\Programs\Python\Python36\lib\site-packages\sklearn\utils\validation.py", line 756, in check_X_y
    estimator=estimator)
  File "C:\Users\9701239167\AppData\Local\Programs\Python\Python36\lib\site-packages\sklearn\utils\validation.py", line 527, in check_array
    array = np.asarray(array, dtype=dtype, order=order)
  File "C:\Users\9701239167\AppData\Local\Programs\Python\Python36\lib\site-packages\numpy\core\numeric.py", line 501, in asarray
    return array(a, dtype, copy=False, order=order)
ValueError: could not convert string to float: 'F'
>>> 
 RESTART: C:\Users\9701239167\Desktop\m.tech project\datasets\2.Acute Liver Failure\naive bayes.py 
   Age  Gender  Region ...   Family Hepatitis  Chronic Fatigue  ALF
0   65       0       3 ...                  0                0    0
1   36       0       2 ...                  0                0    0
2   66       0       3 ...                  0                0    0
3   54       0       3 ...                  0                0    0
4   63       0       1 ...                  0                0    0

[5 rows x 30 columns]
(8785, 30)
Confusion Matrix:  [[1454  193]
 [  48   62]]
Gaussian Naive Bayes model accuracy(in %): 86.28343767786
>>> 
