import numpy as np

class AdaptiveSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute radial distance
        r = np.sqrt(np.sum(x**2))
        
        # Polynomial base with adaptive conditioning
        result = 0.0
        for i in range(self.dim):
            result += 0.5 * x[i]**4 + 0.3 * x[i]**3 + 0.1 * x[i]**2 + 0.05 * x[i]
            
        # Add trigonometric components with varying frequencies
        for i in range(self.dim):
            result += 0.2 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) + 0.1 * np.sin(5.0 * x[i])
            
        # Radial basis function component with multiple centers
        rb_result = 0.0
        centers = np.linspace(-3.0, 3.0, min(5, self.dim))
        for i, center in enumerate(centers):
            if i < self.dim:
                rb_result += np.exp(-0.5 * ((x[i] - center) / 0.5)**2)
                
        result += 0.3 * rb_result
        
        # Spherical shell structure with adaptive scaling
        if r > 0:
            shell_factor = 1.0 + 0.5 * np.sin(2.0 * r) * np.cos(1.5 * r)
            result *= shell_factor
            
        # Add cross-dimensional coupling with adaptive weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                coupling += 0.1 * x[i] * x[j] * np.sin(0.5 * (x[i] + x[j]))
        result += coupling
        
        # Add noise-like perturbations for increased complexity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.02 * np.sin(20.0 * x[i]) * np.cos(15.0 * x[i])
        result += noise
        
        return result