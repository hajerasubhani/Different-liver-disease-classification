Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\9701239167\Desktop\m.tech project\datasets\2.Acute Liver Failure\prepocessing.py 
#printing the dataset
      Age Gender Region ...   Family Hepatitis  Chronic Fatigue  ALF
0      65      M   east ...                0.0              0.0  0.0
1      36      M  south ...                0.0              0.0  0.0
2      66      M   east ...                0.0              0.0  0.0
3      54      M   east ...                0.0              0.0  0.0
4      63      M  north ...                0.0              0.0  0.0
5      26      F   east ...                0.0              0.0  0.0
6      66      F  north ...                0.0              0.0  0.0
7      59      M   east ...                0.0              0.0  0.0
8      53      M   east ...                0.0              0.0  0.0
9      78      M  north ...                0.0              NaN  0.0
10     47      F   east ...                0.0              0.0  0.0
11     47      M  south ...                0.0              0.0  0.0
12     62      F  south ...                0.0              0.0  0.0
13     36      F  south ...                0.0              0.0  0.0
14     60      M  south ...                0.0              0.0  0.0
15     30      M  south ...                0.0              0.0  0.0
16     47      M  south ...                0.0              0.0  0.0
17     53      M   east ...                0.0              0.0  1.0
18     28      M   east ...                0.0              0.0  0.0
19     30      M  south ...                1.0              0.0  0.0
20     52      F   east ...                0.0              0.0  0.0
21     24      M   east ...                0.0              0.0  0.0
22     38      M  south ...                0.0              0.0  0.0
23     85      M  south ...                0.0              0.0  0.0
24     21      F  south ...                0.0              0.0  0.0
25     46      F  south ...                0.0              0.0  0.0
26     74      F  north ...                0.0              0.0  0.0
27     46      F   east ...                0.0              0.0  0.0
28     58      F  north ...                0.0              0.0  0.0
29     35      F   east ...                0.0              0.0  0.0
...   ...    ...    ... ...                ...              ...  ...
8755   67      F   east ...                0.0              0.0  NaN
8756   38      M   east ...                0.0              0.0  NaN
8757   31      F   east ...                0.0              0.0  NaN
8758   39      F  south ...                0.0              0.0  NaN
8759   27      F   east ...                0.0              0.0  NaN
8760   61      M  south ...                0.0              0.0  NaN
8761   30      M  south ...                0.0              0.0  NaN
8762   25      M  south ...                0.0              0.0  NaN
8763   68      M  south ...                0.0              0.0  NaN
8764   58      M   east ...                0.0              0.0  NaN
8765   41      F   east ...                0.0              0.0  NaN
8766   46      M  south ...                0.0              0.0  NaN
8767   70      F   east ...                0.0              0.0  NaN
8768   66      F  north ...                0.0              0.0  NaN
8769   61      M  south ...                0.0              0.0  NaN
8770   66      M   east ...                0.0              0.0  NaN
8771   33      F  south ...                0.0              0.0  NaN
8772   43      F  south ...                0.0              0.0  NaN
8773   78      M  south ...                0.0              NaN  NaN
8774   35      M   east ...                0.0              0.0  NaN
8775   70      M  south ...                0.0              0.0  NaN
8776   58      F   east ...                0.0              1.0  NaN
8777   37      M   west ...                0.0              0.0  NaN
8778   22      M   east ...                1.0              0.0  NaN
8779   29      F   east ...                0.0              0.0  NaN
8780   35      F   east ...                0.0              0.0  NaN
8781   66      F  north ...                0.0              0.0  NaN
8782   37      F  south ...                0.0              0.0  NaN
8783   39      F   east ...                0.0              0.0  NaN
8784   70      M   east ...                0.0              0.0  NaN

