import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add highly oscillatory sinusoidal components with exponential frequency growth
        for i in range(self.dim):
            freq_factor = 3 ** (i % 3 + 1)
            result += 0.6 * np.sin(freq_factor * x[i]) * np.cos(freq_factor * x[i] * 0.7)
            
        # Add complex polynomial barriers with varying exponents
        for i in range(self.dim):
            result += 0.15 * (x[i] - 1.2)**(2 + i % 4) + 0.08 * (x[i] + 1.8)**(4 + i % 3)
            
        # Add a global minimum with intricate structure using exponential decay
        for i in range(self.dim):
            result += 0.03 * np.exp(-0.3 * ((x[i] - 1.2) / 0.6)**2) * np.sin(12 * x[i])
            
        # Add cross-dimensional interaction terms with modified coupling strength
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                result += 0.02 * x[i] * x[j] * np.sin(x[i] + x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        return result