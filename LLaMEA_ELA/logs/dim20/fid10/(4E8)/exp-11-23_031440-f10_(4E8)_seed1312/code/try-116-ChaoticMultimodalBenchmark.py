import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical component with dynamic radius scaling
        spherical = np.sum(x_norm**2)
        
        # Saddle-like component with alternating signs and varying curvature
        saddle = 0.0
        for i in range(self.dim):
            saddle += (-1)**i * (x_norm[i]**2 - x_norm[(i+1) % self.dim]**2)
        
        # Fractal-inspired component using fractional Brownian motion-like scaling
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2**(i+1) * np.pi * x_norm[i]) * (1.0 / (2**(i+1)))
        
        # Dynamic scaling factor based on distance from origin
        r = np.sqrt(np.sum(x_norm**2))
        scale_factor = 1.0 + 3.0 * np.sin(5 * np.pi * r)**2
        
        # Cross-dimensional coupling with phase-shifted interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin(np.pi * (x_norm[i] + x_norm[j])) * np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Asymmetric penalty terms to increase conditioning difficulty
        asym_penalty = 0.0
        for i in range(self.dim):
            if x_norm[i] > 0:
                asym_penalty += 0.5 * x_norm[i]**3
            else:
                asym_penalty += 0.3 * x_norm[i]**4
        
        # Combine all components with weighted contributions
        result = scale_factor * (0.6 * spherical + 0.3 * saddle + 0.2 * fractal + 
                                0.4 * coupling + 0.1 * asym_penalty)
        
        return result