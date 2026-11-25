import numpy as np

class AdaptiveRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic radial basis functions with exponential decay and sinusoidal modulation
        rbfs = []
        centers = np.linspace(-4, 4, min(12, self.dim))
        widths = np.logspace(-1, 1.5, min(12, self.dim))
        phases = np.linspace(0, 2*np.pi, min(12, self.dim))
        
        for i, (center, width, phase) in enumerate(zip(centers, widths, phases)):
            if i < self.dim:
                # Add chaotic modulation to the radial basis
                rbf = np.exp(-np.sum((x - center)**2) / (2 * width**2)) * np.sin(phase * np.sum(x - center))
                rbfs.append(rbf)
        
        # Asymmetric gradient field with polynomial and trigonometric components
        grad_field = np.sum((x - 1)**3 * np.sin(x) + (x + 1)**3 * np.cos(x)) / self.dim
        
        # Dynamic noise injection with chaotic scaling based on input magnitude and position
        noise_level = 0.15 * (1 + np.mean(np.abs(x)) / 5.0) * (1 + 0.5 * np.sin(np.sum(x)))
        noise = np.random.normal(0, noise_level, self.dim)
        
        # Combine components with dynamic weighting based on input characteristics
        rbf_sum = np.sum(rbfs) if rbfs else 0
        total = 0.35 * rbf_sum + 0.35 * grad_field + 0.3 * np.sum(noise**2) / self.dim
        
        return total