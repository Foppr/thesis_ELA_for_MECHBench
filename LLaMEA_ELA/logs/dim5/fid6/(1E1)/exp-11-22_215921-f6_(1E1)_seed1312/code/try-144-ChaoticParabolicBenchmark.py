import numpy as np

class ChaoticParabolicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic tent map component with parameter control
        tent_map = np.sum(1.0 - 2.0 * np.abs(x_norm - 0.5))
        
        # Adaptive parabolic valleys with dynamic curvature
        parabola = np.sum(0.5 * (x_norm**2) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Cross-dimensional coupling with sine-based interaction
        coupling = np.sum(np.sin(3 * np.pi * x_norm[:-1]) * np.cos(2 * np.pi * x_norm[1:]) * 
                         np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Multi-modal Gaussian peaks with chaotic positioning
        gaussian_peaks = 0.7 * np.sum(np.exp(-3 * ((x_norm - 0.4 * np.sin(5 * x_norm))**2 + 
                                                  (x_norm - 0.3 * np.cos(4 * x_norm))**2)))
        
        # Saddle point structure with polynomial interactions
        saddle = np.sum((x_norm[:-1]**3 - x_norm[1:]**3) * (x_norm[:-1] - x_norm[1:]))
        
        # High-dimensional conditioning with exponential scaling
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combine all terms with chaotic weighting
        return condition_factor * (tent_map + parabola + coupling + gaussian_peaks + saddle)