[8785 rows x 30 columns]
#to know what are the columns in ur dataset
Index(['Age', 'Gender', 'Region', 'Weight', 'Height', 'Body Mass Index',
       'Obesity', 'Waist', 'Maximum Blood Pressure', 'Minimum Blood Pressure',
       'Good Cholesterol', 'Bad Cholesterol', 'Total Cholesterol',
       'Dyslipidemia', 'PVD', 'Physical Activity', 'Education', 'Unmarried',
       'Income', 'Source of Care', 'PoorVision', 'Alcohol Consumption',
       'HyperTension', 'Family  HyperTension', 'Diabetes', 'Family Diabetes',
       'Hepatitis', 'Family Hepatitis', 'Chronic Fatigue', 'ALF'],
      dtype='object')
#head function will help us printing top 5 rows(instances) of the dataset
   Age Gender Region ...   Family Hepatitis  Chronic Fatigue  ALF
0   65      M   east ...                0.0              0.0  0.0
1   36      M  south ...                0.0              0.0  0.0
2   66      M   east ...                0.0              0.0  0.0
3   54      M   east ...                0.0              0.0  0.0
4   63      M  north ...                0.0              0.0  0.0

[5 rows x 30 columns]
#tail function will help us printing bottom 5 rows(instances) of the dataset
      Age Gender Region ...   Family Hepatitis  Chronic Fatigue  ALF
8780   35      F   east ...                0.0              0.0  NaN
8781   66      F  north ...                0.0              0.0  NaN
8782   37      F  south ...                0.0              0.0  NaN
8783   39      F   east ...                0.0              0.0  NaN
8784   70      M   east ...                0.0              0.0  NaN

[5 rows x 30 columns]
#checking number of null values in each attribute 
Age                          0
Gender                       0
Region                       0
Weight                     194
Height                     191
Body Mass Index            290
Obesity                    290
Waist                      314
Maximum Blood Pressure     304
Minimum Blood Pressure     376
Good Cholesterol            17
Bad Cholesterol             18
Total Cholesterol           16
Dyslipidemia                 0
PVD                          0
Physical Activity           10
Education                   20
Unmarried                  452
Income                    1161
Source of Care               0
PoorVision                 563
Alcohol Consumption          0
HyperTension                80
Family  HyperTension         0
Diabetes                     2
Family Diabetes              0
Hepatitis                   22
Family Hepatitis             6
Chronic Fatigue             35
ALF                       2785
dtype: int64
#Another useful method if value_counts() which can get count of each category in a categorical attributed series of values. For an instance suppose you are dealing with a dataset of customers who are divided as youth, medium and old categories under column name age and your dataframe is “DF”. You can run this statement to know how many people fall in respective categories. In our data set example education column can be used
85    249
21    177
22    176
40    174
23    173
20    173
45    170
37    170
26    169
44    168
30    166
42    164
60    163
39    162
29    162
32    162
62    161
24    160
41    158
34    155
46    151
27    150
31    149
25    147
35    147
28    146
38    144
70    143
43    143
64    142
     ... 
33    133
53    131
66    131
63    128
49    125
65    125
67    125
50    121
68    118
48    118
71    113
81    111
72    110
73    110
56    108
57    105
55    103
69    100
74     99
75     98
80     92
76     90
77     88
82     81
59     79
58     77
78     74
84     66
79     62
83     53
Name: Age, Length: 66, dtype: int64
# for computing correlations
                             Age    Weight    ...     Chronic Fatigue       ALF
