import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic coefficients for varying curvature and dynamic scaling
        self.coeffs = np.random.rand(dim) * 3 + 1
        self.saddle_points = np.random.rand(dim) * 10 - 5
        self.interaction_coeffs = np.random.rand(dim, dim) * 2 - 1
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic exponential terms with dynamic scaling
        result = 0.0
        for i in range(self.dim):
            # Enhanced exponential decay with chaotic coefficients
            result += self.coeffs[i] * np.exp(-0.3 * (x[i] - self.saddle_points[i])**2) * np.cos(0.5 * x[i])
            # Saddle point contribution with varying curvature and dynamic scaling
            result += 0.3 * (x[i] - self.saddle_points[i])**2 * np.sin(0.7 * x[i])
            # Chaotic gradient component with higher frequency
            result += 0.15 * np.sin(self.coeffs[i] * x[i]) * np.cos(2 * x[i])
            # Add polynomial terms for increased multimodality
            result += 0.05 * x[i]**4 * np.sin(0.3 * x[i])
            
        # Add coupling terms between dimensions with variable interaction coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced interaction with dynamic scaling
                interaction = self.interaction_coeffs[i, j] * np.sin(x[i] * x[j]) * (i + j)
                # Add higher-order coupling terms
                interaction += 0.02 * np.cos(x[i] * x[j]) * (x[i]**2 + x[j]**2)
                result += interaction
                
        # Add global minimum at origin with penalty and enhanced polynomial terms
        result += 0.002 * np.sum(x**8) + 0.001 * np.sum(x**6)
        
        # Add chaotic modulation based on all dimensions
        chaotic_mod = np.sin(np.sum(x**3) * 0.1) * 0.5
        result += chaotic_mod
        
        # Add variable conditioning through dynamic scaling
        conditioning = np.mean(np.abs(x)) * 0.1
        result *= (1 + conditioning)
        
        return result