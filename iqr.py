import numpy as np

def locate_outliers(x):
    media=np.mean(x)
    std=np.std(x)

    z_scores=(x-media)/std
    outliers=np.abs(z_scores) > 3
    outliers_v=x[outliers]

    return outliers, np.sum(outliers),outliers_v

x=np.randn(300,15)

is_outlier,outliers_count,outliers=locate_outliers(x)
