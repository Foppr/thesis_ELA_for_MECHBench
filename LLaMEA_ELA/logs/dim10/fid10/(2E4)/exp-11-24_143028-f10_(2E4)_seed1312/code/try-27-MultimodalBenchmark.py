import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add highly chaotic sinusoidal components with cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.5 * np.sin(9 * x[i]) * np.cos(6 * x[j]) * np.sin(3 * (x[i] + x[j]))
        
        # Add enhanced saddle point structure with higher-order polynomial terms
        for i in range(self.dim):
            result += 0.3 * x[i]**5 - 0.7 * x[i]**4 + 0.4 * x[i]**3 - 0.1 * x[i]**2
        
        # Add stronger non-separable high-frequency oscillations
        sum_x = np.sum(x)
        result += 0.6 * np.sin(15 * sum_x) * np.cos(12 * sum_x)
        
        # Add global minimum penalty with exponential scaling
        result += 0.1 * np.exp(-np.sum(np.abs(x)) / self.dim)
        
        # Add asymmetric cross-dimensional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.sin(5 * x[i]) * np.cos(3 * x[j]) * np.tan(0.5 * (x[i] - x[j]))
        
        # Add additional chaotic component with dynamic frequency (mutated)
        for i in range(self.dim):
            result += 0.15 * np.sin(8 * x[i] + np.sum(x[:i]) if i > 0 else 0) * np.cos(4 * x[i] + 0.5 * np.sin(x[i]))
        
        # Add a new twist: perturbed harmonic interactions
        for i in range(self.dim):
            result += 0.25 * np.sin(7 * x[i]) * np.cos(5 * x[i]) * np.sin(2 * x[i]**2)
        
        return result