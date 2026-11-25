import numpy as np

class MultimodalAttractiveBasin:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better numerical stability
        x_norm = x / 5.0
        
        # Central attractive basin term, significantly shifted and warped
        basin_term = -np.exp(-np.sum((x_norm - 0.4)**2) / (2 * 0.3**2)) * (1 + 0.5 * np.sin(3 * np.pi * np.sum(x_norm)))
        
        # Enhanced sinusoidal oscillations with exponentially increasing frequencies
        freqs = np.arange(1, self.dim + 1) ** 2
        oscillation_term = np.sum(np.sin(freqs * x_norm) ** 4)
        
        # High-order multimodal component with exponential growth
        multi_term = np.sum(np.exp(3 * np.abs(x_norm)) * np.sin(5 * np.pi * x_norm)**2)
        
        # Saddle point structure with cross-dimensional dependencies
        cross_term = 0.3 * np.sum((x_norm[:-1] ** 2) * x_norm[1:])
        
        # Additional non-separable interaction term using Gaussian radial basis
        radial_term = 0.2 * np.sum(np.exp(-np.sum((x_norm.reshape(1, -1) - x_norm.reshape(-1, 1))**2, axis=1) / (2 * 0.5**2)))
        
        # Combine all terms with varying weights to create complex landscape
        return basin_term + oscillation_term + multi_term + cross_term + radial_term