import numpy as np

class PolynomialPeriodicCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Polynomial potential terms with varying degrees and coefficients
        poly_term = 0.0
        for i in range(self.dim):
            degree = 2 + (i % 3)
            coeff = 0.5 + 0.5 * np.sin(i * 0.5)
            poly_term += coeff * (x[i] ** degree)
        
        # Periodic boundary effects with dynamic frequencies
        periodic_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.cos(i * 0.3)
            amp = 1.0 + 0.3 * np.sin(i * 0.4)
            periodic_term += amp * np.sin(freq * x[i] / 5.0) * np.cos(freq * x[i] / 5.0)
        
        # Adaptive correlation structure between dimensions
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_coeff = 0.3 + 0.2 * np.sin(i * j * 0.2)
                corr_term += corr_coeff * x[i] * x[j]
        
        # Ruggedness modulation through multi-scale sinusoidal perturbations
        rugged_term = 0.0
        for i in range(self.dim):
            scale1 = 1.0 + 0.5 * np.sin(i * 0.6)
            scale2 = 1.0 + 0.3 * np.cos(i * 0.4)
            rugged_term += scale1 * np.sin(scale2 * x[i]) * np.cos(scale2 * x[i])
        
        # Directional bias with adaptive weights
        bias_term = 0.0
        for i in range(self.dim):
            weight = 0.8 + 0.2 * np.sin(i * 0.5)
            bias_term += weight * (x[i] ** 2) * np.exp(-0.1 * x[i] ** 2)
        
        # Multi-scale harmonic landscape
        harmonic_term = 0.0
        for i in range(self.dim):
            freq1 = 1.0 + 0.5 * np.sin(i * 0.3)
            freq2 = 2.0 + 0.3 * np.cos(i * 0.4)
            harmonic_term += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
        
        # Global scaling and modulation
        global_scale = 1.0 + 0.2 * np.sin(self.dim * 0.1) * np.cos(self.dim * 0.2)
        
        # Final combination with dynamic weights
        total = (0.3 * poly_term + 
                0.25 * periodic_term + 
                0.2 * corr_term + 
                0.1 * rugged_term + 
                0.1 * bias_term + 
                0.05 * harmonic_term)
        
        return total * global_scale