import numpy as np

class MultimodalAttractiveBasin:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better numerical stability
        x_norm = x / 5.0
        
        # Central attractive basin term, significantly shifted and modified
        basin_term = -np.exp(-np.sum((x_norm - 0.3)**2) / (2 * 0.3**2))
        
        # Chaotic sinusoidal oscillations with prime frequency ratios
        oscillation_term = np.sum(np.sin(11 * np.pi * x_norm) ** 2 + 
                                0.5 * np.sin(17 * np.pi * x_norm) ** 2)
        
        # High-order multimodal component with chaotic interactions
        multi_term = np.sum((x_norm**5) * np.sin(5 * np.pi * x_norm)**3)
        
        # Strong cross-dimensional coupling with exponential interaction
        cross_term = 0.7 * np.sum(np.exp(x_norm[:-1] * x_norm[1:]) - 1)
        
        # Additional chaotic polynomial coupling term
        poly_term = 0.3 * np.sum((x_norm**4 + 0.5 * x_norm**2) * np.cos(3 * np.pi * x_norm))
        
        # Combine all terms with dynamic weighting
        return basin_term + oscillation_term + multi_term + cross_term + poly_term