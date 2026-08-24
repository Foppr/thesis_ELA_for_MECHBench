import numpy as np

class FractalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base exponential decay term with sinusoidal modulation
        result = 0.0
        for i in range(self.dim):
            result += np.exp(-0.1 * np.abs(x[i])) * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
            
        # Add power-law weighted cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                result += 0.5 * (1.0 / (1.0 + distance**1.5)) * np.sin(3.0 * x[i] + 2.0 * x[j])
                
        # Introduce fractal-like scaling with varying exponents
        fractal_scale = 1.0
        for i in range(self.dim):
            fractal_scale += 0.3 * np.sin(5.0 * x[i]) * np.cos(7.0 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Apply exponential transformation with logarithmic conditioning
        log_conditioning = np.log(1.0 + 0.2 * np.sum(np.abs(x)))
        result = result * np.exp(0.1 * np.sum(x**2)) * (1.0 + 0.5 * log_conditioning)
        
        # Add chaotic perturbations with varying frequencies and amplitudes
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            chaotic_perturbation += 0.05 * np.sin(20.0 * x[i]) * np.cos(17.0 * x[i]) * np.sin(13.0 * x[i]**2)
            
        result = result + chaotic_perturbation
        
        # Apply dimensionality-dependent scaling
        result = result * (1.0 + 0.1 * self.dim + 0.02 * np.sum(x**4))
        
        return result