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
        
        # Multi-scale chaotic sine modulation with dynamic frequency adjustment
        freq_mod = np.sum(np.sin(2.0 * x * (1.0 + 0.5 * np.sin(0.3 * x) * np.cos(0.1 * x))) * 
                         np.cos(1.5 * x * (1.0 + 0.3 * np.cos(0.4 * x)) * np.sin(0.2 * x)))
        
        # Dynamic ridge structure with time-varying curvature and sinusoidal shift
        ridge_term = 0.0
        for i in range(self.dim - 1):
            curvature = 0.5 + 0.5 * np.sin(0.2 * x[i] * x[i+1] + 
                                         0.1 * np.sin(x[i]) * np.cos(x[i+1]))
            ridge_term += curvature * (x[i] - x[i+1])**4 * np.exp(-0.1 * (x[i]**2 + x[i+1]**2))
        
        # Advanced chaotic perturbation with hyperbolic and trigonometric coupling
        chaotic_pert = np.sum(np.exp(-0.1 * x**2) * 
                             np.sin(10.0 * x + np.cos(5.0 * x)) * 
                             np.cos(3.0 * x + np.sin(2.0 * x)) * 
                             np.tanh(0.5 * x) * 
                             np.log(1.0 + np.abs(x)))
        
        # Multi-modal component with adaptive amplitude and dynamic phase shift
        modal_term = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.1 * i * x[i]) + 0.2 * np.cos(0.05 * i * x[i])
            phase_shift = 0.3 * np.sin(0.2 * i * x[i]) * np.cos(0.1 * i * x[i])
            modal_term += amp * np.sin(5.0 * x[i] + phase_shift) * np.cos(2.0 * x[i] + phase_shift) * np.exp(-0.01 * x[i]**2)
        
        # Dimensionality-adaptive scaling with exponential and logarithmic components
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1) + 0.05 * np.sum(np.sin(x)**2) + 0.02 * np.sum(np.cos(x)**2)
        
        # Cross-dimensional interaction with fractal-weighted coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.sin(0.1 * (i + j)) * np.cos(0.05 * (i - j))
                cross_term += weight * (x[i] * x[j]) / (1.0 + 0.5 * np.abs(x[i] - x[j]))
        
        # Add a novel hyper-fractal component with recursive scaling
        hyper_fractal = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * 
                              np.exp(-0.05 * x**2) * 
                              np.log(1.0 + np.abs(x)) * 
                              np.sin(np.log(1.0 + np.abs(x))))
        
        return scale_factor * (log_term + freq_mod + ridge_term + chaotic_pert + modal_term + 0.15 * cross_term + hyper_fractal)