import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Sum of quadratic terms with exponentially increasing coefficients
        for i in range(self.dim):
            result += (x[i] ** 2) * (2 ** i)
            
        # Add highly oscillatory local minima using sine waves with exponentially increasing frequencies
        for i in range(self.dim):
            freq = 2 ** (i % 5)
            result += 0.7 * np.sin(freq * x[i]) * np.cos(freq * x[(i + 1) % self.dim])
            
        # Add cross-dimensional interaction terms with high-frequency oscillations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(12 * x[i] * x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
                
        # Add a complex penalty term with multiple local minima
        penalty = 0.0
        for i in range(self.dim):
            penalty += (x[i] - 1.5)**6 + (x[i] + 1.5)**6 + 0.6 * np.sin(12 * x[i])
            
        # Add a chaotic component using logistic map-like behavior with higher sensitivity
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(120 * x[i]) * np.cos(60 * x[(i + 1) % self.dim]) + 0.3 * np.sin(80 * x[i]**2)
            
        # Add a multi-scale oscillation component
        multiscale = 0.0
        for i in range(self.dim):
            multiscale += 0.4 * np.sin(20 * x[i]) * np.cos(15 * x[(i + 2) % self.dim]) * np.exp(-0.05 * x[i]**2)
            
        return result + 0.025 * penalty + 0.008 * chaos + 0.01 * multiscale