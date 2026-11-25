import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay with multi-scale polynomial modulation
        f1 = np.sum(np.exp(-np.abs(x_norm)**2.0) * (np.sin(4 * np.pi * x_norm)**3 + 0.15 * np.cos(6 * x_norm) + 0.05 * np.sin(8 * x_norm)))
        
        # Modified trigonometric coupling with dynamic frequency shifts and amplitude modulation
        f2 = np.sum(np.sin(9 * x_norm + 0.4 * np.sin(3 * x_norm)) * np.cos(5 * x_norm + 0.2 * np.cos(4 * x_norm)) * (1 + 0.1 * np.sin(2 * x_norm)))
        
        # Improved asymmetric gradient field with multi-scale weights and chaotic perturbations
        f3 = np.sum(np.exp(-x_norm**2.5) * (x_norm**4 - 0.4 * x_norm**3 + 0.2 * x_norm**2 + 0.1 * x_norm + 0.03 * np.sin(12 * x_norm)))
        
        # Enhanced saddle-point interaction with cross-dimensional coupling and non-linear interactions
        f4 = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**3 + 0.15 * (x_norm[:-1] * x_norm[1:])**3 + 0.05 * (x_norm[:-1] + x_norm[1:])**4)
        
        # Modified chaotic oscillation terms with variable amplitudes and time-varying frequencies
        f5 = np.sum(np.sin(15 * x_norm) * np.cos(13 * x_norm) * np.exp(-0.4 * x_norm**2) * (1 + 0.25 * np.sin(8 * x_norm) + 0.1 * np.cos(9 * x_norm)))
        
        # Adjusted cubic polynomial with enhanced nonlinearity and multi-scale oscillations
        f6 = np.sum(np.sign(x_norm) * np.abs(x_norm)**4.0 * np.cos(7 * x_norm) * (1 + 0.15 * np.sin(5 * x_norm) + 0.08 * np.cos(6 * x_norm)))
        
        # Improved cross-dimensional interaction with adaptive weights and multi-scale coupling
        f7 = np.sum(np.exp(-np.abs(x_norm[:-1] + x_norm[1:])**1.5) * (x_norm[:-1]**3 + x_norm[1:]**3 + 0.1 * x_norm[:-1] * x_norm[1:] + 0.08 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Enhanced chaotic perturbation with adaptive magnitude and multi-scale noise
        noise = 0.005 * np.random.random()
        
        return 0.35 * f1 + 0.65 * f2 + 0.45 * f3 + 0.75 * f4 + 0.35 * f5 + 0.85 * f6 + 0.25 * f7 + noise