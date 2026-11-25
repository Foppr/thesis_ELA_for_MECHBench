import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with strong conditioning
        result = 0.3 * np.sum(x**2)
        
        # Add highly complex periodic components with chaotic wavelength modulation
        for i in range(self.dim):
            wavelength = 2 * np.pi / (1 + i % 7 + 0.5 * np.sin(i * 0.7))
            amplitude = 1.5 + 0.8 * np.cos(i * 0.3)
            result += amplitude * np.sin(wavelength * x[i]) * np.cos(wavelength * x[i] * 0.4) * np.exp(-0.1 * np.abs(x[i]))
            
        # Introduce deeply asymmetric basins with multiple exponents and cross-dimensional coupling
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.3 * (x[i] - 1.5)**5 + 0.2 * (x[i] - 1.5)**4 + 0.1 * (x[i] - 1.5)**3
            else:
                result += 0.3 * (x[i] + 1.5)**5 + 0.2 * (x[i] + 1.5)**4 + 0.1 * (x[i] + 1.5)**3
                
        # Add intricate saddle point structure with higher-order cross-dimensional terms
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                result += 0.1 * x[i]**2 * x[j]**2 * np.sin(0.3 * (x[i]**3 + x[j]**3))
                
        # Include highly chaotic nested oscillations with varying frequencies
        chaotic = 0.05 * np.sum(np.sin(15 * np.sin(x)) * np.cos(8 * np.sin(x)) * np.tanh(x))
        result += chaotic
        
        # Add extreme noise-like perturbations with non-uniform frequency
        for i in range(self.dim):
            result += 0.05 * np.sin(100 * x[i]) * np.cos(70 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Add a global shaping term to increase conditioning and non-separability
        result += 0.2 * np.sum(np.abs(x)**3) * np.sin(0.2 * np.sum(x**2))
        
        return result