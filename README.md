# Pandas Indexing: A Comprehensive Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Index Basics](#index-basics)
3. [Label-based Indexing (.loc)](#label-based-indexing-loc)
4. [Position-based Indexing (.iloc)](#position-based-indexing-iloc)
5. [Boolean Indexing](#boolean-indexing)
6. [MultiIndex](#multiindex)
7. [Advanced Indexing Techniques](#advanced-indexing-techniques)
8. [Performance Considerations](#performance-considerations)

## Introduction

Pandas indexing is the foundation of data selection and manipulation in pandas DataFrames and Series. Understanding indexing is crucial for efficient data analysis and manipulation.

## Index Basics

### What is an Index?
An index in pandas is a label for rows or columns that provides fast access to data.

```python
import pandas as pd

# Creating a Series with custom index
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
```

### DataFrame Index
```python
# Creating DataFrame with custom index
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['row1', 'row2', 'row3'])
```

## Label-based Indexing (.loc)

### Basic .loc Usage
```python
# Select single row
df.loc['row1']

# Select multiple rows
df.loc['row1':'row3']

# Select specific rows and columns
df.loc['row1', 'A']
df.loc['row1':'row2', 'A':'B']

# Select with lists
df.loc[['row1', 'row3'], ['A']]
```

### Advanced .loc Operations
```python
# Conditional selection
df.loc[df['A'] > 1]

# Setting values
df.loc['row1', 'A'] = 100
df.loc[df['A'] > 1, 'B'] = 999
```

## Position-based Indexing (.iloc)

### Basic .iloc Usage
```python
# Select by position
df.iloc[0]  # First row
df.iloc[-1]  # Last row
df.iloc[0:2]  # First two rows

# Select rows and columns by position
df.iloc[0, 1]  # First row, second column
df.iloc[0:2, 0:1]  # First two rows, first column
```

### Slicing with .iloc
```python
# Various slicing patterns
df.iloc[:, 0]  # All rows, first column
df.iloc[::2, :]  # Every other row
df.iloc[::-1, :]  # Reverse row order
```

## Boolean Indexing

### Creating Boolean Masks
```python
# Simple conditions
mask = df['A'] > 1
filtered_df = df[mask]

# Multiple conditions
mask = (df['A'] > 1) & (df['B'] < 6)
filtered_df = df[mask]

# Using isin()
mask = df['A'].isin([1, 3])
filtered_df = df[mask]
```

### Boolean Indexing with .loc
```python
# Combining boolean indexing with .loc
df.loc[df['A'] > 1, 'B'] = 100

# Complex conditions
df.loc[(df['A'] > 1) & (df['B'] < 10), ['A', 'B']]
```

## MultiIndex

### Creating MultiIndex
```python
# Creating MultiIndex DataFrame
arrays = [['A', 'A', 'B', 'B'], [1, 2, 1, 2]]
index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
df_multi = pd.DataFrame({'values': [10, 20, 30, 40]}, index=index)
```

### Indexing MultiIndex
```python
# Access level 0
df_multi.loc['A']

# Access specific combination
df_multi.loc[('A', 1)]

# Cross-section
df_multi.xs('A', level='first')
df_multi.xs(1, level='second')

# Using tuple for multiple levels
df_multi.loc[('A', 1), 'values']
```

### MultiIndex Operations
```python
# Swapping levels
df_multi.swaplevel()

# Sorting by index
df_multi.sort_index()

# Resetting index
df_multi.reset_index()
```

## Advanced Indexing Techniques

### Query Method
```python
# Using query for complex conditions
df.query('A > 1 and B < 6')
df.query('A in [1, 3]')

# With variables
threshold = 2
df.query('A > @threshold')
```

### Setting and Resetting Index
```python
# Setting new index
df.set_index('A')

# Resetting index
df.reset_index()
df.reset_index(drop=True)

# Multiple column index
df.set_index(['A', 'B'])
```

### Index Operations
```python
# Reindexing
new_index = ['row1', 'row2', 'row4']
df.reindex(new_index)

# Forward fill missing values
df.reindex(new_index, method='ffill')

# Renaming index
df.rename(index={'row1': 'first_row'})
```

## Performance Considerations

### Index Performance Tips
```python
# Sorting index for better performance
df.sort_index(inplace=True)

# Using categorical index for memory efficiency
df.index = df.index.astype('category')

# Avoiding chained indexing
# Bad: df['A'][0] = value
# Good: df.loc[0, 'A'] = value
```

### Memory Optimization
```python
# Using appropriate data types
df = df.astype({'A': 'int32', 'B': 'float32'})

# Setting index on frequently accessed columns
df.set_index('frequently_used_column', inplace=True)
```

### Best Practices
- Use `.loc` for label-based indexing
- Use `.iloc` for position-based indexing
- Avoid chained indexing (`df['A'][0]`)
- Sort your index when possible for better performance
- Use boolean indexing for filtering
- Consider MultiIndex for hierarchical data
- Use `.query()` for readable complex conditions

## Common Pitfalls
- **SettingWithCopyWarning**: Always use `.loc` when setting values
- **Chained Indexing**: Use `.loc` instead of multiple bracket operations
- **Index Alignment**: Be aware of automatic index alignment in operations
- **Missing Labels**: Handle KeyError when accessing non-existent labels

This comprehensive guide covers the essential aspects of pandas indexing, from basic operations to advanced techniques for efficient data manipulation.