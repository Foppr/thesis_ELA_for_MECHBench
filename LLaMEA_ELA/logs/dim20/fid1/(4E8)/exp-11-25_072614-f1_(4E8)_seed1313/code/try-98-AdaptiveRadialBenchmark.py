import numpy as np

class AdaptiveRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic radial basis functions with higher frequency sinusoidal modulation
        rbfs = []
        centers = np.linspace(-4.5, 4.5, min(15, self.dim))
        widths = np.logspace(-1.2, 1.7, min(15, self.dim))
        phases = np.linspace(0, 3*np.pi, min(15, self.dim))
        
        for i, (center, width, phase) in enumerate(zip(centers, widths, phases)):
            if i < self.dim:
                # Enhanced chaotic modulation with cubic and exponential components
                rbf = np.exp(-np.sum((x - center)**2) / (2 * width**2)) * np.sin(phase * np.sum(x - center)**3)
                rbfs.append(rbf)
        
        # Modified asymmetric gradient field with polynomial and hyperbolic components
        grad_field = np.sum((x - 1.5)**4 * np.tanh(x) + (x + 1.5)**4 * np.cosh(x)) / self.dim
        
        # Adaptive noise injection with dynamic scaling based on input magnitude and position
        noise_level = 0.2 * (1 + np.mean(np.abs(x)) / 5.0) * (1 + 0.7 * np.cos(np.sum(x**2)))
        noise = np.random.normal(0, noise_level, self.dim)
        
        # Combine components with adjusted weighting based on input characteristics
        rbf_sum = np.sum(rbfs) if rbfs else 0
        total = 0.4 * rbf_sum + 0.3 * grad_field + 0.3 * np.sum(noise**2) / self.dim
        
        # Add novel cross-term interaction components for increased complexity
        cross_terms = np.sum((x[i] - x[(i+1)%self.dim])**2 * np.sin(x[i] * x[(i+1)%self.dim]) for i in range(self.dim))
        
        return total + 0.1 * cross_terms