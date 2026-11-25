import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term
        result = np.sum(x**4) / 4.0
        
        # Add trigonometric interactions with varying frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(2 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Add saddle point structure with higher-order terms
        for i in range(self.dim):
            result += 0.2 * x[i]**6 - 0.5 * x[i]**5 + 0.3 * x[i]**4
        
        # Introduce dynamic scaling based on dimensionality
        scale_factor = np.log(self.dim + 1) / 2.0
        for i in range(self.dim):
            result += scale_factor * np.sin(4 * x[i]) * np.cos(2 * x[i])
        
        # Add asymmetric coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                asym_term = (x[i] - x[j])**3 * np.exp(-0.05 * (x[i] + x[j])**2)
                result += 0.15 * asym_term
        
        # Add chaotic component with non-linear transformation
        sum_x_sq = np.sum(x**2)
        result += 0.2 * np.sin(10 * sum_x_sq) * np.cos(5 * sum_x_sq) * np.exp(-0.01 * sum_x_sq)
        
        # Add penalty for proximity to boundaries
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 0.1 * (5.0 - np.abs(x[i]))**2
        result += boundary_penalty
        
        return result