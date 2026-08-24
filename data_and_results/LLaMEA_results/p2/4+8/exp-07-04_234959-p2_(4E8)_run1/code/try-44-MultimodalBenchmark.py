import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamically shift global minimum with chaotic perturbation
        self.global_min = np.array([2.0 * np.sin(i * 0.5) + 0.5 * np.cos(i * 0.3) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis component with varying radii
        f1 = np.sum((x - self.global_min)**2 / (1.0 + 0.1 * np.abs(x)))
        
        # Trigonometric modulations with varying frequencies and amplitudes
        f2 = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.tan(0.5 * x))
        
        # Step-like function with chaotic transitions
        f3 = np.sum(np.floor(2.0 + 1.5 * np.sin(x)) * np.exp(-0.1 * np.abs(x)))
        
        # Exponential decay with sinusoidal modulation
        f4 = np.sum(np.exp(-0.5 * (x - self.global_min)**2) * (1.0 + 0.3 * np.sin(4.0 * x)))
        
        # Chaotic component using logistic map-like behavior
        f5 = np.sum(np.sin(np.pi * np.sin(x)) * np.cos(np.pi * np.cos(x)))
        
        # Combine all components with optimized weights
        return 0.2 * f1 + 0.25 * f2 + 0.2 * f3 + 0.2 * f4 + 0.15 * f5