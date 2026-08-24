import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic coefficients for varying curvature
        self.coeffs = np.random.rand(dim) * 3 + 1
        self.saddle_points = np.random.rand(dim) * 10 - 5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic exponential terms with enhanced decay
        result = 0.0
        for i in range(self.dim):
            # Enhanced exponential decay with chaotic coefficients
            result += self.coeffs[i] * np.exp(-0.3 * (x[i] - self.saddle_points[i])**2)
            # Saddle point contribution with enhanced curvature
            result += 0.3 * (x[i] - self.saddle_points[i])**2 * np.sin(2 * x[i])
            # Chaotic gradient component with higher frequency
            result += 0.15 * np.sin(self.coeffs[i] * x[i]) * np.cos(1.5 * x[i])
            
        # Add coupling terms between dimensions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.08 * np.sin(x[i] * x[j]) * (i + j) * np.cos(0.5 * (i + j))
                
        # Add global minimum at origin with penalty
        result += 0.002 * np.sum(x**6)
        
        # Add a new chaotic component to improve fitness
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(3 * x[i]) * np.cos(2 * x[i]) * np.exp(-0.1 * x[i]**2)
        result += 0.05 * chaotic_term
        
        return result