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
        
        # Spatially varying ridge structure with curvature modulation
        ridge_term = 0.0
        for i in range(self.dim - 1):
            curvature = 0.5 + 0.5 * np.sin(0.2 * x[i] * x[i+1] + 0.1 * np.cos(x[i]))
            ridge_term += curvature * (x[i] - x[i+1])**4
        
        # Chaotic perturbation with exponential decay - modified coefficients
        chaotic_pert = np.sum(np.exp(-0.15 * x**2) * 
                             np.sin(12.0 * x + np.cos(6.0 * x)) * 
                             np.cos(3.5 * x + np.sin(2.5 * x)))
        
        # Multi-modal component with varying amplitude - modified frequencies
        modal_term = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.6 * np.sin(0.15 * i * x[i])
            modal_term += amp * np.sin(6.0 * x[i]) * np.cos(2.5 * x[i])
        
        # Adaptive scaling based on dimensionality - modified factor
        scale_factor = 1.0 + 0.15 * np.log(self.dim + 1)
        
        return scale_factor * (log_term + freq_mod + ridge_term + chaotic_pert + modal_term)