# SPDX-License-Identifier: Apache-2.0

my_list = [1,2,3]
s = set([1,2,3])
d = {"one": 1, "two": 2}
t = (1,2,3)

# range, enumerate, filter, map, zip
# https://docs.python.org/3.7/library/functions.html
# Topics to research: Iterable, iterator, generator

from pxr import Vt, Gf

for i, x in enumerate(my_list):
    print(i, x)

for x in Gf.Vec3f([1,2,3]):
    print(x)

my_usd_arr = Vt.BoolArray([False, True, False])
print(type(my_usd_arr))
for x in my_usd_arr:
    print(x)

for i, x in Vt.BoolArray([False, True, False]):
    print(i, x)

class PowTwo:
    num = 1
    def __iter__(self):
        return self
    
    def __next__(self):
        self.num = self.num * 2
        if self.num > 32:
            raise StopIteration()
        return self.num

pow2 = PowTwo()

# for x in pow2:
#     print(x)

print(next(pow2))
print(next(pow2))
print(next(pow2))
print(next(pow2))
print(next(pow2))
print(next(pow2))
print(next(pow2))