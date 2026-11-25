import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add modified chaotic sinusoidal components with altered cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.4 * np.sin(8 * x[i]) * np.cos(5 * x[j]) * np.sin(2 * (x[i] + x[j]))
        
        # Add refined saddle point structure with modified polynomial terms
        for i in range(self.dim):
            result += 0.25 * x[i]**5 - 0.6 * x[i]**4 + 0.3 * x[i]**3 - 0.08 * x[i]**2
        
        # Add adjusted non-separable high-frequency oscillations
        sum_x = np.sum(x)
        result += 0.5 * np.sin(12 * sum_x) * np.cos(10 * sum_x)
        
        # Add modified global minimum penalty with logarithmic scaling
        result += 0.08 * np.log(1 + np.sum(np.abs(x)) / self.dim)
        
        # Add altered asymmetric cross-dimensional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(4 * x[i]) * np.cos(2 * x[j]) * np.tan(0.3 * (x[i] - x[j]))
        
        # Add updated chaotic component with fixed frequency
        for i in range(self.dim):
            result += 0.12 * np.sin(7 * x[i]) * np.cos(3 * x[i]) * np.sin(0.5 * x[i]**2)
        
        # Add new perturbed harmonic interactions with different frequencies
        for i in range(self.dim):
            result += 0.2 * np.sin(6 * x[i]) * np.cos(4 * x[i]) * np.sin(1.5 * x[i]**2)
        
        return result