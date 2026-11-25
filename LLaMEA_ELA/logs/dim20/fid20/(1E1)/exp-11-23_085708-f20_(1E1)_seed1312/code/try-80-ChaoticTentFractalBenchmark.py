import numpy as np

class ChaoticTentFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Tent map chaotic component
        tent = 0.0
        for i in range(self.dim):
            tent += np.abs(x_scaled[i] - 0.5) * (1 - 2 * np.abs(x_scaled[i] - 0.5))
        
        # Polynomial interaction terms with varying degrees
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i]**3 + x[j]**2) * (x[i] * x[j])**2
        
        # Fractal-like recursive sine modulation
        fractal = 0.0
        for i in range(self.dim):
            temp = x[i]
            for k in range(5):  # 5 levels of recursion
                temp = np.sin(temp * (k + 1))
            fractal += temp**2
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(x[i] * x[j])
        
        # Hyperbolic tangent landscape with multiple peaks
        tanh_term = 0.0
        for i in range(self.dim):
            tanh_term += np.tanh(3 * x[i]) + 0.5 * np.tanh(6 * x[i])**2
        
        # Add a global scaling factor based on dimensionality
        dim_factor = 1.0 + 0.1 * self.dim
        
        # Combine all terms with different weights
        result = (tent + poly_interaction + fractal + cross_coupling + 
                 tanh_term) * dim_factor
        
        # Add a small constant offset to ensure positive fitness
        return result + 5.0