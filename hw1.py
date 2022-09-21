import numpy as np
import matplotlib.pyplot as plt
import os
ROOT_DIR = os.getcwd()
FILES_DIR = ROOT_DIR + '\data'
IMAGES_PATH = os.path.join(ROOT_DIR, "images")
os.makedirs(IMAGES_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

plt.style.use('seaborn')

pms = np.array([0,0.1,0.2,0.3,0.5])

def time_scale(pm, pl):
    sigma = 0.25
    p0 = 556.25
    b = 556
    a = 556.5
    gamma = 3
    pu = 1 - pm - pl
    const = (0.5*(a-b))**2
    var = const * (pu+pl-(pu-pl)**2)
    std = np.sqrt(var)

    T = (std/(sigma*p0))**(gamma)
    return T

pm = 0


def plot_T():
    fig, ax = plt.subplots(nrows=5,ncols=1,figsize=(12,12))
    fig.suptitle("Time Scale plots for asset under question when $\gamma=3$", fontsize = 18)
    for i in range(5):
        pm = pms[i]
        x = np.arange(0,1.01-pm,0.01)
        y = time_scale(pm,x)
        ax[i].plot(x,y, label = '$p_m=${}'.format(pm))
        ax[i].set_xlim(0,1)
        ax[i].set_xlabel('$p_l$', fontsize = 14)
        ax[i].set_ylabel('$T_*$', fontsize = 14)
        ax[i].set_title('Plot of $T_*$ when $p_m$={}'.format(pm), fontsize = 16)
    save_fig('hw1_q5'.format(pm))
    plt.show()


plot_T()
