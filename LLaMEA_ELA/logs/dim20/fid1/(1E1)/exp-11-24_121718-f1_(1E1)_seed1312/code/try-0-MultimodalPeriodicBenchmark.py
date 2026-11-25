import numpy as np

class MultimodalPeriodicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2) / self.dim
        
        # Periodic multimodal component with multiple global minima
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(5 * np.pi * x[i]) * np.exp(-0.1 * (x[i] - 1)**2)
        
        # Additional periodic term to increase complexity
        additional_periodic = 0.0
        for i in range(self.dim):
            additional_periodic += np.cos(3 * np.pi * x[i]) * np.exp(-0.05 * (x[i] + 2)**2)
            
        # Combine terms with different weights to create challenging landscape
        return quadratic + 0.5 * periodic + 0.3 * additional_periodic