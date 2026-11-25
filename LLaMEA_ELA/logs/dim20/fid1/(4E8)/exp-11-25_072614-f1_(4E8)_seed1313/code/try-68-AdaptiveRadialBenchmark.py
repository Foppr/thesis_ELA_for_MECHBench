import numpy as np

class AdaptiveRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic radial basis functions with exponential decay and varying centers
        rbfs = []
        centers = np.sin(np.linspace(0, np.pi, min(15, self.dim))) * 4.0
        widths = np.logspace(-2, 1.5, min(15, self.dim))
        
        for i, (center, width) in enumerate(zip(centers, widths)):
            if i < self.dim:
                # Add chaotic modulation to the radial distance
                chaotic_factor = 1 + 0.3 * np.sin(x[i] * np.pi / 2)
                rbf = np.exp(-np.sum((x - center)**2) / (2 * width**2 * chaotic_factor))
                rbfs.append(rbf)
        
        # Dynamic gradient field with time-varying directional bias
        t = np.sum(x**2) / self.dim
        grad_field = np.sum(np.sin(x + t) * np.cos(x - t)) / self.dim
        
        # Time-varying noise injection with adaptive amplitude and frequency
        noise_level = 0.15 * (1 + np.mean(np.abs(x)) / 5.0) * (1 + 0.2 * np.sin(t))
        noise_freq = 2 + 3 * np.cos(t)
        noise = np.random.normal(0, noise_level, self.dim)
        noise = noise * np.sin(noise_freq * x)
        
        # Polynomial saddle point terms with dynamic scaling
        saddle_terms = []
        for i in range(min(5, self.dim)):
            saddle_terms.append((x[i]**4 - 2*x[i]**2 + 1) * np.cos(x[i]))
        saddle_sum = np.sum(saddle_terms) if saddle_terms else 0
        
        # Combine all components with dynamic weighting
        rbf_sum = np.sum(rbfs) if rbfs else 0
        total = 0.35 * rbf_sum + 0.25 * grad_field + 0.2 * saddle_sum + 0.2 * np.sum(noise**2) / self.dim
        
        return total