import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-cosine waves with varying frequencies and amplitudes
        chaotic_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * 
                             (1 + 0.3 * np.sin(7 * np.pi * x_norm)) * 
                             np.exp(-0.15 * np.abs(x_norm)))
        
        # Asymmetric quartic potentials with different coefficients for positive and negative regions
        quartic_term = np.sum(np.where(x_norm >= 0, 
                                      0.6 * x_norm**4, 
                                      -0.2 * x_norm**4))
        
        # Non-separable high-order polynomial interactions with mixed terms
        poly_interaction = np.sum(x_norm[:-1]**2 * x_norm[1:]**3 + 
                                x_norm[:-1]**3 * x_norm[1:]**2 + 
                                0.1 * x_norm[:-1]**4 * x_norm[1:]**2)
        
        # Central repulsive force field with exponential decay
        center_distance = np.sqrt(np.sum(x_norm**2))
        repulsion_term = 2.5 / (1.0 + center_distance**3 + 0.15 * center_distance**6)
        
        # Add noise to increase robustness testing
        noise = 0.03 * np.random.normal(0, 1, self.dim)
        
        # Cross-dimensional coupling with trigonometric interaction
        cross_term = 0.15 * np.sum(np.sin(2 * x_norm[:-1] + x_norm[1:]) * 
                                np.cos(x_norm[:-1] - 2 * x_norm[1:]))
        
        # Enhanced gradient complexity through modified interactions
        enhanced_term = 0.2 * np.sum(np.sin(4 * x_norm) * np.cos(3 * x_norm) * 
                                   (1 + 0.2 * np.sin(6 * x_norm)) * 
                                   np.exp(-0.2 * np.abs(x_norm)))
        
        # Additional non-separable coupling with higher-order terms
        high_order_coupling = 0.1 * np.sum(x_norm[:-2]**3 * x_norm[1:-1]**2 * x_norm[2:]**3 + 
                                          x_norm[:-2]**2 * x_norm[1:-1]**3 * x_norm[2:]**2)
        
        # Perturbed repulsive force field with additional non-linearity
        perturbed_repulsion = 3.0 / (1.0 + center_distance**4 + 0.2 * center_distance**8)
        
        return chaotic_term + quartic_term + poly_interaction - perturbed_repulsion + cross_term + enhanced_term + high_order_coupling + np.sum(noise)