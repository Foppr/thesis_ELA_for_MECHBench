import numpy as np

class AdaptiveRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis functions with varying widths and centers
        rbfs = []
        centers = np.linspace(-4, 4, min(10, self.dim))
        widths = np.logspace(-1, 1, min(10, self.dim))
        
        for i, (center, width) in enumerate(zip(centers, widths)):
            if i < self.dim:
                rbf = np.exp(-np.sum((x - center)**2) / (2 * width**2))
                rbfs.append(rbf)
        
        # Asymmetric gradient field with directional bias
        grad_field = np.sum((x - 1)**2 * np.sin(x) + (x + 1)**2 * np.cos(x)) / self.dim
        
        # Adaptive noise injection based on input magnitude
        noise_level = 0.1 * (1 + np.mean(np.abs(x)) / 5.0)
        noise = np.random.normal(0, noise_level, self.dim)
        
        # Combine components with dynamic weighting
        rbf_sum = np.sum(rbfs) if rbfs else 0
        total = 0.4 * rbf_sum + 0.3 * grad_field + 0.3 * np.sum(noise**2) / self.dim
        
        return total