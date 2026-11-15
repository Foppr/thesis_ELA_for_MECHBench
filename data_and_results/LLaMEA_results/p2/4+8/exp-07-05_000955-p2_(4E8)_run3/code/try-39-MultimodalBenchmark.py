import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        f1 = np.sum(x**2)
        
        # Multiple sinusoidal components with varying frequencies and amplitudes
        f2 = 0.2 * np.sum(np.sin(10.0 * x) * np.cos(5.0 * x))
        
        # Chaotic sine-wave interactions
        f3 = 0.15 * np.sum(np.sin(7.0 * x) * np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Radial gradient component with non-linear curvature
        f4 = 0.05 * np.sum((x**2) * np.sin(5.0 * np.sqrt(np.sum(x**2))))
        
        # Additional penalty term for global convergence
        f5 = 0.02 * np.sum(np.abs(x)**1.5)
        
        # Add a small perturbation to avoid degeneracy
        f6 = 0.01 * np.sum(np.sin(15.0 * x) * np.cos(8.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6