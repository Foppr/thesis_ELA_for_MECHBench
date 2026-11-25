import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay term with chaotic modulation
        exp_term = np.sum(np.exp(-np.abs(x_norm)) * np.sin(2 * np.pi * x_norm * (1 + 0.5 * np.sin(self.dim * x_norm))))
        
        # Trigonometric wave interference creating complex landscape
        wave_term = np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm) * np.sin(3 * x_norm**2))
        
        # Adaptive gradient modulation based on dimensionality
        grad_mod = np.sum((x_norm**2) * np.cos(self.dim * x_norm) * np.sin(x_norm))
        
        # Multi-scale harmonic interaction
        harmonic_term = np.sum(np.sin(np.pi * x_norm * np.exp(0.3 * x_norm)) * np.cos(0.5 * np.pi * x_norm**3))
        
        # Chaotic phase coupling with exponential scaling
        phase_coupling = np.sum(np.exp(-0.5 * x_norm**2) * np.sin(np.pi * x_norm * (1 + 0.2 * np.cos(self.dim * x_norm))))
        
        # Dimension-adaptive penalty term
        penalty = 0.1 * self.dim * np.sum(np.abs(x_norm)**3)
        
        # Combine all terms with dynamic weighting
        return (0.4 * exp_term + 0.3 * wave_term + 0.2 * grad_mod + 0.05 * harmonic_term + 
                0.03 * phase_coupling + penalty) / (1.0 + 0.01 * self.dim)