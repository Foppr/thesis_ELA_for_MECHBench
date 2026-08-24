import numpy as np

class MultimodalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Polynomial chaos with mixed exponents
        for i in range(self.dim):
            result += 0.1 * x[i]**3 + 0.05 * x[i]**4 + 0.02 * x[i]**5
            
        # Saddle point inducing terms with trigonometric coupling
        for i in range(self.dim):
            result += 0.3 * np.sin(0.5 * x[i]) * np.cos(0.5 * x[i]) * x[i]**2
            
        # Exponential scaling with interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction
                result += 0.2 * np.exp(-0.1 * (x[i] - x[j])**2) * (x[i]**2 + x[j]**2)
                
        # Multimodal component with sinusoidal modulation
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(3 * x[i]) * np.cos(2 * x[i]) + 0.5 * np.sin(5 * x[i])
        result += 0.5 * multimodal**2
        
        # Additional saddle point structure
        sum_x_sq = np.sum(x**2)
        result += 0.1 * sum_x_sq * np.sin(0.2 * sum_x_sq)
        
        # Global optimum enforcing term with exponential penalty
        result += 0.001 * np.sum(np.exp(0.5 * np.abs(x)) - 1)
        
        return result