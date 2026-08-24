import numpy as np

class MultiPeakSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Multi-peak sinusoidal component with varying frequencies and amplitudes
        peaks = 0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(i * 0.5)
            amp = 1 + 0.5 * np.cos(i * 0.3)
            peaks += amp * np.sin(freq * x_normalized[i])**2
        
        # Polynomial correlation terms with adaptive exponents
        poly_corr = 0
        for i in range(self.dim):
            exponent = 2 + 2 * np.sin(i * 0.7)
            poly_corr += np.abs(x_normalized[i])**exponent
            
        # Adaptive conditioning based on dimension
        conditioning = 0
        for i in range(self.dim):
            cond_factor = 1 + 0.5 * np.sin(i * 0.4)
            conditioning += cond_factor * x_normalized[i]**4
            
        # Cross-dimensional interaction terms with varying coupling strengths
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.2 * np.sin(i * j * 0.2)
                interaction += coupling * x_normalized[i] * x_normalized[j]
                
        # Global modulation with multi-scale sinusoidal patterns
        modulation = 0
        for i in range(self.dim):
            modulation += np.sin(x_normalized[i] * 5) * np.cos(x_normalized[i] * 2) * np.sin(x_normalized[i] * 8)
            
        # Combined landscape
        result = 0.25 * f1 + 0.3 * peaks + 0.2 * poly_corr + 0.15 * conditioning + 0.1 * interaction + 0.05 * modulation
        
        # Add a small perturbation to increase complexity
        perturbation = 0.02 * np.sum(np.sin(x_normalized * 10) * np.cos(x_normalized * 3))
        result += perturbation
        
        return result