Age                     1.000000 -0.045157    ...            0.176459  0.367639
Weight                 -0.045157  1.000000    ...            0.026088 -0.019161
Height                 -0.121437  0.458892    ...           -0.026622 -0.050380
Body Mass Index         0.019808  0.862399    ...            0.041763  0.004539
Obesity                 0.004970  0.662575    ...            0.028031  0.008785
Waist                   0.178103  0.872568    ...            0.068361  0.060799
Maximum Blood Pressure  0.553844  0.057283    ...            0.061129  0.216645
Minimum Blood Pressure  0.019171  0.185339    ...           -0.048076 -0.087266
Good Cholesterol        0.025275 -0.314143    ...           -0.050919 -0.031826
Bad Cholesterol         0.145062  0.124533    ...           -0.012035  0.033539
Total Cholesterol       0.155087  0.009265    ...           -0.030876  0.021847
Dyslipidemia            0.032718  0.072681    ...            0.018041  0.001812
PVD                     0.234480 -0.043910    ...            0.077320  0.168850
Physical Activity      -0.169622 -0.043476    ...           -0.088232 -0.119817
Education              -0.105897  0.044938    ...           -0.059782 -0.059445
Unmarried              -0.013485 -0.060537    ...            0.032851  0.063628
Income                 -0.151117  0.037603    ...           -0.083515 -0.092472
PoorVision              0.166340 -0.031072    ...            0.040782  0.100678
Alcohol Consumption     0.202266  0.093446    ...            0.056064  0.067631
HyperTension            0.491531  0.126719    ...            0.129491  0.232705
Family  HyperTension   -0.116944  0.082806    ...            0.007458 -0.045650
Diabetes                0.239842  0.120990    ...            0.118911  0.155641
Family Diabetes         0.094034  0.096377    ...            0.032327  0.017326
Hepatitis               0.266345  0.024441    ...            0.337806  0.214971
Family Hepatitis       -0.018104 -0.032113    ...            0.008495  0.056097
Chronic Fatigue         0.176459  0.026088    ...            1.000000  0.162796
ALF                     0.367639 -0.019161    ...            0.162796  1.000000

[27 rows x 27 columns]
# computes numerical data ranks 
         Age  Gender  Region   ...    Family Hepatitis  Chronic Fatigue     ALF
