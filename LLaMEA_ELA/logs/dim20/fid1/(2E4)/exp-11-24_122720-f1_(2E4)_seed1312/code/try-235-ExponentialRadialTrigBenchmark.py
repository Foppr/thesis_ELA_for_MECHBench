import numpy as np

class ExponentialRadialTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive parameters for varied conditioning
        self.scale_factors = [1.0 + 0.4 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.freq_factors = [2.0 + 0.3 * np.cos(i * np.pi / (dim + 2)) for i in range(dim)]
        self.cross_coupling = [[0.4 * np.sin(i * j * np.pi / (dim + 1)) for j in range(dim)] for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential radial component with sharper curvature
        norm = np.linalg.norm(x)
        if norm > 0:
            radial_term = np.exp(-0.15 * norm) * (norm - 1.5)**3 * (1 + 0.3 * np.sin(norm))
        else:
            radial_term = 0
            
        # Modified trigonometric cross-dimensional interactions
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.cross_coupling[i][j]
                cross_term += coupling * np.sin(self.freq_factors[i] * x[i]) * np.sin(self.freq_factors[j] * x[j])
                
        # Dimensional sinusoidal components with enhanced scaling
        sin_term = 0
        for i in range(self.dim):
            scale = self.scale_factors[i]
            sin_term += scale * (np.sin(self.freq_factors[i] * x[i]) + 0.6 * np.cos(2 * self.freq_factors[i] * x[i]))
            
        # Quadratic shaping with stronger chaotic perturbations
        quad_term = 0
        for i in range(self.dim):
            perturbation = 0.15 * np.sin(i * np.pi / (self.dim + 3))
            quad_term += (x[i]**2 + perturbation) * (1 + 0.15 * np.cos(i))
            
        # Enhanced adaptive conditioning factor
        adapt_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combine all components with adjusted weighting
        return adapt_factor * (radial_term + cross_term + sin_term + quad_term) + 0.15 * self.dim