import numpy as np

class ExponentialRadialTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize enhanced adaptive parameters for varied conditioning
        self.scale_factors = [1.0 + 0.6 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.freq_factors = [1.5 + 1.2 * np.cos(i * np.pi / (dim + 2)) for i in range(dim)]
        self.cross_coupling = [[0.6 * np.sin(i * j * np.pi / (dim + 1)) + 0.3 * np.cos(i * j * np.pi / (dim + 3)) for j in range(dim)] for i in range(dim)]
        # Add chaotic perturbations
        self.perturbations = [0.2 * np.sin(i * np.pi / (dim + 5)) + 0.1 * np.cos(i * np.pi / (dim + 6)) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential radial component with adaptive scaling and chaotic modulation
        norm = np.linalg.norm(x)
        if norm > 0:
            radial_term = np.exp(-0.2 * norm) * (norm - 1.2)**3 * (1 + 0.4 * np.sin(norm) * np.cos(norm))
        else:
            radial_term = 0
            
        # Augmented trigonometric cross-dimensional interactions with chaotic coupling
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.cross_coupling[i][j]
                cross_term += coupling * np.sin(self.freq_factors[i] * x[i]) * np.cos(self.freq_factors[j] * x[j])
                
        # Enhanced dimensional sinusoidal components with varying scales and perturbations
        sin_term = 0
        for i in range(self.dim):
            scale = self.scale_factors[i]
            perturbation = self.perturbations[i]
            sin_term += scale * (np.sin(self.freq_factors[i] * x[i]) + 0.7 * np.cos(2 * self.freq_factors[i] * x[i]) + perturbation)
            
        # Quadratic shaping with enhanced chaotic perturbations and interaction terms
        quad_term = 0
        for i in range(self.dim):
            perturbation = 0.2 * np.sin(i * np.pi / (self.dim + 4)) + 0.15 * np.cos(i * np.pi / (self.dim + 7))
            quad_term += (x[i]**2 + perturbation) * (1 + 0.2 * np.cos(i) + 0.1 * np.sin(2 * i))
            
        # Additional chaotic interaction term between dimensions
        chaos_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_term += 0.3 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Adaptive conditioning factor based on dimension with chaotic modulation
        adapt_factor = 1.2 + 0.4 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / 4)
        
        # Combine all components with proper weighting and add chaotic offset
        return adapt_factor * (radial_term + cross_term + sin_term + quad_term + chaos_term) + 0.2 * self.dim