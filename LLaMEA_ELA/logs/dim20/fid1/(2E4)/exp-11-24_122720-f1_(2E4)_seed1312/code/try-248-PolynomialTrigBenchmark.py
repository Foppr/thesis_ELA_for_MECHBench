import numpy as np

class PolynomialTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive parameters for varied conditioning
        self.scale_factors = [1.0 + 0.5 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.freq_factors = [1.0 + 0.7 * np.cos(i * np.pi / (dim + 2)) for i in range(dim)]
        self.cross_coupling = [[0.3 * np.cos(i * j * np.pi / (dim + 1)) for j in range(dim)] for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial radial component with adaptive scaling
        norm = np.linalg.norm(x)
        if norm > 0:
            radial_term = (norm / 5.0)**4 * (1 + 0.2 * np.cos(norm))
        else:
            radial_term = 0
            
        # Trigonometric cross-dimensional interactions
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.cross_coupling[i][j]
                cross_term += coupling * np.cos(self.freq_factors[i] * x[i]) * np.sin(self.freq_factors[j] * x[j])
                
        # Dimensional polynomial components with varying scales
        poly_term = 0
        for i in range(self.dim):
            scale = self.scale_factors[i]
            poly_term += scale * (x[i]**3 + 0.5 * x[i]**2 + 0.3 * x[i])
            
        # Quadratic shaping with chaotic perturbations
        quad_term = 0
        for i in range(self.dim):
            perturbation = 0.2 * np.cos(i * np.pi / (self.dim + 3))
            quad_term += (x[i]**2 + perturbation) * (1 + 0.1 * np.sin(i))
            
        # Adaptive conditioning factor based on dimension
        adapt_factor = 1.0 + 0.4 * np.log(self.dim + 1)
        
        # Combine all components with proper weighting
        return adapt_factor * (radial_term + cross_term + poly_term + quad_term) + 0.2 * self.dim