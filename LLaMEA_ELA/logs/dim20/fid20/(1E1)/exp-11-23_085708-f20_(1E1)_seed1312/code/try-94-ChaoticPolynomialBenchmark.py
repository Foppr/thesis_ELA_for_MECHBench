import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Tent map chaotic component with parameter control
        chaos = 0.0
        a = 1.8
        for i in range(self.dim):
            if i == 0:
                xi_prev = x_scaled[-1]  # Wrap around
            else:
                xi_prev = x_scaled[i-1]
            
            # Tent map: f(x) = a * x if x < 0.5, otherwise f(x) = a * (1 - x)
            chaos += np.abs(a * xi_prev - 0.5) - 0.5
        
        # Polynomial interaction terms with varying degrees
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_scaled[i]**3 + x_scaled[j]**2) * (i + j + 1)
        
        # Fractal-like self-similarity component using sine and cosine combinations
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2**i * x_scaled[i]) * np.cos(3**i * x_scaled[i])
            
        # Cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.exp(-0.1 * (x_scaled[i] - x_scaled[j])**2) * (i + j)
        
        # Add a global scaling factor based on dimensionality
        dim_factor = 1.0 + 0.1 * self.dim
        
        # Combine all components
        result = dim_factor * (poly_interaction + fractal + coupling + chaos**2)
        
        # Normalize and shift to ensure global minimum at origin
        return result + 5.0 * self.dim