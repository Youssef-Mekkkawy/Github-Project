# Simple Size (File Size) Convert.

> # Calculation Method.
> 
> ### Binary Calculation.
> 
> $$
> i = {log _{1024} \left(Size\right)} \newline 
>p = 1024^2 \newline
>s = Size/p \newline
> > $$
> 
> ### Decimal Calculation.
> 
> > $$
> > i = {log _{1000} \left(Size\right)} \newline 
p = 1000^2 \newline
s = Size/p \newline



> > $$

### 

## (1) - Imports

```python
import math
```

## (2) - Calculation Function.

    

> ## This Function Convert Byte To KB, MB, GB, etc...
> 
> ```python
> def Calulation(self, size_bytes:int, Type:int = 1000 | 1024) -> tuple:
>     i = int(math.floor(math.log(size_bytes, Type)))
>     p = math.pow(Type, i)
>     size = round(size_bytes / p, 2) #round(Size,Number Digits After Dot)
>         
>     # Decimal
>     if Type == 1000:
>         return size, self.size_name_decimal[i]
>     # Binary
>     elif Type == 1024:
>         return size, self.size_name_binary[i]
> 
>     else:
>         return "Please Use Decimal-> {1000} or Binary-> {1024}"
> 
> ```
> 
> ## 
> 
> ## This Function Convert KB, MB, GB, etc... To Byte.
> 
> ```python
> def Bytes_Calulation(self, size_bytes:int, UNIT:str = "B", Type:int = 1000 | 1024):
>     UNIT = UNIT.upper()
> 
>     if UNIT in self.size_name_binary or UNIT in self.size_name_decimal:
> 
>         if UNIT in self.B:
>             i = 0
>             
>         elif UNIT in self.K:
>             i = 1
> 
>         elif UNIT in self.M:
>             i = 2
> 
>         elif UNIT in self.G:
>             i = 3
> 
>         elif UNIT in self.T:
>             i = 4
> 
>         elif UNIT in self.P:
>             i = 5
> 
>         else:
>             return "Unit Not Supported."
> 
>     else:
>         return "Unit Not Supported."
> 
>     p = math.pow(Type, i)
>     s = size_bytes * p
>     size = round(s, 2   
>     if Type == 1000:
>         return size, self.size_name_decimal[0   
>     elif Type == 1024:
>         return size, self.size_name_binary[0    
>     else:
>         return "Please Use Decimal-> {1000} or Binary-> {1024}"
> ```
