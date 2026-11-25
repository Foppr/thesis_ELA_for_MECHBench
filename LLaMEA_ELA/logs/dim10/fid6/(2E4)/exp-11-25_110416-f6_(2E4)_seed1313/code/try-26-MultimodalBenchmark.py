import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add trigonometric chaos with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2 ** (i % 4 + 1)
            amp = 1.0 + 0.5 * np.sin(i * 0.5)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.exp(-0.05 * x[i]**2)
            
        # Add radial symmetry terms with multiple peaks
        r = np.sqrt(np.sum(x**2))
        result += 0.3 * np.sin(10 * r) * np.exp(-0.1 * r**2)
        
        # Add cross-dimensional coupling with chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                result += 0.05 * interaction * (1 + 0.2 * np.sin(i + j))
                
        # Add polynomial barriers with varying degrees
        for i in range(self.dim):
            result += 0.1 * (x[i]**4 - 2*x[i]**2 + 1) * np.exp(-0.05 * abs(x[i]))
            
        # Add global minimum structure with multiple local minima
        for i in range(self.dim):
            result += 0.2 * np.exp(-0.5 * ((x[i] - 1.0) / 0.3)**2) * np.sin(8 * x[i])
            
        return result