0     6610.0  6470.5  2162.5   ...              4300.0           4248.5  2768.5
1     2615.5  6470.5  7213.5   ...              4300.0           4248.5  2768.5
2     6738.0  6470.5  2162.5   ...              4300.0           4248.5  2768.5
3     5272.5  6470.5  2162.5   ...              4300.0           4248.5  2768.5
4     6341.5  6470.5  5123.0   ...              4300.0           4248.5  2768.5
5     1091.0  2078.0  2162.5   ...              4300.0           4248.5  2768.5
6     6738.0  2078.0  5123.0   ...              4300.0           4248.5  2768.5
7     5772.0  6470.5  2162.5   ...              4300.0           4248.5  2768.5
8     5140.0  6470.5  2162.5   ...              4300.0           4248.5  2768.5
9     8034.5  6470.5  5123.0   ...              4300.0              NaN  2768.5
10    4358.5  2078.0  2162.5   ...              4300.0           4248.5  2768.5
11    4358.5  6470.5  7213.5   ...              4300.0           4248.5  2768.5
12    6197.0  2078.0  7213.5   ...              4300.0           4248.5  2768.5
13    2615.5  2078.0  7213.5   ...              4300.0           4248.5  2768.5
14    5893.0  6470.5  7213.5   ...              4300.0           4248.5  2768.5
15    1716.5  6470.5  7213.5   ...              4300.0           4248.5  2768.5
16    4358.5  6470.5  7213.5   ...              4300.0           4248.5  2768.5
17    5140.0  6470.5  2162.5   ...              4300.0           4248.5  5768.5
18    1398.5  6470.5  2162.5   ...              4300.0           4248.5  2768.5
19    1716.5  6470.5  7213.5   ...              8689.5           4248.5  2768.5
20    5003.5  2078.0  2162.5   ...              4300.0           4248.5  2768.5
21     779.5  6470.5  2162.5   ...              4300.0           4248.5  2768.5
22    2927.5  6470.5  7213.5   ...              4300.0           4248.5  2768.5
23    8661.0  6470.5  7213.5   ...              4300.0           4248.5  2768.5
24     262.0  2078.0  7213.5   ...              4300.0           4248.5  2768.5
25    4214.0  2078.0  7213.5   ...              4300.0           4248.5  2768.5
26    7672.0  2078.0  5123.0   ...              4300.0           4248.5  2768.5
27    4214.0  2078.0  2162.5   ...              4300.0           4248.5  2768.5
28    5694.0  2078.0  5123.0   ...              4300.0           4248.5  2768.5
29    2472.0  2078.0  2162.5   ...              4300.0           4248.5  2768.5
...      ...     ...     ...   ...                 ...              ...     ...
8755  6866.0  2078.0  2162.5   ...              4300.0           4248.5     NaN
8756  2927.5  6470.5  2162.5   ...              4300.0           4248.5     NaN
8757  1874.0  2078.0  2162.5   ...              4300.0           4248.5     NaN
8758  3080.5  2078.0  7213.5   ...              4300.0           4248.5     NaN
8759  1250.5  2078.0  2162.5   ...              4300.0           4248.5     NaN
8760  6045.5  6470.5  7213.5   ...              4300.0           4248.5     NaN
8761  1716.5  6470.5  7213.5   ...              4300.0           4248.5     NaN
8762   933.0  6470.5  7213.5   ...              4300.0           4248.5     NaN
8763  6987.5  6470.5  7213.5   ...              4300.0           4248.5     NaN
8764  5694.0  6470.5  2162.5   ...              4300.0           4248.5     NaN
8765  3414.5  2078.0  2162.5   ...              4300.0           4248.5     NaN
8766  4214.0  6470.5  7213.5   ...              4300.0           4248.5     NaN
8767  7218.0  2078.0  2162.5   ...              4300.0           4248.5     NaN
8768  6738.0  2078.0  5123.0   ...              4300.0           4248.5     NaN
8769  6045.5  6470.5  7213.5   ...              4300.0           4248.5     NaN
8770  6738.0  6470.5  2162.5   ...              4300.0           4248.5     NaN
8771  2177.0  2078.0  7213.5   ...              4300.0           4248.5     NaN
8772  3729.0  2078.0  7213.5   ...              4300.0           4248.5     NaN
8773  8034.5  6470.5  7213.5   ...              4300.0              NaN     NaN
8774  2472.0  6470.5  2162.5   ...              4300.0           4248.5     NaN
8775  7218.0  6470.5  7213.5   ...              4300.0           4248.5     NaN
8776  5694.0  2078.0  2162.5   ...              4300.0           8623.5     NaN
8777  2770.5  6470.5  8645.5   ...              4300.0           4248.5     NaN
8778   438.5  6470.5  2162.5   ...              8689.5           4248.5     NaN
8779  1552.5  2078.0  2162.5   ...              4300.0           4248.5     NaN
8780  2472.0  2078.0  2162.5   ...              4300.0           4248.5     NaN
8781  6738.0  2078.0  5123.0   ...              4300.0           4248.5     NaN
8782  2770.5  2078.0  7213.5   ...              4300.0           4248.5     NaN
8783  3080.5  2078.0  2162.5   ...              4300.0           4248.5     NaN
8784  7218.0  6470.5  2162.5   ...              4300.0           4248.5     NaN

[8785 rows x 30 columns]
# prints first 5 rows and every column which replicates dataset.head() 
   Age Gender Region ...   Family Hepatitis  Chronic Fatigue  ALF
0   65      M   east ...                0.0              0.0  0.0
1   36      M  south ...                0.0              0.0  0.0
2   66      M   east ...                0.0              0.0  0.0
3   54      M   east ...                0.0              0.0  0.0
4   63      M  north ...                0.0              0.0  0.0

[5 rows x 30 columns]
      Age Gender Region ...   Family Hepatitis  Chronic Fatigue  ALF
