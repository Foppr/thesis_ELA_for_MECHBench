import numpy as np

class MultimodalAttractiveBasin:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better numerical stability
        x_norm = x / 5.0
        
        # Central attractive basin term with exponential decay and noise
        basin_term = -np.exp(-np.sum((x_norm - 0.3)**2) / (2 * 0.3**2)) * np.exp(-np.sum(np.abs(x_norm)) / 2)
        
        # High-frequency sinusoidal oscillations with chaotic coupling
        oscillation_term = np.sum(np.sin(15 * np.pi * x_norm) ** 4 + 0.5 * np.sin(23 * np.pi * x_norm) ** 2)
        
        # Higher-order multimodal component with exponential growth and chaotic modulation
        multi_term = np.sum((x_norm**5) * np.exp(-x_norm**2) * np.sin(6 * np.pi * x_norm)**3)
        
        # Cross-dimensional interaction with exponentially decaying weights
        cross_term = 0.3 * np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * (x_norm[:-1] * x_norm[1:]))
        
        # Additional chaotic modulation term to increase conditioning difficulty
        chaos_term = 0.2 * np.sum(np.sin(np.exp(x_norm)) * np.cos(np.exp(2 * x_norm)))
        
        # Combine all terms
        return basin_term + oscillation_term + multi_term + cross_term + chaos_term