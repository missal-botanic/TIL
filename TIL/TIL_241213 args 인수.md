

### 1. 위치 인수를 함수에 전달하면, 함수 내 위치 매개변수와 일치한다.

위치 인수는 함수 호출 시 순서대로 매개변수에 할당됩니다.

```python
def example(a, b):
    print(f'a: {a}, b: {b}')

# 함수 호출: 위치 인수 1과 2를 순서대로 a와 b에 전달
example(1, 2)
```

### 출력:
```
a: 1, b: 2
```

### 설명:
- `example(1, 2)`에서 **위치 인수** `1`과 `2`는 함수의 매개변수 `a`와 `b`에 순서대로 할당됩니다.

---

### 2. 튜플 인수를 함수에 전달하면, 함수 내 튜플 매개변수가 있다.

튜플 인수를 함수에 전달할 때, 함수 내에서 이를 **튜플로 받을 수 있습니다**. 이 예시는 튜플을 직접 전달하는 경우입니다.

```python
def print_tuple(t):
    print(f'Tuple: {t}')

# 함수 호출: 튜플 인수를 전달
print_tuple(('apple', 'banana', 'cherry'))
```

### 출력:
```
Tuple: ('apple', 'banana', 'cherry')
```

### 설명:
- `print_tuple(('apple', 'banana', 'cherry'))`에서 **튜플** `('apple', 'banana', 'cherry')`를 함수에 전달하여, **튜플 매개변수** `t`에 할당합니다.

---

### 3. 위치 인수를 함수에 전달하고, 매개변수 *args로 수집하여 튜플 인수로 해석할 수 있다.

**`*args`**는 함수가 **가변 개수의 위치 인수**를 받을 수 있게 해주는 매개변수입니다. 이 매개변수는 전달된 위치 인수들을 **튜플로 모읍니다**.

```python
def collect_args(*args):
    print(f'Positional arguments as tuple: {args}')

# 함수 호출: 여러 개의 위치 인수를 전달
collect_args(1, 2, 3, 4)
```

### 출력:
```
Positional arguments as tuple: (1, 2, 3, 4)
```

### 설명:
- `collect_args(1, 2, 3, 4)`에서 **위치 인수** `1, 2, 3, 4`는 **`*args`**에 의해 **튜플** `(1, 2, 3, 4)`로 수집됩니다.

---

### 4. args라는 튜플 인수를 함수에 전달하여, 위치 매개변수 *args로 분해할 수 있다. 이것은 튜플 매개변수 args 안에 다시 수집된다.

이 예시는 **튜플을 함수로 전달하고**, 그 튜플을 **`*args`**로 분해하여, 각 항목이 **개별 매개변수**로 전달되는 것을 보여줍니다.

```python
def unpack_args(*args):
    print(f'First: {args[0]}, Second: {args[1]}, Third: {args[2]}')

# 튜플을 전달하고, *args로 분해하여 매개변수에 할당
args_tuple = ('apple', 'banana', 'cherry')
unpack_args(*args_tuple)
```

### 출력:
```
First: apple, Second: banana, Third: cherry
```

### 설명:
- `args_tuple = ('apple', 'banana', 'cherry')`라는 튜플을 **`unpack_args(*args_tuple)`**로 전달하면, 튜플 **`args_tuple`**이 **`*args`**로 분해되어 개별 항목들이 각각의 위치 매개변수 `First`, `Second`, `Third`에 할당됩니다.
- 이때 `*args_tuple`은 **언팩(분해)**되어 각 항목들이 **위치 인수**로 함수에 전달됩니다.

---

### 요약:

- **위치 인수**는 함수 정의에 맞게 순서대로 전달되어, 매개변수와 일치합니다.
- **튜플 인수**를 함수에 전달하면, 그 튜플은 함수 내에서 **튜플 매개변수로** 받습니다.
- **`*args`**를 사용하면, 전달된 **위치 인수들을 하나의 튜플로** 모아서 받을 수 있습니다.
- **튜플 인수를 `*args`로 전달하여 분해**할 수 있고, 이때 **각 항목이 개별 위치 매개변수**에 할당됩니다.

이렇게 **`*args`**를 사용하면 함수에서 **가변 개수의 인수를 처리**하거나, **튜플을 언팩하여 개별 인수로 전달**할 수 있어 매우 유용합니다.