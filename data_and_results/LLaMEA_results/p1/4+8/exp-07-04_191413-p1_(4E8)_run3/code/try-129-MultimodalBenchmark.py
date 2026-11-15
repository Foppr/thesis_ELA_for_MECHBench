import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Center the search space at origin for easier computation
        x_centered = x - 0.0
        
        # Normalize to [-1, 1] range
        x_normalized = x_centered / 5.0
        
        # Radial quadratic term for conditioning
        r_squared = np.sum(x_normalized**2)
        radial_quad = 0.5 * r_squared
        
        # Polynomial conditioning with varying degrees
        poly_cond = np.sum(x_normalized**4 + 0.3 * x_normalized**6)
        
        # Sinusoidal perturbations with multiple frequencies
        sin_perturb = np.sum(np.sin(2 * np.pi * x_normalized) + 
                            0.5 * np.sin(5 * np.pi * x_normalized) + 
                            0.3 * np.sin(10 * np.pi * x_normalized))
        
        # Cross-dimensional coupling with chaotic interaction
        cross_coupling = 0.2 * np.sum(np.sin(3 * np.pi * x_normalized[:-1]) * 
                                    np.cos(4 * np.pi * x_normalized[1:]) * 
                                    (x_normalized[:-1]**2 + x_normalized[1:]**2))
        
        # Radial multi-modal component with multiple peaks
        radial_multi = 0.1 * np.sum(np.sin(15 * np.pi * r_squared) * 
                                  np.exp(-0.5 * r_squared))
        
        # Chaotic sine-wave component with non-linear modulation
        chaotic = 0.25 * np.sum(np.sin(7 * np.pi * x_normalized**3) * 
                               np.cos(11 * np.pi * x_normalized) * 
                               np.exp(-0.3 * x_normalized**2))
        
        # Add a global scaling factor and combine all terms
        return radial_quad + 0.7 * poly_cond + 0.5 * sin_perturb + cross_coupling + radial_multi + chaotic