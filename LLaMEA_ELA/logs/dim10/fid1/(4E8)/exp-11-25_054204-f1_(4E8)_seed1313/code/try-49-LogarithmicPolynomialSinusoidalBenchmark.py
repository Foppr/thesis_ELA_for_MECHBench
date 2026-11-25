import numpy as np

class LogarithmicPolynomialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term for conditioning
        result = np.sum(x**4) / 100.0
        
        # Add logarithmic barrier terms to create ruggedness
        for i in range(self.dim):
            result += 2.0 * np.log(1.0 + np.abs(x[i])) * np.sin(2 * np.pi * x[i])
            
        # Add polynomial chaos expansion with mixed interactions
        for i in range(self.dim):
            result += 0.5 * x[i]**3 * np.cos(0.5 * x[i])
            
        # Cross-dimensional polynomial interactions with sinusoidal modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * (x[i]**2 + x[j]**2) * np.sin(0.7 * x[i] * x[j])
                
        # Add higher-order mixed terms for increased complexity
        for i in range(self.dim):
            result += 0.15 * x[i]**5 * np.cos(3 * x[i])
            
        # Introduce sinusoidal wave interactions between dimensions
        wave_sum = 0.0
        for i in range(self.dim):
            wave_sum += np.sin(1.5 * x[i])
        for i in range(self.dim):
            result += 0.2 * wave_sum * np.cos(0.8 * x[i])
            
        # Add Gaussian-like perturbations with logarithmic scaling
        for i in range(self.dim):
            result += 0.4 * np.exp(-0.5 * (x[i] - 1.5)**2) * np.sin(4 * x[i])
            
        # Add cross-dimensional exponential interactions with polynomial weighting
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.25 * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * (x[i] + x[j])**3
                
        # Add global conditioning factor
        result *= (1.0 + 0.05 * np.sum(np.abs(x)))
        
        return result