import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Time-varying global minimum with chaotic perturbation
        np.random.seed(42)
        self.global_min = np.random.uniform(-5.0, 5.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical base term with adaptive scaling
        f1 = np.sum((x - self.global_min)**2)
        
        # Sinusoidal modulation with varying frequency
        f2 = np.sum(np.sin(2.0 * np.pi * x) * np.cos(1.5 * np.pi * x))
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        f3 = np.exp(-0.1 * r) * np.sin(3.0 * r)
        
        # Chaotic coupling via nested trigonometric functions
        f4 = np.sum(np.sin(np.cos(x)) * np.cos(np.sin(x)))
        
        # Dynamic noise component
        noise = np.random.normal(0, 0.1, self.dim)
        f5 = np.sum(noise * x)
        
        # Polynomial cross-terms with chaotic coefficients
        f6 = np.sum(x**4 - 10 * x**2 + 5 * x)
        
        # Combine all components with varying weights
        return 0.2 * f1 + 0.2 * f2 + 0.15 * f3 + 0.15 * f4 + 0.15 * f5 + 0.15 * f6