# Unified Random
A Random function that works the same way across different programming languages.

Calling the function with the same seed set will return the set of numbers, regardless of the programming language or architecture used.


## Why?

In case you need to generate certain set of numbers the same way in different software elements. For example, if your backend server is in Python and your client-side is written in JavaScript, you can use this package to produce the same outputs on both sides.

## Languages currently supported
- JavaScript
- Python3
- C#

C/C++ and PHP implementations are under developement

## How to use
1. Create an instance of class UnifiedRandom and provide seed in constructor. If you do not enter any seed, it will be automatically genereted from your system's datatime.
```
const urandom = new UnifiedRandom("abcd");
```

2. Call GetNumber(int min, int max) or GetValue() function:
```
const randomNumber = urandom.getNumber(4, 24);
// randomNumber <- 15
const randomValue = urandom.getValue();
// randomValue <- 0.5608629047637805
```

getNumber(int min, int max) returns a random number (integer) from given range (min, max).
Both min are max must be of integer type.

getValue() returns a random value from 0 (inclusive) to 1 (inclusive).


## Tests
Several test have been carried out to ensure that the function returns approximately random numbers, spread evenly without any bias.

Here are results from test of 500,000 random numbers (min = 0, max = 3):
```
seed = seed_test
500,000 random numbers (min = 0, max = 3):
Average number: 1.500126
Output 0: 125043 times.
Output 1: 124846 times.
Output 2: 125243 times.
Output 3: 124741 times.
```

## Pseudocode
```
Function GetSignValue(sign)
    If sign == '0' return (1/16)/2
    If sign == '1' return (1/16 + 2/16)/2
    If sign == '2' return (2/16 + 3/16)/2
    If sign == '3' return (3/16 + 4/16)/2
    …
    If sign == 'e' return (14/16 + 15/16)/2
    If sign == 'f' return (15/16 + 16/16)/2

Function GetValue()
    toHash = seed + "-" + index
    hash = Hash(toHash)
    value = 0
    For i = 0..8
        sign = hash[i]
        signValue = GetSignValue(sign)
        
        If i == 0
            value = signValue
        Else
            delta = 1
            For j = 0..i
                delta = delta/16
            If GetSignValue(hash[15 – i]) < 0.5
                value = value – signValue * delta
            Else
                value = value – signValue \* delta
                If value < 0
                    value = 0
                If value > 1
                    value = 1
    
    index = index + 1
    return value

Function GetNumber(min, max)
    value = GetValue()
    intervals = max – min + 1
    return Floor(intervals \* value)
```
_Where:_
_Hash(string)_ is a function that returns hashed string (using sha256)

_Floor(number)_ is a function that rounds down number and returns the largest integer less than or equal to a given number

## Changelog
### 1.01
- Added type verification and automatic type repairs to supported untyped languages (JavaScript, Python3)
- Improved performance by reducing redundant calculations
- Fixed bug with wrong range return in GetNumber(min, max) function

## Author

Michal Obara (@mobaradev)
[mobaradev@yahoo.com](mailto:mobaradev@yahoo.com)
http://www.mobaradev.com

## License

The MIT License

Copyright 2023 Michal Obara (mobaradev)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
