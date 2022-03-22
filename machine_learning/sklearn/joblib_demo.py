# 忽略 warning
import warnings
warnings.filterwarnings('ignore')

from sklearn import svm
from sklearn import datasets

# 向量机
# https://xacecask2.gitbooks.io/scikit-learn-user-guide-chinese-version/content/sec1.4.html
clf = svm.SVC()
X, y = datasets.load_iris(return_X_y=True)
clf.fit(X, y)

# 序列化模型
import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(X[0:1])

y[0]

# 打包模型文件
file_name = "sklearn.joblib"
from joblib import dump, load

dump(clf, file_name)
clf = load(file_name)

print("joblib dump and load success")
