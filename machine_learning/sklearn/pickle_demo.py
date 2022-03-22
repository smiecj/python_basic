import pickle
import pprint

# 序列化
dogs_dict = {'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16}
file_name = "test_pickle"
outfile = open(file_name, 'wb')
pickle.dump(dogs_dict, outfile)
outfile.close()

print("dump success")

# 反序列化
infile = open(file_name, 'rb')
new_dict = pickle.load(infile)
infile.close()

print(type(new_dict))
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(new_dict)

print("load success")

# 序列化 + 压缩
import bz2
import pickle

small_file_name = "smallerfile"
sfile = bz2.BZ2File(small_file_name, 'w')
pickle.dump(dogs_dict, sfile)
sfile.close()

print("dump with bzip success")

sfile = bz2.BZ2File('smallerfile', 'r')
new_dict = pickle.load(sfile)
infile.close()

pp.pprint(new_dict)
print("load with bzip success")

# 序列化方法
import pathos.multiprocessing as mp
from math import cos

p = mp.Pool(2)
# p.map(cos, range(10))
p.map(lambda x: 2**x, range(10))
