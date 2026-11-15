import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos component with mixed degrees
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x_norm[i]**4 - 2*x_norm[i]**2 + 1) * np.cos(x_norm[i])
        
        # Logarithmic barrier interactions
        log_barrier = 0.0
        for i in range(self.dim):
            log_barrier += -np.log(1e-10 + np.abs(x_norm[i]))
        
        # Quantum-inspired oscillatory terms
        quantum = 0.0
        for i in range(self.dim):
            quantum += np.sin(2 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
        
        # Cross-terms with exponential coupling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(x_norm[i] * x_norm[j])
        
        # Radial polynomial with multiple local minima
        r = np.sqrt(np.sum(x_norm**2))
        radial_poly = 0.5 * r**4 - r**2 + 0.25
        
        # Combine all components
        return 0.3 * poly_chaos + 0.25 * log_barrier + 0.2 * quantum + 0.15 * cross + 0.1 * radial_poly