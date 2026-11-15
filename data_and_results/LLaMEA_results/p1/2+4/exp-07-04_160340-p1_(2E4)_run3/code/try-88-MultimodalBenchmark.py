import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        base = np.sum(x**2)
        
        # Periodic sinusoidal modulation with varying frequencies
        periodic = 0.0
        for i in range(self.dim):
            freq = 2.0 * (i + 1)
            periodic += np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Exponential decay terms with random centers
        decay = 0.0
        np.random.seed(42 + self.dim)  # For reproducibility
        centers = np.random.uniform(-5.0, 5.0, self.dim)
        for i in range(self.dim):
            decay += np.exp(-0.5 * ((x[i] - centers[i]) / (0.5 * (i + 1)))**2)
        
        # Asymmetric global minima distribution
        asymmetry = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                asymmetry += (x[i] - 2.0)**2
            else:
                asymmetry += (x[i] + 2.0)**2
        
        # Add a nested structure with multiple local optima
        nested = 0.0
        for i in range(self.dim):
            nested += np.sin(10 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Combine all components
        result = base + 0.5 * periodic + 0.3 * decay + 0.2 * asymmetry + 0.1 * nested
        
        return result