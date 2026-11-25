import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with varying degrees
        poly = np.sum((x**3 + 0.5 * x**2 - 2 * x)**2)
        
        # Sinusoidal component with multiple frequencies and amplitudes
        sin_component = 0
        for i in range(self.dim):
            sin_component += np.sin(2**(i+1) * x[i]) * np.cos(3**(i+1) * x[i])
            
        # Radial basis function component with random centers and varying widths
        rbfs = 0
        for i in range(min(5, self.dim)):  # Use at most 5 RBFs
            center = np.random.uniform(-5, 5, self.dim)
            width = np.random.uniform(0.5, 2.0)
            distance = np.sum((x - center)**2)
            rbfs += np.exp(-distance / (2 * width**2))
            
        # Conditioning component with different weights per dimension
        condition = 0
        for i in range(self.dim):
            condition += (i + 1) * x[i]**4
            
        # Noise component to increase robustness testing
        noise = np.random.normal(0, 0.1) * np.sum(np.sin(x)**2)
        
        # Combine all components with appropriate scaling
        return 0.5 * poly + 0.3 * sin_component + 0.2 * rbfs + 0.4 * condition + noise + 10