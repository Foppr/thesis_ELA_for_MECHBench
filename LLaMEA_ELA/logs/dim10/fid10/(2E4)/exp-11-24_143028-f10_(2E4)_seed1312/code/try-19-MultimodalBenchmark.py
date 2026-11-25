import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with conditionally scaled coefficients
        result = 0.5 * np.sum(x**2)
        
        # Enhanced chaotic sinusoidal components with higher frequency modulation
        for i in range(self.dim):
            freq = 5 + 3 * np.sin(0.7 * x[i]) + 2 * np.cos(0.3 * x[i])
            result += 0.3 * np.sin(freq * x[i]) * np.cos(3 * x[i] + 0.4 * np.sin(2 * x[i]))
        
        # Stronger asymmetric cross-dimensional interactions with dynamic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.2 * (i + 1) / (j + 1) * np.cos(0.5 * x[i])
                result += coupling * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j] + 0.3 * np.sin(x[i] - x[j]))
        
        # Non-uniform penalty term with multiple local minima and additional complexity
        result += 0.1 * np.sum((x - 2.0)**2 * (1 + 0.5 * np.sin(5 * x)) * (1 + 0.3 * np.cos(3 * x)))
        
        # Additional chaotic oscillation component with higher frequency
        chaos_term = 0.15 * np.sum(np.sin(5 * x) * np.cos(9 * x) * np.sin(2 * x))
        result += chaos_term
        
        # Non-separable high-order interaction term
        if self.dim >= 2:
            for i in range(self.dim - 1):
                result += 0.08 * np.sin(x[i] + x[i+1]) * np.cos(x[i] * x[i+1]) * np.exp(-0.1 * (x[i]**2 + x[i+1]**2))
        
        return result