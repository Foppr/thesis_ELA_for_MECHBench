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
                result += 0.7 * np.sin(12 * x[i]) * np.cos(9 * x[j]) * np.sin(5 * (x[i] + x[j]))
        
        # Stronger saddle point structure with higher-order polynomial terms
        for i in range(self.dim):
            result += 0.5 * x[i]**5 - 1.0 * x[i]**4 + 0.6 * x[i]**3 - 0.3 * x[i]**2
        
        # Enhanced non-separable high-frequency oscillations
        sum_x = np.sum(x)
        result += 0.8 * np.sin(20 * sum_x) * np.cos(17 * sum_x)
        
        # Global minimum penalty with exponential scaling
        result += 0.2 * np.exp(-np.sum(np.abs(x)) / self.dim)
        
        # Asymmetric cross-dimensional coupling with enhanced complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(7 * x[i]) * np.cos(5 * x[j]) * np.tan(0.7 * (x[i] - x[j]))
        
        # Additional chaotic component with dynamic frequency and amplitude
        for i in range(self.dim):
            result += 0.25 * np.sin(10 * x[i] + np.sum(x[:i]) if i > 0 else 0) * np.cos(6 * x[i])
        
        # Add a new term to increase the number of local minima
        for i in range(self.dim):
            result += 0.15 * np.sin(25 * x[i]) * np.cos(12 * x[i]) * (x[i]**2 + 1)
        
        # Introduce a new component to improve fitness score by reducing bias
        for i in range(self.dim):
            result += 0.05 * np.sin(30 * x[i]) * np.cos(15 * x[i]) * np.exp(-x[i]**2)
        
        return result