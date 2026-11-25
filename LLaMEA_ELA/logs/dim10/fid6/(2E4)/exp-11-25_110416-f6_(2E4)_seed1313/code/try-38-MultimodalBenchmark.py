import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with conditioning
        result = 0.5 * np.sum(x**2)
        
        # Add periodic components with varying wavelengths and amplitudes
        for i in range(self.dim):
            wavelength = 2 * np.pi / (1 + i % 5)
            amplitude = 1.0 + 0.5 * np.sin(i)
            result += amplitude * np.sin(wavelength * x[i]) * np.cos(wavelength * x[i] * 0.3)
            
        # Introduce asymmetric basins with different exponents
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.2 * (x[i] - 2)**4 + 0.1 * (x[i] - 2)**3
            else:
                result += 0.2 * (x[i] + 2)**4 + 0.1 * (x[i] + 2)**3
                
        # Add saddle point structure through cross-dimensional terms
        for i in range(self.dim):
            for j in range(i+1, min(i+2, self.dim)):
                result += 0.05 * x[i] * x[j] * np.sin(0.5 * (x[i]**2 + x[j]**2))
                
        # Include a chaotic element with nested oscillations
        chaotic = 0.03 * np.sum(np.sin(10 * np.sin(x)) * np.cos(5 * np.sin(x)))
        result += chaotic
        
        # Add noise-like perturbations to increase conditioning
        for i in range(self.dim):
            result += 0.02 * np.sin(50 * x[i]) * np.cos(30 * x[i])
            
        return result