# data-versioner
Data versioner is a python package that offers git-like tracking of your dataframe so that your experimental variations and EDA findings are preserved, even as your notebook evolves.

## Import and initialize data versioner
```python
>>> from dataversioner.dataversioner import DataVersioner
>>> import pandas as pd

>>> df = pd.DataFrame([[1, 2, 3],[4, 5, 6], [7, 8, 9]], 
                  columns = ["a", "b", "c"])

>>> dv = DataVersioner(df)
>>> dv.commits()
['Initial df']
```

## Add commits
```python
>>> dv.data['sum'] = dv.data.sum(axis=1)
>>> dv.data
a	b	c	sum
0	1	2	3	6
1	4	5	6	15
2	7	8	9	24

>>> dv.commit("Row sum", "Added 'sum' of a, b, c")
>>> dv.commits()
['Initial df', 'Row sum']
```

## View commits
```python
# See current commit
>>> dv.status()
'Row sum' - Added 'sum' of a, b, c
Committed at 05:03 PM on Mar 06, 2022

   a  b  c  sum
0  1  2  3    6
1  4  5  6   15
2  7  8  9   24

>>> dv.show_commit('Initial df')
'Initial df' - First commit of data
Committed at 05:06 PM on Mar 06, 2022

   a  b  c
0  1  2  3
1  4  5  6
2  7  8  9

>>> dv.show_commits()
Initial df
   - Row sum
```

## Checkout commits
```python
>>> dv.checkout('Initial df')
>>> dv.data
a	b	c
0	1	2	3
1	4	5	6
2	7	8	9
```
