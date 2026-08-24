import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic perturbation of global minimum using pseudo-random walk
        np.random.seed(42)
        self.global_min = np.array([(-1)**i * 2.0 + 0.3 * np.random.randn() for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric field with adaptive frequency modulation
        f1 = np.sum(np.sin(2.0 * x + np.cos(x)) * np.cos(1.5 * x + np.sin(x)))
        
        # Adaptive polynomial coupling with dynamic exponents
        exponents = 2 + 0.5 * np.sin(np.arange(self.dim) * np.pi / self.dim)
        f2 = np.sum((x - self.global_min)**exponents)
        
        # Rugged gradient structure with exponential barrier terms
        f3 = np.sum(np.exp(-0.5 * (x - self.global_min)**2) * np.sin(3.0 * x))
        
        # Chaotic interaction terms using logistic map-like dynamics
        f4 = np.sum(np.sin(x * np.sin(x)) + np.cos(x * np.cos(x)))
        
        # Multi-scale sinusoidal interference with varying amplitudes
        f5 = np.sum(np.sin(4.0 * x) * np.cos(2.0 * x) * np.sin(0.5 * x))
        
        # Perturbed global minimum influence with distance-dependent scaling
        dist = np.sqrt(np.sum((x - self.global_min)**2))
        f6 = dist * np.exp(-0.1 * dist)
        
        # Combine all components with chaotic weight scaling
        weights = np.abs(np.sin(np.arange(6) * np.pi / 6)) + 0.5
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4 + weights[4] * f5 + weights[5] * f6