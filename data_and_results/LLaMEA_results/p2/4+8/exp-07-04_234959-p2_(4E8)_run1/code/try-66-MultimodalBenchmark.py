import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamically shift global minimum with chaotic perturbation
        self.global_min = np.array([2.5 * np.sin(i * 0.5) + 1.0 for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis component with variable scaling
        r = np.sqrt(np.sum((x - self.global_min)**2))
        f1 = r * (1.0 + 0.2 * np.sin(r))
        
        # Trigonometric modulations with varying frequencies
        f2 = np.sum(np.sin(2.0 * x + np.cos(x)) * np.cos(1.5 * x + np.sin(x)))
        
        # Logarithmic penalty with adaptive base
        f3 = np.sum(np.log(1.0 + 0.5 * np.abs(x)) * (1.0 + 0.1 * np.sin(3.0 * x)))
        
        # Hyperbolic component for increased complexity
        f4 = np.sum(np.tanh(x) * np.exp(-0.5 * x**2))
        
        # Chaotic sine composition with phase modulation
        f5 = np.sum(np.sin(np.pi * np.sin(x)) * np.cos(np.pi * np.cos(x)))
        
        # Combine all components with optimized weights
        return 0.2 * f1 + 0.25 * f2 + 0.2 * f3 + 0.2 * f4 + 0.15 * f5