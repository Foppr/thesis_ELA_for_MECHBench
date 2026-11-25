import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 3 ** (i % 5 + 1)
            amp = 0.8 + 0.2 * np.sin(i)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.exp(-0.1 * abs(x[i]))
            
        # Add multiple global minima with different structures
        for i in range(self.dim):
            result += 0.15 * (x[i]**2 - 2*x[i] + 1) * np.sin(5 * x[i]) + 0.1 * (x[i]**3 - x[i])**2
            
        # Add complex polynomial barriers with varying exponents and coefficients
        for i in range(self.dim):
            result += 0.08 * (x[i] - 2)**(4 + i % 2) + 0.06 * (x[i] + 3)**(5 + i % 3)
            
        # Add chaotic cross-dimensional interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                result += 0.02 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * (1 + 0.1 * np.sin(i+j))
                
        # Add a complex global minimum structure with multiple peaks
        for i in range(self.dim):
            result += 0.03 * np.exp(-0.5 * ((x[i] - 2.0) / 0.4)**2) * np.cos(15 * x[i])
            
        return result