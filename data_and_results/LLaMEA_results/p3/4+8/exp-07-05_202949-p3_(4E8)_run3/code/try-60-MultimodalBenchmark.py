import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic and polynomial terms with adaptive scaling
        result = 0.0
        for i in range(self.dim):
            result += (x[i] - 1.2)**2 + (x[i] + 1.2)**2 + 0.015 * x[i]**4 + 0.003 * x[i]**6
        
        # Enhanced interaction terms with adaptive coupling and exponential scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use adaptive scaling based on dimension indices
                adaptive_scale = np.exp(1.5 * (i + j) / self.dim)
                result += adaptive_scale * (x[i] - x[j])**2
        
        # Saddle point structure with multi-frequency sinusoidal modulations
        for i in range(self.dim):
            result += 0.9 * np.sin(3.5 * x[i]) * np.cos(2.5 * x[i]) + 0.4 * np.sin(5.5 * x[i]) + 0.2 * np.sin(7.0 * x[i])
        
        # Complex global minimum with high curvature and multi-dimensional polynomial terms
        result += 0.0025 * np.sum(x**2) + 0.0006 * np.sum(x**6) + 0.00015 * np.sum(x**8)
        
        # Highly periodic component with variable frequency and amplitude
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(4.5 * x[i]) * np.cos(3.5 * x[i]) + 0.6 * np.sin(6.5 * x[i]) + 0.3 * np.sin(8.0 * x[i])
        result += 0.2 * periodic_term
        
        # Shift global minimum with enhanced offset and higher-order polynomial
        result += 0.8 * np.sum((x - 0.25)**2) + 0.06 * np.sum((x - 0.25)**4) + 0.01 * np.sum((x - 0.25)**6)
        
        # Ruggedness enhancement with cross-dimensional noise-like component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.025 * np.sin(11.0 * x[i]) * np.cos(8.0 * x[i]) + 0.01 * np.sin(13.0 * x[i])
        result += noise
        
        # Add dimensionality-dependent scaling factor to increase challenge
        result *= (1.0 + 0.1 * self.dim / 10.0)
        
        return result