import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component with adaptive radius
        spherical = np.sum((x / (1.0 + 0.1 * np.abs(x)))**2)
        
        # Saddle-point structure with alternating signs and varying curvature
        saddle = np.sum(x[:-1] * x[1:] * np.sin(2.0 * np.pi * x[:-1]) * np.cos(2.0 * np.pi * x[1:]))
        
        # Fractal-like self-similar structure using iterative scaling
        fractal = 0.0
        for i in range(min(5, self.dim)):
            scale = 2.0**(i - self.dim/3.0)
            fractal += scale * np.sin(scale * x[i]) * np.cos(scale * x[i]**2)
        
        # Adaptive dimensionality scaling with exponential weighting
        dim_scaling = np.sum(np.exp(-0.5 * (np.arange(self.dim) - self.dim/2.0)**2 / self.dim))
        
        # Dynamic noise component with frequency modulation based on position
        noise = 0.05 * np.sum(np.random.rand() * np.sin(10.0 * x + np.arange(self.dim)) * 
                             np.cos(5.0 * x + np.arange(self.dim)))
        
        # Coupling terms with multi-scale interactions and variable strength
        coupling = 0.3 * np.sum(x[:-2]**3 * x[1:-1]**2 * x[2:]**4 + 
                              x[:-2]**2 * x[1:-1]**4 * x[2:]**3)
        
        # Exponential barrier near boundaries with adaptive steepness
        barrier = np.sum(np.exp(5.0 / (5.0 - np.abs(x)) - 5.0) * (np.abs(x) >= 4.5))
        
        # Combined fitness value with weighted components
        return (1.0 + 0.2 * dim_scaling) * (spherical + saddle + fractal + coupling + noise) + barrier