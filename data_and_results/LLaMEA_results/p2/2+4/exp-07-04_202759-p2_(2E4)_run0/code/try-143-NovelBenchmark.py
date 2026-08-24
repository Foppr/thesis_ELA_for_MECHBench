import numpy as np

class NovelBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sine-based periodic component with varying frequencies and amplitudes
        periodic = np.sum(np.sin(10 * x) * np.cos(7 * x) * np.exp(-0.1 * x**2))
        
        # Asymmetric quadratic bowl with shifted centers
        bowl = np.sum((x - 2.0)**2 + 0.5 * (x + 1.5)**2)
        
        # Saddle-point structure with coupled cross-terms
        saddle = 0
        for i in range(self.dim - 1):
            j = (i + 1) % self.dim
            saddle += (x[i]**2 - x[j]**2) * np.sin(0.5 * (x[i] + x[j]))
        
        # Multi-scale oscillatory component with fractal-like behavior
        oscillatory = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(3.0 * x[i])
            oscillatory += np.sin(freq * x[i]) * np.cos(freq * x[i] * 2.0) * np.exp(-0.05 * x[i]**2)
        
        # Asymmetric exponential decay component
        exp_decay = np.sum(np.exp(-0.5 * (x - 1.0)**2) * np.sin(2.0 * x) * np.cos(1.5 * x))
        
        # Cross-dimensional interaction with varying coupling strength
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range coupling
                coupling += (x[i] * x[j]) * np.sin(0.3 * (x[i] - x[j])**2)
        
        # Combine components with adaptive weights
        return 0.4 * periodic + 0.3 * bowl + 0.15 * saddle + 0.1 * oscillatory + 0.05 * exp_decay + 0.05 * coupling