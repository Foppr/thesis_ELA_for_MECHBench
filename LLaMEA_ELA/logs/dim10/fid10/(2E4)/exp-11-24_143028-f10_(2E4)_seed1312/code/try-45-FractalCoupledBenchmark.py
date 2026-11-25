import numpy as np

class FractalCoupledBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Fractal-like oscillatory component with varying frequencies
        for i in range(self.dim):
            result += 0.5 * np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.sin(6 * x[i]**2)
        
        # Dynamic coupling with exponentially increasing frequency
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 5 + (i + j) * 0.5
                result += 0.4 * np.sin(freq * x[i]) * np.cos(freq * x[j]) * np.tan(0.3 * (x[i] - x[j]))
        
        # Embedded fractal structure using recursive-like terms
        for i in range(self.dim):
            result += 0.3 * np.sin(15 * x[i]) * np.cos(12 * x[i]) * np.sin(9 * x[i]**3)
        
        # Non-separable high-order polynomial with chaotic interaction
        sum_x = np.sum(x)
        result += 0.6 * np.sin(20 * sum_x) * (sum_x**4 - 2*sum_x**3 + sum_x**2)
        
        # Saddle point enhancement with multiple local extrema
        for i in range(self.dim):
            result += 0.25 * x[i]**6 - 0.8 * x[i]**5 + 0.9 * x[i]**4 - 0.7 * x[i]**3 + 0.3 * x[i]**2
        
        # Cross-dimensional exponential interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.exp(-np.abs(x[i] - x[j]) / (1 + np.abs(x[i]) + np.abs(x[j]))) * np.cos(10 * (x[i] + x[j]))
        
        # Additional chaotic oscillation with variable amplitude
        for i in range(self.dim):
            result += 0.35 * np.sin(25 * x[i] + np.sin(5 * x[i])) * np.cos(20 * x[i]) * (1 + 0.2 * np.abs(x[i]))
        
        # Global minimum attraction with boundary sensitivity
        result += 0.15 * np.exp(-np.sum(np.abs(x)) / self.dim) * np.sin(30 * sum_x)
        
        return result