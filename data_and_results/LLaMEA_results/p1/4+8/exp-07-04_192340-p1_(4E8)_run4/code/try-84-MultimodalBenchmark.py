import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic coefficients for varying curvature
        self.coeffs = np.random.rand(dim) * 3 + 1
        self.saddle_points = np.random.rand(dim) * 10 - 5
        # Additional chaotic parameters for increased complexity
        self.chaos_params = np.random.rand(dim) * 0.5 + 0.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic exponential terms with enhanced decay
        result = 0.0
        for i in range(self.dim):
            # Enhanced exponential decay with chaotic coefficients
            result += self.coeffs[i] * np.exp(-0.3 * (x[i] - self.saddle_points[i])**2)
            # Saddle point contribution with varying curvature and chaos
            result += 0.3 * (x[i] - self.saddle_points[i])**2 * np.sin(self.chaos_params[i] * x[i])
            # Chaotic gradient component with modified frequency
            result += 0.15 * np.sin(self.coeffs[i] * x[i]) * np.cos(self.chaos_params[i] * x[i])
            
        # Add coupling terms between dimensions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling with chaotic modulation
                coupling = np.sin(x[i] * x[j]) * (i + j) * self.chaos_params[i] * self.chaos_params[j]
                result += 0.08 * coupling
                
        # Add global minimum at origin with penalty
        result += 0.002 * np.sum(x**6)
        
        # Add chaotic sine-wave interaction term for multimodality
        result += 0.2 * np.prod(np.sin(0.5 * x))
        
        return result