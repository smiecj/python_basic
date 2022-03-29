import matplotlib.pyplot as plt
import plotly.tools as tls
import plotly.offline as offline

# %matplotlib inline

data = {
    'time': [1, 2, 3],
    'name': ['hi', 'hello', 'ho']
}

fig, ax = plt.subplots()
ax.plot(data['time'], data["name"])
plt.show()  # 用 matplot 画图

offline.iplot_mpl(fig)  # 用 plotly 转换为交互式绘图