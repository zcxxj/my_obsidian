
### GPT-o3生成
```python
"""  
Please run on jupyter notebook  
  
Interactive 3-D joint PDF visualizer for two random variables (X, Y).  
  
Author : ChatGPT (July 21 2025)  
---------------------------------------------------------------  
- Choose marginal distributions for X and Y from dropdowns.  
- For (Normal, Normal) pair, adjust correlation ρ (covariance) with a slider.  
- Click “Update Plot” to redraw a Plotly surface of the joint PDF.  
---------------------------------------------------------------  
"""  
  
import numpy as np  
import scipy.stats as stats  
import plotly.graph_objects as go  
import ipywidgets as widgets  
from IPython.display import display, clear_output  
  
# ------------------------------------------------------------------  
# 1. Distribution registry  ——  add more items here if needed  
# ------------------------------------------------------------------  
DIST_REGISTRY = {  
    "Normal (μ=0, σ=1)": dict(  
        pdf=lambda x: stats.norm.pdf(x, 0, 1),  
        support=(-4, 4),  
        is_normal=True,  
    ),  
    "Uniform (a=-1, b=1)": dict(  
        pdf=lambda x: stats.uniform.pdf(x, -1, 2),  # width 2  
        support=(-1.2, 1.2),  
        is_normal=False,  
    ),  
    "Exponential (λ=1)": dict(  
        pdf=lambda x: stats.expon.pdf(x, 0, 1),  
        support=(0, 6),  
        is_normal=False,  
    ),  
}  
  
# ------------------------------------------------------------------  
# 2. Widgets  
# ------------------------------------------------------------------  
x_dist_dd = widgets.Dropdown(options=list(DIST_REGISTRY.keys()), description="X dist")  
y_dist_dd = widgets.Dropdown(options=list(DIST_REGISTRY.keys()), description="Y dist")  
rho_slider = widgets.FloatSlider(  
    value=0.0,  
    min=-0.95,  
    max=0.95,  
    step=0.05,  
    description="ρ (N×N)",  
    continuous_update=False,  
)  
update_btn = widgets.Button(description="Update Plot", button_style="success")  
  
# Output area for the plot  
plot_out = widgets.Output()  
  
  
# ------------------------------------------------------------------  
# 3. Core drawing routine  
# ------------------------------------------------------------------  
def draw_surface(x_dist_name, y_dist_name, rho):  
    """Compute grid & joint pdf, then draw a 3-D surface."""  
    # Look up distribution metadata  
    xd = DIST_REGISTRY[x_dist_name]  
    yd = DIST_REGISTRY[y_dist_name]  
  
    # Build grid — use union of supports, 60 × 60 points  
    x_min, x_max = xd["support"]  
    y_min, y_max = yd["support"]  
    x = np.linspace(x_min, x_max, 60)  
    y = np.linspace(y_min, y_max, 60)  
    X, Y = np.meshgrid(x, y)  
  
    # Case 1 : Both Normal → use bivariate normal with correlation ρ  
    if xd["is_normal"] and yd["is_normal"]:  
        det = 1 - rho**2  
        coeff = 1 / (2 * np.pi * np.sqrt(det))  
        Z = coeff * np.exp(-(X**2 - 2 * rho * X * Y + Y**2) / (2 * det))  
        title = f"Bivariate Normal (ρ = {rho:.2f})"  
    else:  
        # Case 2 : treat as independent  
        fx = xd["pdf"](X)  
        fy = yd["pdf"](Y)  
        Z = fx * fy  
        title = "Assumed independent (ρ ignored)"  
  
    # Plotly surface  
    fig = go.Figure(  
        data=go.Surface(x=X, y=Y, z=Z, colorscale="Viridis", showscale=False)  
    )  
    fig.update_layout(  
        title=title,  
        scene=dict(  
            xaxis_title="X",  
            yaxis_title="Y",  
            zaxis_title="Joint PDF",  
            camera=dict(eye=dict(x=1.3, y=1.3, z=0.8)),  
        ),  
        margin=dict(l=0, r=0, b=0, t=30),  
    )  
    return fig  
  
  
# ------------------------------------------------------------------  
# 4. Callback  
# ------------------------------------------------------------------  
def on_update_clicked(_):  
    with plot_out:  
        clear_output(wait=True)  
        fig = draw_surface(x_dist_dd.value, y_dist_dd.value, rho_slider.value)  
        fig.show(renderer="notebook")  
  
update_btn.on_click(on_update_clicked)  
  
# Disable / enable ρ slider automatically  
def toggle_rho_slider(*_):  
    both_normal = (  
        DIST_REGISTRY[x_dist_dd.value]["is_normal"]  
        and DIST_REGISTRY[y_dist_dd.value]["is_normal"]  
    )  
    rho_slider.disabled = not both_normal  
    rho_slider.description = "ρ (N×N)" if both_normal else "ρ (disabled)"  
  
x_dist_dd.observe(toggle_rho_slider, names="value")  
y_dist_dd.observe(toggle_rho_slider, names="value")  
  
# ------------------------------------------------------------------  
# 5. Show UI  
# ------------------------------------------------------------------  
ui = widgets.VBox(  
    [  
        widgets.HBox([x_dist_dd, y_dist_dd, rho_slider, update_btn]),  
        plot_out,  
    ]  
)  
  
display(ui)  
  
# Trigger initial plot  
on_update_clicked(None)
```

