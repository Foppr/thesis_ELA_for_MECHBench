import numpy as np

class AdaptiveRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic radial basis functions with modified exponential decay and frequency modulation
        rbfs = []
        centers = np.linspace(-4.5, 4.5, min(15, self.dim))
        widths = np.logspace(-1.2, 1.8, min(15, self.dim))
        frequencies = np.linspace(1.0, 3.0, min(15, self.dim))
        
        for i, (center, width, freq) in enumerate(zip(centers, widths, frequencies)):
            if i < self.dim:
                # Enhanced chaotic modulation with frequency scaling
                rbf = np.exp(-np.sum((x - center)**2) / (2 * width**2)) * np.sin(freq * np.sum(x - center) + np.sum(x**2) / 10.0)
                rbfs.append(rbf)
        
        # Modified asymmetric gradient field with higher-order polynomial and trigonometric components
        grad_field = np.sum((x - 1.5)**4 * np.cos(x) + (x + 1.5)**4 * np.sin(x)) / self.dim
        
        # Adaptive noise injection with dynamic scaling based on input magnitude, position, and dimensionality
        noise_level = 0.2 * (1 + np.mean(np.abs(x)) / 5.0) * (1 + 0.3 * np.sin(np.sum(x) * 0.5)) * np.log(self.dim + 1)
        noise = np.random.normal(0, noise_level, self.dim)
        
        # Combine components with updated weighting and normalization
        rbf_sum = np.sum(rbfs) if rbfs else 0
        total = 0.4 * rbf_sum + 0.3 * grad_field + 0.3 * np.sum(noise**2) / self.dim
        
        return total