import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with higher-order components
        result = np.sum(x**6) / 6.0
        
        # Add trigonometric interactions with varying frequencies and amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_factor = (i + 1) * (j + 1)
                result += 0.25 * np.sin(freq_factor * x[i]) * np.cos(freq_factor * x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Add enhanced saddle point structure with asymmetric terms
        for i in range(self.dim):
            result += 0.15 * x[i]**7 - 0.4 * x[i]**6 + 0.3 * x[i]**5
        
        # Introduce dynamic scaling based on dimensionality with logarithmic growth
        scale_factor = np.log(self.dim + 2) / 3.0
        for i in range(self.dim):
            result += scale_factor * np.sin(5 * x[i]) * np.cos(3 * x[i])
        
        # Add asymmetric coupling with stronger exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                asym_term = (x[i] - x[j])**4 * np.exp(-0.1 * (x[i] + x[j])**2)
                result += 0.2 * asym_term
        
        # Add chaotic component with stronger non-linear transformation
        sum_x_sq = np.sum(x**2)
        result += 0.3 * np.sin(15 * sum_x_sq) * np.cos(7 * sum_x_sq) * np.exp(-0.02 * sum_x_sq)
        
        # Add penalty for proximity to boundaries with quadratic scaling
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 0.15 * (5.0 - np.abs(x[i]))**3
        result += boundary_penalty
        
        # Add cross-dimensional coupling with sinusoidal modulation
        if self.dim > 1:
            sum_x = np.sum(x)
            result += 0.2 * np.sin(2 * sum_x) * np.cos(3 * sum_x) * np.exp(-0.03 * sum_x**2)
        
        return result