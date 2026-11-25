import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with mixed degrees for conditioning
        f1 = np.sum(0.1 * x**6 + 0.5 * x**4 + 0.8 * x**2) / self.dim
        
        # Trigonometric terms creating multiple oscillations
        f2 = np.sum(np.sin(5.0 * x) * np.cos(3.0 * x) * np.exp(-0.1 * np.abs(x))) / self.dim
        
        # Radial basis function component with varying centers and widths
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        f3 = 0.0
        for i in range(min(5, self.dim)):
            if i < len(centers):
                f3 += np.exp(-0.5 * ((x - centers[i]) / (1.0 + 0.2 * i))**2)
        
        # Cross-term interactions with asymmetric coupling
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += (x[i] * x[i+1] * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i+1]))
        
        # Asymmetric saddle points with varying steepness
        f5 = np.sum((x**3 + 0.5 * x**2 - 0.3 * x) * np.exp(-0.2 * np.abs(x))) / self.dim
        
        # Add noise-like perturbations for increased complexity
        f6 = 0.05 * np.sum(np.sin(10.0 * x) * np.cos(7.0 * x) * np.tanh(x))
        
        return f1 + f2 + f3 + f4 + f5 + f6