0      65      M   east ...                0.0              0.0  0.0
1      36      M  south ...                0.0              0.0  0.0
2      66      M   east ...                0.0              0.0  0.0
3      54      M   east ...                0.0              0.0  0.0
4      63      M  north ...                0.0              0.0  0.0
5      26      F   east ...                0.0              0.0  0.0
6      66      F  north ...                0.0              0.0  0.0
7      59      M   east ...                0.0              0.0  0.0
8      53      M   east ...                0.0              0.0  0.0
9      78      M  north ...                0.0              NaN  0.0
10     47      F   east ...                0.0              0.0  0.0
11     47      M  south ...                0.0              0.0  0.0
12     62      F  south ...                0.0              0.0  0.0
13     36      F  south ...                0.0              0.0  0.0
14     60      M  south ...                0.0              0.0  0.0
15     30      M  south ...                0.0              0.0  0.0
16     47      M  south ...                0.0              0.0  0.0
17     53      M   east ...                0.0              0.0  1.0
18     28      M   east ...                0.0              0.0  0.0
19     30      M  south ...                1.0              0.0  0.0
20     52      F   east ...                0.0              0.0  0.0
21     24      M   east ...                0.0              0.0  0.0
22     38      M  south ...                0.0              0.0  0.0
23     85      M  south ...                0.0              0.0  0.0
24     21      F  south ...                0.0              0.0  0.0
25     46      F  south ...                0.0              0.0  0.0
26     74      F  north ...                0.0              0.0  0.0
27     46      F   east ...                0.0              0.0  0.0
28     58      F  north ...                0.0              0.0  0.0
29     35      F   east ...                0.0              0.0  0.0
...   ...    ...    ... ...                ...              ...  ...
8755   67      F   east ...                0.0              0.0  NaN
8756   38      M   east ...                0.0              0.0  NaN
8757   31      F   east ...                0.0              0.0  NaN
8758   39      F  south ...                0.0              0.0  NaN
8759   27      F   east ...                0.0              0.0  NaN
8760   61      M  south ...                0.0              0.0  NaN
8761   30      M  south ...                0.0              0.0  NaN
8762   25      M  south ...                0.0              0.0  NaN
8763   68      M  south ...                0.0              0.0  NaN
8764   58      M   east ...                0.0              0.0  NaN
8765   41      F   east ...                0.0              0.0  NaN
8766   46      M  south ...                0.0              0.0  NaN
8767   70      F   east ...                0.0              0.0  NaN
8768   66      F  north ...                0.0              0.0  NaN
8769   61      M  south ...                0.0              0.0  NaN
8770   66      M   east ...                0.0              0.0  NaN
8771   33      F  south ...                0.0              0.0  NaN
8772   43      F  south ...                0.0              0.0  NaN
8773   78      M  south ...                0.0              NaN  NaN
8774   35      M   east ...                0.0              0.0  NaN
8775   70      M  south ...                0.0              0.0  NaN
8776   58      F   east ...                0.0              1.0  NaN
8777   37      M   west ...                0.0              0.0  NaN
8778   22      M   east ...                1.0              0.0  NaN
8779   29      F   east ...                0.0              0.0  NaN
8780   35      F   east ...                0.0              0.0  NaN
8781   66      F  north ...                0.0              0.0  NaN
8782   37      F  south ...                0.0              0.0  NaN
8783   39      F   east ...                0.0              0.0  NaN
8784   70      M   east ...                0.0              0.0  NaN

[8785 rows x 30 columns]
      Age Gender Region  Weight  Height
