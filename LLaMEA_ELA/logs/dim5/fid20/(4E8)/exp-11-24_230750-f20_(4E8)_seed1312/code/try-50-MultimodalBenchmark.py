import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logarithmic terms with varying base and amplitude
        log_terms = np.sum(np.log(1.0 + np.abs(x)) * np.sin(3.0 * np.log(1.0 + np.abs(x))) * np.cos(2.0 * np.log(1.0 + np.abs(x))))
        
        # Spherical harmonics with varying degree and order
        sph_harmonics = 0.0
        for i in range(self.dim):
            r = np.sqrt(np.sum(x**2))
            theta = np.arctan2(x[i], x[(i+1)%self.dim]) if self.dim > 1 else 0.0
            phi = np.arccos(x[i] / (r + 1e-8))
            sph_harmonics += np.sin((i+1) * theta) * np.cos((i+2) * phi)
        
        # Adaptive noise component with dynamic scaling based on position
        noise = np.sum(np.random.normal(0, 0.1 * (1.0 + np.abs(x)), self.dim))
        
        # Multi-scale exponential decay with sinusoidal modulation
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.sin(4.0 * x) * np.cos(6.0 * x))
        
        # Polynomial interaction terms with non-integer exponents and random coefficients
        poly_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_terms += (x[i]**1.5 * x[j]**2.3 + x[i]**2.7 * x[j]**1.8) * np.random.uniform(0.5, 1.5)
        
        # Combined function value
        return log_terms + sph_harmonics + noise + exp_decay + poly_terms