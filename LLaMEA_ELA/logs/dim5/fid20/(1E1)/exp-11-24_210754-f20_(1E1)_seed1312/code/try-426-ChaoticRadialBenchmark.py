import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r**2 * (1.0 + 0.3 * np.sin(10.0 * r) * np.cos(7.0 * r))
        
        # Sinusoidal waves in each dimension with varying frequencies and amplitudes
        wave_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 2.0 * (i + 1) * np.pi / 5.0
            amp = 1.0 + 0.5 * np.sin(i)
            wave_sum += amp * np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Polynomial chaos component with fractional powers and random coefficients
        poly_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            coeff = 0.8 + 0.4 * np.sin(i * 0.7)
            poly_term += coeff * xi**3.2 + 0.6 * xi**2.7 + 0.3 * xi**1.9
        
        # Cross-dimensional interaction terms with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2))
        
        # Asymmetric saddle points with exponential decay
        saddle_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            saddle_term += (xi**4 - 2.0 * xi**2) * np.exp(-0.1 * np.abs(xi))
        
        # Global scaling and normalization
        total = radial_term + wave_sum + poly_term + cross_term + saddle_term
        return total / self.dim