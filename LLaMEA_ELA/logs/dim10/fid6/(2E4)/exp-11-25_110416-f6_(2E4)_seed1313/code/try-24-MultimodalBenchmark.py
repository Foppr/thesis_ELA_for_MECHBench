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
            freq = 2 ** (i % 6 + 1)
            amp = 0.7 + 0.3 * np.sin(i * 0.5)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.4) * np.exp(-0.15 * abs(x[i]))
            
        # Add multiple global minima with different structures
        for i in range(self.dim):
            result += 0.2 * (x[i]**2 - 2*x[i] + 1) * np.sin(7 * x[i]) + 0.15 * (x[i]**3 - x[i])**2
            
        # Add complex polynomial barriers with varying exponents and coefficients
        for i in range(self.dim):
            result += 0.1 * (x[i] - 2)**(4 + i % 3) + 0.08 * (x[i] + 3)**(5 + i % 4)
            
        # Add chaotic cross-dimensional interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                result += 0.03 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * (1 + 0.15 * np.sin(i+j))
                
        # Add a complex global minimum structure with multiple peaks
        for i in range(self.dim):
            result += 0.04 * np.exp(-0.5 * ((x[i] - 2.0) / 0.3)**2) * np.cos(18 * x[i])
            
        # Add a new term to increase the complexity of the landscape
        for i in range(self.dim):
            result += 0.05 * np.sin(2 * x[i]) * np.cos(3 * x[i]) * (1 + 0.2 * np.sin(x[i]**2))
            
        return result