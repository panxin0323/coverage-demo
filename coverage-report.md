# Diff Coverage
## Diff: main...HEAD, staged and unstaged changes

- myapp/calc&#46;py (50.0%): Missing lines 7
- myapp/utils&#46;py (25.0%): Missing lines 9-10,12

## Summary

- **Total**: 6 lines
- **Missing**: 4 lines
- **Coverage**: 33%



## myapp/calc&#46;py

Lines 3-7

```python
  3 
  4 def mul(a: int, b: int) -> int:
  5     return a * b
  6 def sub(a, b):
! 7     return a - b
```


---



## myapp/utils&#46;py

Lines 5-12

```python
   5     if not name:
   6         return "Hello guest"
   7     return f"Hello {name}"
   8 def max2(a, b):
!  9     if a > b:
! 10         return a
  11     else:
! 12         return b
```


---


