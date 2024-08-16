Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\9701239167\Desktop\m.tech project\datasets\2.Acute Liver Failure\max and min vale count.py 
   Age Gender Region ...   Family Hepatitis  Chronic Fatigue  ALF
0   65      M   east ...                0.0              0.0  0.0
1   36      M  south ...                0.0              0.0  0.0
2   66      M   east ...                0.0              0.0  0.0
3   54      M   east ...                0.0              0.0  0.0
4   63      M  north ...                0.0              0.0  0.0

[5 rows x 30 columns]
prints the max vale and in vale
Age                           85
Gender                         M
Region                      west
Weight                     193.3
Height                     200.1
Body Mass Index            66.44
Obesity                        1
Waist                      173.4
Maximum Blood Pressure       233
Minimum Blood Pressure       132
Good Cholesterol             160
Bad Cholesterol              684
Total Cholesterol            727
Dyslipidemia                   1
PVD                            1
Physical Activity              4
Education                      1
Unmarried                      1
Income                         1
Source_of_Care            clinic
PoorVision                     1
Alcohol Consumption            1
HyperTension                   1
Family  HyperTension           1
Diabetes                       1
Family Diabetes                1
Hepatitis                      1
Family Hepatitis               1
Chronic Fatigue                1
ALF                            1
dtype: object
Traceback (most recent call last):
  File "C:\Users\9701239167\Desktop\m.tech project\datasets\2.Acute Liver Failure\max and min vale count.py", line 20, in <module>
    print(dataset.value_counts())
  File "C:\Users\9701239167\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'value_counts'
>>> 
