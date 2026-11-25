import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with multiple local minima
        result = 0.0
        centers = np.linspace(-4.5, 4.5, min(10, self.dim))
        for i in range(min(10, self.dim)):
            center = centers[i] if self.dim > 1 else 0.0
            result += np.exp(-0.5 * np.sum((x - center)**2)) * np.sin(2 * np.pi * x[0] if self.dim > 0 else 0)
            
        # Sinusoidal modulation with frequency scaling and phase shifts
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i)
            phase = 0.3 * np.cos(i)
            result += 2.0 * np.sin(freq * x[i] + phase) * np.cos(0.7 * x[i])
            
        # Asymmetric polynomial potentials with varying exponents
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.5 * x[i]**3.5 * (1 + 0.2 * np.sin(x[i]))
            else:
                result += 0.7 * x[i]**4.2 * (1 + 0.15 * np.cos(x[i]))
                
        # Cross-dimensional coupling with exponential interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(3 * x[i] + 2 * x[j])
                result += 0.3 * coupling
                
        # Conditioning and scaling term based on dimensionality
        conditioning = 1.0 + 0.1 * self.dim + 0.05 * np.sum(np.abs(x))
        result *= conditioning
        
        return result