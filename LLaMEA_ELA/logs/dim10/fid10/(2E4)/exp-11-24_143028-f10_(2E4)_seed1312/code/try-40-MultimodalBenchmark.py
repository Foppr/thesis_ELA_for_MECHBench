import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with higher-order components
        result = np.sum(x**8) / 8.0
        
        # Add trigonometric interactions with varying frequencies and amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_factor = (i + 1) * (j + 1)
                result += 0.3 * np.sin(freq_factor * x[i]) * np.cos(freq_factor * x[j]) * np.exp(-0.08 * (x[i] - x[j])**2)
        
        # Add enhanced saddle point structure with asymmetric terms
        for i in range(self.dim):
            result += 0.2 * x[i]**9 - 0.5 * x[i]**8 + 0.4 * x[i]**7 - 0.1 * x[i]**6
        
        # Introduce dynamic scaling based on dimensionality with logarithmic growth
        scale_factor = np.log(self.dim + 3) / 4.0
        for i in range(self.dim):
            result += scale_factor * np.sin(7 * x[i]) * np.cos(5 * x[i])
        
        # Add asymmetric coupling with stronger exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                asym_term = (x[i] - x[j])**5 * np.exp(-0.15 * (x[i] + x[j])**2)
                result += 0.25 * asym_term
        
        # Add chaotic component with stronger non-linear transformation
        sum_x_sq = np.sum(x**2)
        result += 0.4 * np.sin(20 * sum_x_sq) * np.cos(10 * sum_x_sq) * np.exp(-0.03 * sum_x_sq)
        
        # Add penalty for proximity to boundaries with cubic scaling
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 0.2 * (5.0 - np.abs(x[i]))**4
        result += boundary_penalty
        
        # Add cross-dimensional coupling with sinusoidal modulation
        if self.dim > 1:
            sum_x = np.sum(x)
            result += 0.25 * np.sin(3 * sum_x) * np.cos(4 * sum_x) * np.exp(-0.05 * sum_x**2)
        
        # Add fractal-like oscillations with multiple frequency components
        for i in range(self.dim):
            result += 0.1 * np.sin(25 * x[i]) * np.cos(15 * x[i]) * np.sin(10 * x[i])
        
        # Add higher-order cross-dimensional interactions
        if self.dim > 2:
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    for k in range(j+1, self.dim):
                        result += 0.05 * np.sin(x[i] + x[j] + x[k]) * np.exp(-0.01 * (x[i]**2 + x[j]**2 + x[k]**2))
        
        return result