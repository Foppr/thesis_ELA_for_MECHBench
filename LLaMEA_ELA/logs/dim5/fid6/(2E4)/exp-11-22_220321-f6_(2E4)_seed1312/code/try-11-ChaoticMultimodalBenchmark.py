import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Polynomial conditioning with exponential growth
        for i in range(self.dim):
            result += (x[i] ** 2) * (1.1 ** i)
            
        # Nested sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            # Primary oscillation
            result += 0.3 * np.sin(2 * np.pi * x[i]) * np.cos(4 * np.pi * x[i])
            # Secondary nested oscillation
            result += 0.1 * np.sin(8 * np.pi * x[i]) * np.cos(16 * np.pi * x[i])
            
        # Cross-dimensional interactions with chaotic behavior
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction scope
                # Chaotic interaction using trigonometric functions
                result += 0.05 * np.sin(10 * x[i] + 5 * x[j]) * np.cos(10 * x[i] - 5 * x[j])
                
        # Non-separable multi-modal component
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (x[i] ** 4) - 8 * (x[i] ** 2) + 16  # Quartic with multiple minima
            
        # Add the multi-modal component with varying weights
        result += 0.2 * multi_modal
        
        # Introduce chaotic behavior through recursive-like interactions
        chaos = 0.0
        for i in range(self.dim):
            if i > 0:
                chaos += 0.01 * np.sin(50 * (x[i] - x[i-1])) * np.cos(25 * (x[i] + x[i-1]))
                
        result += chaos
        
        # Add a complex penalty term that creates multiple local minima
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.5 * ((x[i] - 3.0)**4 + (x[i] + 3.0)**4) + 0.2 * np.sin(20 * x[i])
            
        result += 0.01 * penalty
        
        return result