import numpy as np

class ChaoticSaddlePeak:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic saddle term using sine-based chaotic map
        chaotic_term = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Embedded Gaussian peaks with varying heights and positions
        peak_term = 0.0
        for i in range(8):
            # Generate peak positions and heights dynamically
            peak_pos = np.sin(i * np.pi / 4) * 0.5
            peak_height = 1.0 + 0.5 * np.sin(i * np.pi / 3)
            sigma = 0.3 + 0.2 * np.cos(i * np.pi / 5)
            
            # Gaussian peak contribution
            peak_contribution = peak_height * np.exp(-np.sum((x_norm - peak_pos)**2) / (2 * sigma**2))
            peak_term += peak_contribution
        
        # Cross-dimensional coupling with polynomial interactions
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(3 * np.pi * x_norm[i] * x_norm[i+1])
        
        # Add a global trend with sinusoidal modulation
        trend_term = 0.5 * np.sum(np.sin(2 * np.pi * x_norm)**3)
        
        # Combine all terms
        return chaotic_term + peak_term + cross_term + trend_term