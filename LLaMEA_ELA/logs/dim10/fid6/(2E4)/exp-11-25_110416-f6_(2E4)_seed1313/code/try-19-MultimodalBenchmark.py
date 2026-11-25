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
            freq_factor = 2 ** (i % 5 + 1)
            result += 0.6 * np.sin(freq_factor * x[i]) * np.cos(freq_factor * x[i] * 0.7)
            
        # Add complex polynomial barriers with varying exponents
        for i in range(self.dim):
            result += 0.12 * (x[i] - 1)**(3 + i % 4) + 0.06 * (x[i] + 2)**(4 + i % 5)
            
        # Add a global minimum with intricate structure
        for i in range(self.dim):
            result += 0.03 * np.exp(-0.5 * ((x[i] - 1.5) / 0.6)**2) * np.sin(12 * x[i])
            
        # Add cross-dimensional interaction terms with chaotic phase shifts
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                phase_shift = np.sin(0.5 * (i + j))
                result += 0.015 * x[i] * x[j] * np.sin(x[i] + x[j] + phase_shift)
                
        return result