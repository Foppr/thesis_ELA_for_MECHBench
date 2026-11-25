import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic_term = np.sum(x_norm**2)
        
        # Enhanced chaotic sinusoidal component with multiple frequency combinations
        sin_term = np.sum(np.sin(7 * np.pi * x_norm) * np.sin(11 * np.pi * x_norm) * 
                         np.sin(17 * np.pi * x_norm))
        
        # Increased polynomial penalties with non-uniform exponents and adaptive scaling
        poly_term = np.sum(x_norm**5) + 0.03 * np.sum(x_norm**9)
        
        # Novel cross-dimensional interaction terms with weighted coupling
        interaction_term = 0.15 * np.sum((x_norm[:-1] - x_norm[1:])**2) + \
                          0.08 * np.sum((x_norm[:-2] + x_norm[2:])**2) + \
                          0.05 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Additional chaotic perturbation with non-linear coupling
        chaotic_perturbation = 0.02 * np.sum(np.sin(41 * x_norm) * np.cos(23 * x_norm) * 
                                            np.sin(13 * x_norm))
        
        # Add a new term that creates multiple local minima through coupled polynomial interactions
        coupled_poly = 0.01 * np.sum((x_norm[:-1]**2 + x_norm[1:]**2 - 0.5)**3)
        
        # Introduce multi-scale chaotic coupling with exponentially increasing frequencies
        multi_scale_coupling = 0.04 * np.sum(np.sin(2**(np.arange(self.dim-1)) * np.pi * x_norm[:-1]) * 
                                           np.cos(3**(np.arange(self.dim-1)) * np.pi * x_norm[1:]))
        
        # Add a high-frequency oscillatory component to increase conditioning difficulty
        high_freq_osc = 0.015 * np.sum(np.sin(100 * x_norm) * np.cos(77 * x_norm))
        
        # Introduce a novel term based on fourth-order Chebyshev polynomials for enhanced multimodality
        chebyshev_term = 0.02 * np.sum(np.cos(4 * np.arccos(x_norm))**2)
        
        # Combine all terms with different weights to create a challenging landscape
        return quadratic_term + 0.9 * sin_term + 0.025 * poly_term + interaction_term + \
               chaotic_perturbation + coupled_poly + multi_scale_coupling + high_freq_osc + chebyshev_term