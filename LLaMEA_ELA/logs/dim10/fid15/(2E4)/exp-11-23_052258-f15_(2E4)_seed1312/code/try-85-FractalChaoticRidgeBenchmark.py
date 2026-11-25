import numpy as np

class FractalChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic scaling component with fractal-like self-similarity
        log_term = np.sum(np.log(1.0 + np.abs(x)) * np.sin(np.log(1.0 + np.abs(x))))
        
        # Multi-scale sine modulation with adaptive frequency
        freq_mod = np.sum(np.sin(2.0 * x * (1.0 + 0.5 * np.sin(0.3 * x))) * 
                         np.cos(1.5 * x * (1.0 + 0.3 * np.cos(0.4 * x))))
        
        # Spatially varying ridge structure with curvature modulation and sinusoidal shift
        ridge_term = 0.0
        for i in range(self.dim - 1):
            curvature = 0.5 + 0.5 * np.sin(0.2 * x[i] * x[i+1] + 0.1 * np.sin(x[i]))
            ridge_term += curvature * (x[i] - x[i+1])**4
        
        # Chaotic perturbation with exponential decay and enhanced nonlinearity
        chaotic_pert = np.sum(np.exp(-0.1 * x**2) * 
                             np.sin(10.0 * x + np.cos(5.0 * x)) * 
                             np.cos(3.0 * x + np.sin(2.0 * x)) * 
                             np.tanh(0.5 * x))
        
        # Multi-modal component with varying amplitude and increased complexity
        modal_term = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.1 * i * x[i]) + 0.2 * np.cos(0.05 * i * x[i])
            modal_term += amp * np.sin(5.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.01 * x[i]**2)
        
        # Enhanced adaptive scaling based on dimensionality and interaction terms
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1) + 0.05 * np.sum(np.sin(x)**2)
        
        # Add cross-dimensional interaction for increased complexity with modified weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) / (1.0 + 0.5 * np.abs(x[i] - x[j]))
        
        # Slight mutation: Adjusted chaotic perturbation with additional sinusoidal modulation
        chaotic_pert = np.sum(np.exp(-0.1 * x**2) * 
                             np.sin(10.0 * x + np.cos(5.0 * x)) * 
                             np.cos(3.0 * x + np.sin(2.0 * x)) * 
                             np.tanh(0.5 * x) * 
                             np.sin(0.5 * x))
        
        return scale_factor * (log_term + freq_mod + ridge_term + chaotic_pert + modal_term + 0.15 * cross_term)