import numpy as np

class FractalChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-logarithmic component with multi-scale self-similarity
        log_term = np.sum(np.log(1.0 + np.abs(x)) * 
                         np.sin(np.log(1.0 + np.abs(x))) * 
                         np.cos(np.log(2.0 + np.abs(x))))
        
        # Multi-scale chaotic sine modulation with dynamic frequency and amplitude
        freq_mod = np.sum(np.sin(3.0 * x * (1.0 + 0.3 * np.sin(0.5 * x) + 0.2 * np.cos(0.7 * x))) * 
                         np.cos(2.0 * x * (1.0 + 0.4 * np.cos(0.6 * x) + 0.1 * np.sin(0.8 * x))))
        
        # Enhanced ridge structure with multi-dimensional curvature and sinusoidal modulation
        ridge_term = 0.0
        for i in range(self.dim - 1):
            curvature = 0.7 + 0.3 * np.sin(0.3 * x[i] * x[i+1] + 
                                         0.2 * np.sin(x[i]) * np.cos(x[i+1]))
            ridge_term += curvature * (x[i] - x[i+1])**4 + \
                         0.1 * np.sin(2.0 * x[i] + 0.5 * x[i+1]) * (x[i]**2 + x[i+1]**2)
        
        # Advanced chaotic perturbation with multi-layered nonlinearity and dimension-dependent scaling
        chaotic_pert = np.sum(np.exp(-0.15 * x**2) * 
                             np.sin(12.0 * x + np.cos(6.0 * x)) * 
                             np.cos(4.0 * x + np.sin(3.0 * x)) * 
                             np.tanh(0.7 * x) * 
                             np.log(1.0 + 0.5 * np.abs(x)))
        
        # Complex multi-modal component with dynamic amplitude and phase modulation
        modal_term = 0.0
        for i in range(self.dim):
            amp = 1.2 + 0.4 * np.sin(0.15 * i * x[i]) + 0.3 * np.cos(0.08 * i * x[i]) + \
                   0.1 * np.sin(0.25 * i * x[i]**2)
            phase = 0.5 * np.sin(0.1 * i) + 0.3 * np.cos(0.05 * i)
            modal_term += amp * np.sin(6.0 * x[i] + phase) * np.cos(3.0 * x[i] + phase) * \
                         np.exp(-0.02 * x[i]**2) * (1.0 + 0.1 * np.sin(x[i]))
        
        # Dimension-adaptive scaling with fractal-like growth and interaction effects
        scale_factor = 1.0 + 0.15 * np.log(self.dim + 2) + 0.08 * np.sum(np.sin(x)**3) + \
                      0.03 * np.sum(np.cos(x)**2)
        
        # Novel cross-dimensional interaction with exponential decay and multi-scale coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i] * x[j]) / (1.0 + 0.3 * np.abs(x[i] - x[j])) * \
                             np.exp(-0.05 * (x[i]**2 + x[j]**2))
                cross_term += interaction * np.sin(0.5 * (x[i] + x[j]))
        
        # Add a novel fractal-like component with recursive self-similarity
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_component += np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) * \
                               np.exp(-0.1 * np.abs(x[i]))
        
        return scale_factor * (log_term + freq_mod + ridge_term + chaotic_pert + 
                              modal_term + 0.2 * cross_term + 0.1 * fractal_component)