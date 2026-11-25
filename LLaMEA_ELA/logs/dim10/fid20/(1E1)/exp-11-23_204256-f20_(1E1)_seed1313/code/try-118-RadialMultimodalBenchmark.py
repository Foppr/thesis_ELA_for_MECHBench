import numpy as np

class RadialMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with polynomial scaling
        r = np.sqrt(np.sum(x_normalized**2))
        radial_term = 0.5 * r**4 + 0.3 * r**2
        
        # Sinusoidal oscillations in radial direction with varying frequencies
        radial_oscillation = np.sin(10 * r) * np.cos(15 * r) + 0.5 * np.sin(25 * r)
        
        # Angular components with cross-dimension interactions
        angular_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angular_terms += np.sin(x_normalized[i] * x_normalized[j]) * (i + j + 1)
        
        # Polynomial conditioning with dimension-dependent weights
        poly_cond = 0.0
        for i in range(self.dim):
            poly_cond += (i + 1) * x_normalized[i]**6
        
        # Add noise-like perturbations
        noise = 0.1 * np.sum(np.sin(30 * x_normalized) ** 2)
        
        # Combine all terms with adaptive scaling based on dimensionality
        adaptive_scale = 1.0 + 0.5 * np.log(1.0 + self.dim / 10.0)
        
        return adaptive_scale * (radial_term + radial_oscillation + angular_terms + poly_cond + noise)