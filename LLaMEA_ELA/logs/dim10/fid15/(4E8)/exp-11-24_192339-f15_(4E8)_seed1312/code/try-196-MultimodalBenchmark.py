import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with varying frequencies
        sin_component = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.2 * x[i])
            sin_component += np.sin(freq * x[i]) * np.cos(0.3 * x[i]**2)
        
        # Radial basis function with adaptive width and asymmetric influence
        rbf_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                width = 1.0 + 0.3 * np.sin(0.4 * x[i])
                # Asymmetric coupling based on dimension order
                asym_coupling = (x[i]**2 + x[j]) * np.exp(-0.5 * (dist / width)**2)
                rbf_component += asym_coupling
        
        # Polynomial coupling with hyperbolic tangent modulation
        poly_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                tan_mod = np.tanh(x[i] * x[j])
                poly_term = (x[i]**3 + x[j]**2) * tan_mod * np.exp(-0.1 * (x[i] - x[j])**2)
                poly_component += poly_term
        
        # Asymmetric polynomial interaction with fractal-like scaling
        asym_poly = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like scaling factor
                scale = 1.0 + 0.2 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[j])
                asym_poly += (x[i] - x[j])**3 * scale
        
        # Exponential decay with dimension-dependent modulation
        exp_component = 0
        for i in range(self.dim):
            exp_component += np.exp(-0.5 * x[i]**2) * np.sin(0.1 * self.dim * x[i])
        
        # Global scaling factor based on problem dimensionality
        scale_factor = 1.0 + 0.1 * np.sin(0.5 * self.dim)
        
        # Combine all components with optimized weights
        return scale_factor * (0.25 * sin_component + 0.3 * rbf_component + 
                              0.2 * poly_component + 0.15 * asym_poly + 0.1 * exp_component)