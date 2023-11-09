import math#if we need to import whole module
result = math.sqrt(16)
print(result)
print(dir(math))#all the function inside maths will be printed

from math import sqrt, pi#if certain function of module is required
ans = sqrt(16)
print(ans)

# from math import * #it'll import whole function of modules
 #as keyword

from math import sqrt as s
res = s(9)
print(res)

from module import wel, app
wel()
print(app)