5      26      F   east   119.3   193.2
6      66      F  north    85.1   172.1
7      59      M   east    69.9   160.9
8      53      M   east    75.2   174.1
9      78      M  north    47.6   155.3
10     47      F   east    99.6   188.2
11     47      M  south    49.0   155.3
12     62      F  south    56.1   165.5
13     36      F  south    78.8   183.8
14     60      M  south    68.3   146.7
15     30      M  south    68.3   157.8
16     47      M  south    62.1   149.6
17     53      M   east    94.9   178.0
18     28      M   east    65.0   156.8
19     30      M  south   109.8   166.6
20     52      F   east    96.8   186.4
21     24      M   east    76.8   155.1
22     38      M  south    67.0   153.7
23     85      M  south    38.5     NaN
24     21      F  south    64.2   167.0
25     46      F  south    99.6   173.6
26     74      F  north    63.6   172.4
27     46      F   east    88.6   172.9
28     58      F  north   179.0   181.3
29     35      F   east    66.8   181.9
30     27      M   east    89.1   168.9
31     81      M   east    68.4   164.2
32     44      M  south   105.4   145.3
33     53      F  south    77.1   168.7
34     38      F  south    80.5   171.0
...   ...    ...    ...     ...     ...
8755   67      F   east    84.9   169.7
8756   38      M   east    81.6   174.9
8757   31      F   east    72.6   177.1
8758   39      F  south    83.6   168.3
8759   27      F   east    65.6   174.3
8760   61      M  south    70.6   152.2
8761   30      M  south    96.0   156.2
8762   25      M  south    62.3   160.6
8763   68      M  south    70.5   166.3
8764   58      M   east    57.9   152.1
8765   41      F   east    83.3   167.0
8766   46      M  south    90.0   161.9
8767   70      F   east    92.2   167.7
8768   66      F  north    67.7   187.3
8769   61      M  south    72.7   151.6
8770   66      M   east    74.2   161.6
8771   33      F  south    77.6   168.3
8772   43      F  south    75.5   164.8
8773   78      M  south    64.3   160.0
8774   35      M   east    67.9   161.4
8775   70      M  south    94.3   162.3
8776   58      F   east    85.2   182.6
8777   37      M   west    57.3   162.4
8778   22      M   east    70.9   168.9
8779   29      F   east    99.5   177.3
8780   35      F   east    70.0   171.5
8781   66      F  north   102.0   180.7
8782   37      F  south    84.4   186.0
8783   39      F   east    92.1   184.8
8784   70      M   east    58.5   161.1

[8780 rows x 5 columns]
               Age       Weight     ...       Chronic Fatigue          ALF
count  8785.000000  8591.000000     ...           8750.000000  6000.000000
mean     49.349915    79.100198     ...              0.029029     0.077333
std      18.831309    19.406975     ...              0.167896     0.267142
min      20.000000    25.600000     ...              0.000000     0.000000
25%      33.000000    65.400000     ...              0.000000     0.000000
50%      47.000000    76.800000     ...              0.000000     0.000000
75%      65.000000    89.550000     ...              0.000000     0.000000
max      85.000000   193.300000     ...              1.000000     1.000000

[8 rows x 27 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8785 entries, 0 to 8784
Data columns (total 30 columns):
Age                       8785 non-null int64
Gender                    8785 non-null object
Region                    8785 non-null object
Weight                    8591 non-null float64
Height                    8594 non-null float64
Body Mass Index           8495 non-null float64
Obesity                   8495 non-null float64
Waist                     8471 non-null float64
Maximum Blood Pressure    8481 non-null float64
Minimum Blood Pressure    8409 non-null float64
Good Cholesterol          8768 non-null float64
Bad Cholesterol           8767 non-null float64
Total Cholesterol         8769 non-null float64
Dyslipidemia              8785 non-null int64
PVD                       8785 non-null int64
Physical Activity         8775 non-null float64
Education                 8765 non-null float64
Unmarried                 8333 non-null float64
Income                    7624 non-null float64
Source of Care            8785 non-null object
PoorVision                8222 non-null float64
Alcohol Consumption       8785 non-null int64
HyperTension              8705 non-null float64
Family  HyperTension      8785 non-null int64
Diabetes                  8783 non-null float64
Family Diabetes           8785 non-null int64
Hepatitis                 8763 non-null float64
Family Hepatitis          8779 non-null float64
Chronic Fatigue           8750 non-null float64
ALF                       6000 non-null float64
dtypes: float64(21), int64(6), object(3)
memory usage: 2.0+ MB

(8785, 30)


<class 'pandas.core.frame.DataFrame'>
>>> 