### claude生成
```python
import numpy as np  
import matplotlib.pyplot as plt  
from matplotlib import cm  
from matplotlib.widgets import Slider, RadioButtons, TextBox  
from mpl_toolkits.mplot3d import Axes3D  
from scipy import stats  
  
  
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 或者 'Microsoft YaHei'，用于显示中文  
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号  
  
  
class JointDistributionVisualizer:  
    def __init__(self):  
        # 初始化参数  
        self.x_dist = 'normal'  
        self.y_dist = 'normal'  
        self.covariance = 0.5  
        self.x_params = {'loc': 0, 'scale': 1}  
        self.y_params = {'loc': 0, 'scale': 1}  
  
        # 创建图形和子图  
        self.fig = plt.figure(figsize=(12, 9))  
  
        # 3D图形子图  
        self.ax_3d = self.fig.add_subplot(111, projection='3d', position=[0.1, 0.3, 0.6, 0.65])  
  
        # 初始化绘图  
        self.update_plot()  
  
        # 创建控件  
        self.create_widgets()  
  
    def create_widgets(self):  
        # X分布选择  
        ax_x_dist = plt.axes([0.05, 0.15, 0.15, 0.1])  
        self.radio_x = RadioButtons(ax_x_dist, ('normal', 'uniform', 'exponential'))  
        self.radio_x.on_clicked(self.update_x_dist)  
  
        # Y分布选择  
        ax_y_dist = plt.axes([0.25, 0.15, 0.15, 0.1])  
        self.radio_y = RadioButtons(ax_y_dist, ('normal', 'uniform', 'exponential'))  
        self.radio_y.on_clicked(self.update_y_dist)  
  
        # 协方差输入框  
        ax_cov = plt.axes([0.5, 0.15, 0.1, 0.04])  
        self.text_cov = TextBox(ax_cov, '协方差:', initial=str(self.covariance))  
        self.text_cov.on_submit(self.update_covariance)  
  
        # X分布参数滑块  
        ax_x_loc = plt.axes([0.75, 0.2, 0.2, 0.03])  
        ax_x_scale = plt.axes([0.75, 0.15, 0.2, 0.03])  
        self.slider_x_loc = Slider(ax_x_loc, 'X均值', -5, 5, valinit=0)  
        self.slider_x_scale = Slider(ax_x_scale, 'X标准差', 0.1, 3, valinit=1)  
        self.slider_x_loc.on_changed(self.update_params)  
        self.slider_x_scale.on_changed(self.update_params)  
  
        # Y分布参数滑块  
        ax_y_loc = plt.axes([0.75, 0.1, 0.2, 0.03])  
        ax_y_scale = plt.axes([0.75, 0.05, 0.2, 0.03])  
        self.slider_y_loc = Slider(ax_y_loc, 'Y均值', -5, 5, valinit=0)  
        self.slider_y_scale = Slider(ax_y_scale, 'Y标准差', 0.1, 3, valinit=1)  
        self.slider_y_loc.on_changed(self.update_params)  
        self.slider_y_scale.on_changed(self.update_params)  
  
        # 添加文字说明  
        self.fig.text(0.05, 0.26, 'X分布类型:', fontsize=10)  
        self.fig.text(0.25, 0.26, 'Y分布类型:', fontsize=10)  
        self.fig.text(0.45, 0.2, '协方差范围: [-1, 1]', fontsize=9)  
  
    def get_distribution(self, dist_type, params):  
        """根据分布类型返回相应的分布对象"""  
        if dist_type == 'normal':  
            return stats.norm(loc=params['loc'], scale=params['scale'])  
        elif dist_type == 'uniform':  
            return stats.uniform(loc=params['loc'] - params['scale'], scale=2 * params['scale'])  
        elif dist_type == 'exponential':  
            return stats.expon(loc=params['loc'], scale=params['scale'])  
  
    def generate_joint_distribution(self):  
        """生成联合分布数据"""  
        # 生成网格点  
        x_range = np.linspace(-5, 5, 50)  
        y_range = np.linspace(-5, 5, 50)  
        X, Y = np.meshgrid(x_range, y_range)  
  
        # 获取边缘分布  
        x_dist = self.get_distribution(self.x_dist, self.x_params)  
        y_dist = self.get_distribution(self.y_dist, self.y_params)  
  
        # 使用Copula方法生成相关性  
        # 这里使用高斯Copula来引入相关性  
        n_samples = 100000  
  
        # 生成相关的均匀分布  
        mean = [0, 0]  
        cov_matrix = [[1, self.covariance], [self.covariance, 1]]  
  
        # 生成相关的正态分布样本  
        samples = np.random.multivariate_normal(mean, cov_matrix, n_samples)  
  
        # 转换为均匀分布  
        u1 = stats.norm.cdf(samples[:, 0])  
        u2 = stats.norm.cdf(samples[:, 1])  
  
        # 通过逆变换得到目标分布  
        x_samples = x_dist.ppf(u1)  
        y_samples = y_dist.ppf(u2)  
  
        # 计算2D直方图作为联合密度的近似  
        Z, x_edges, y_edges = np.histogram2d(x_samples, y_samples, bins=50,  
                                             range=[[-5, 5], [-5, 5]], density=True)  
  
        # 调整网格以匹配直方图边缘  
        X_hist = (x_edges[:-1] + x_edges[1:]) / 2  
        Y_hist = (y_edges[:-1] + y_edges[1:]) / 2  
        X_hist, Y_hist = np.meshgrid(X_hist, Y_hist)  
  
        return X_hist, Y_hist, Z.T  
  
    def update_plot(self):  
        """更新3D图形"""  
        self.ax_3d.clear()  
  
        # 生成联合分布  
        X, Y, Z = self.generate_joint_distribution()  
  
        # 绘制3D表面  
        surf = self.ax_3d.plot_surface(X, Y, Z, cmap=cm.viridis,  
                                       linewidth=0, antialiased=True, alpha=0.8)  
  
        # 添加等高线投影  
        self.ax_3d.contour(X, Y, Z, zdir='z', offset=0, cmap=cm.viridis, alpha=0.5)  
  
        # 设置标签和标题  
        self.ax_3d.set_xlabel('X')  
        self.ax_3d.set_ylabel('Y')  
        self.ax_3d.set_zlabel('联合概率密度')  
        self.ax_3d.set_title(f'联合分布: X~{self.x_dist}, Y~{self.y_dist}, Cov={self.covariance:.2f}')  
  
        # 设置视角  
        self.ax_3d.view_init(elev=20, azim=45)  
  
        plt.draw()  
  
    def update_x_dist(self, label):  
        """更新X分布类型"""  
        self.x_dist = label  
        self.update_plot()  
  
    def update_y_dist(self, label):  
        """更新Y分布类型"""  
        self.y_dist = label  
        self.update_plot()  
  
    def update_covariance(self, text):  
        """更新协方差"""  
        try:  
            cov = float(text)  
            if True :  
                self.covariance = cov  
                self.update_plot()  
            else:  
                print("协方差必须在[-1, 1]范围内")  
                self.text_cov.set_val(str(self.covariance))  
        except ValueError:  
            print("请输入有效的数字")  
            self.text_cov.set_val(str(self.covariance))  
  
    def update_params(self, val):  
        """更新分布参数"""  
        self.x_params['loc'] = self.slider_x_loc.val  
        self.x_params['scale'] = self.slider_x_scale.val  
        self.y_params['loc'] = self.slider_y_loc.val  
        self.y_params['scale'] = self.slider_y_scale.val  
        self.update_plot()  
  
    def show(self):  
        """显示图形"""  
        plt.show()  
  
  
# 创建并显示可视化  
if __name__ == "__main__":  
    visualizer = JointDistributionVisualizer()  
    visualizer.show()
```