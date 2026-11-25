import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal components with cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.6 * np.sin(10 * x[i]) * np.cos(7 * x[j]) * np.sin(4 * (x[i] + x[j]))
        
        # Stronger saddle point structure with higher-order polynomial terms
        for i in range(self.dim):
            result += 0.4 * x[i]**5 - 0.8 * x[i]**4 + 0.5 * x[i]**3 - 0.2 * x[i]**2
        
        # Enhanced non-separable high-frequency oscillations
        sum_x = np.sum(x)
        result += 0.7 * np.sin(18 * sum_x) * np.cos(15 * sum_x)
        
        # Global minimum penalty with exponential scaling
        result += 0.15 * np.exp(-np.sum(np.abs(x)) / self.dim)
        
        # Asymmetric cross-dimensional coupling with enhanced complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.25 * np.sin(6 * x[i]) * np.cos(4 * x[j]) * np.tan(0.6 * (x[i] - x[j]))
        
        # Additional chaotic component with dynamic frequency and amplitude
        for i in range(self.dim):
            result += 0.2 * np.sin(9 * x[i] + np.sum(x[:i]) if i > 0 else 0) * np.cos(5 * x[i])
        
        # Add a new term to increase the number of local minima
        for i in range(self.dim):
            result += 0.1 * np.sin(20 * x[i]) * np.cos(10 * x[i]) * (x[i]**2 + 1)
        
        return result