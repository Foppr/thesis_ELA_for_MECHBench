import numpy as np

class FractalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors
        self.fractal_factors = np.array([1.0, 0.5, 0.25, 0.125][:min(4, dim)]) if dim > 0 else np.array([])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with dynamic scaling
        r = np.sqrt(np.sum(x**2))
        rbf_term = np.exp(-0.1 * r) * np.sin(3.0 * r)
        
        # Self-similar fractal pattern using multiple scales
        fractal_sum = 0.0
        for i, factor in enumerate(self.fractal_factors):
            if i < len(x):
                fractal_sum += factor * np.sin((2**i) * x[i]) * np.cos((2**i) * x[i])
        
        # Multi-scale harmonic modulation
        harmonic_term = 0.0
        for i in range(min(5, self.dim)):
            freq = 2**(i+1)
            harmonic_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Polynomial distortion with variable exponents
        poly_distortion = np.sum((x**4.0 + 0.5 * x**3.0 - 0.2 * x**2.0 + 0.8 * x + 1.0)**1.5)
        
        # Dynamic coupling between dimensions
        coupling_term = 0.0
        for i in range(self.dim-1):
            coupling_term += np.sin(x[i] * x[i+1]) * np.exp(-0.05 * (x[i]**2 + x[i+1]**2))
            
        # Combine all components with adaptive weights
        return 0.3 * rbf_term + 0.25 * fractal_sum + 0.2 * harmonic_term + 0.15 * poly_distortion + 0.1 * coupling_term + 2.1