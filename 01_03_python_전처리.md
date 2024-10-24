
```
import numpy as np

### 1차원 배열 생성
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

### 배열을 10x1 형태로 재구성
reshaped_arr = arr.reshape(-1, 1)

print(reshaped_arr)
```

```
[[ 1]
 [ 2]
 [ 3]
 [ 4]
 [ 5]
 [ 6]
 [ 7]
 [ 8]
 [ 9]
 [10]]
 ```
