import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with conditionally scaled coefficients
        result = 0.5 * np.sum(x**2)
        
        # Chaotic sinusoidal components with non-linear frequency modulation
        for i in range(self.dim):
            freq = 3 + 2 * np.sin(0.5 * x[i])
            result += 0.2 * np.sin(freq * x[i]) * np.cos(2 * x[i] + 0.5 * np.sin(x[i]))
        
        # Asymmetric cross-dimensional interactions with variable coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.1 * (i + 1) / (j + 1)
                result += coupling * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        
        # Non-uniform penalty term with multiple local minima
        result += 0.05 * np.sum((x - 2.0)**2 * (1 + 0.3 * np.sin(5 * x)))
        
        # Additional chaotic oscillation component
        chaos_term = 0.1 * np.sum(np.sin(3 * x) * np.cos(7 * x))
        result += chaos_term
        
        return result