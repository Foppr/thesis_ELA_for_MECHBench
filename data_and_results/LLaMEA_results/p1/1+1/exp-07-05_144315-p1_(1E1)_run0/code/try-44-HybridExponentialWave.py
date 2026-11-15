import numpy as np

class HybridExponentialWave:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with varying rates
        exp_decay = np.sum(np.exp(-0.5 * np.abs(x)) * np.exp(-0.1 * x**2))
        
        # Trigonometric wave interference with multiple frequencies
        wave_interference = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * np.exp(-0.05 * np.abs(x)))
        
        # Polynomial penalty terms with different degrees
        poly_penalty = 0.0
        for i in range(self.dim):
            poly_penalty += (x[i]**5) * np.exp(-0.1 * x[i]**2) + 0.1 * (x[i]**4) * np.sin(0.5 * x[i])
        
        # Asymmetric Gaussian peaks with different scales
        asymmetric_peaks = 0.0
        for i in range(1, 4):
            center = np.full(self.dim, i * 0.8)
            # Asymmetric scaling based on sign of coordinates
            scale = np.exp(-0.5 * np.sum((x - center)**2)) * (1 + 0.3 * np.sum(np.sign(x) * (x - center)))
            asymmetric_peaks += scale * np.sin(2 * np.pi * np.sum(x - center))
        
        # Saddle point structure using cross-terms
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited cross-terms for sparsity
                saddle += (x[i] * x[j]) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Global scaling with exponential growth
        global_scale = 1.0 + 0.5 * np.exp(0.1 * np.sum(x**2))
        
        # Combine all components with different weights
        return exp_decay + 0.7 * wave_interference + 0.3 * poly_penalty + 0.4 * asymmetric_peaks + 0.2 * saddle + global_scale