# Sorting algorithms
Before we go into sorting we need to understand about built - in list.sort() and sorted(list)

## 1. Bubble Sort:
It has two goals:
- Put the largest number into the last or the desired position
- Compare two corresponding index items to get the largest number
### Pseudocode
```python
for j= n down to 2:
  for i = 1 to (j-1) #1 indexing:
    if list[i] > list[i+1]:
      then list[i] <--> list[i+1]
    end if
  end for
end for
```
