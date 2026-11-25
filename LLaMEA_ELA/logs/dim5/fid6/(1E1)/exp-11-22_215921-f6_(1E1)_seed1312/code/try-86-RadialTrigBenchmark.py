import numpy as np

class RadialTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with multiple peaks
        r = np.sqrt(np.sum(x_norm**2, axis=-1, keepdims=True))
        radial_term = 2.0 * np.sin(8 * np.pi * r) * np.exp(-r**2)
        
        # Angular components with varying frequencies and amplitudes
        if self.dim >= 2:
            angles = np.arctan2(x_norm[:, 1], x_norm[:, 0])
            angular_term = 1.5 * np.sum(np.sin(12 * angles) * np.cos(7 * angles) * 
                                      np.exp(-0.5 * (x_norm[:, 0]**2 + x_norm[:, 1]**2)), axis=-1, keepdims=True)
            
            # Cross-dimensional coupling with sine and cosine interactions
            cross_term = 0.8 * np.sum(np.sin(5 * x_norm[:, :-1]) * np.cos(5 * x_norm[:, 1:]) *
                                    (x_norm[:, :-1]**2 + x_norm[:, 1:]**2), axis=-1, keepdims=True)
        else:
            angular_term = 0
            cross_term = 0
            
        # Multi-scale periodic components with different periods and amplitudes
        period_terms = np.sum(
            [0.5 * np.sin((i+1) * np.pi * x_norm) * np.cos((i+1) * np.pi * x_norm) * 
             np.exp(-0.2 * (x_norm**2)) for i in range(3)], axis=0
        )
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Combine all terms with appropriate scaling
        total = condition_factor * (np.sum(radial_term) + 
                                  np.sum(angular_term) + 
                                  np.sum(cross_term) + 
                                  np.sum(period_terms))
        
        return total