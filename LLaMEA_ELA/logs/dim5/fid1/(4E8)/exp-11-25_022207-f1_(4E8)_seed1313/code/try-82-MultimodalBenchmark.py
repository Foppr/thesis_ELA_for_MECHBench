import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-cosine waves with varying frequencies and amplitudes
        chaotic_term = np.sum(np.sin(3.5 * np.pi * x_norm) * np.cos(4.5 * np.pi * x_norm) * 
                             (1 + 0.25 * np.sin(6.5 * np.pi * x_norm)) * 
                             np.exp(-0.2 * np.abs(x_norm)))
        
        # Asymmetric quartic potentials with different coefficients for positive and negative regions
        quartic_term = np.sum(np.where(x_norm >= 0, 
                                      0.7 * x_norm**4, 
                                      -0.15 * x_norm**4))
        
        # Non-separable high-order polynomial interactions with mixed terms
        poly_interaction = np.sum(x_norm[:-1]**2 * x_norm[1:]**3 + 
                                x_norm[:-1]**3 * x_norm[1:]**2 + 
                                0.12 * x_norm[:-1]**4 * x_norm[1:]**2)
        
        # Central repulsive force field with exponential decay
        center_distance = np.sqrt(np.sum(x_norm**2))
        repulsion_term = 3.0 / (1.0 + center_distance**2.5 + 0.2 * center_distance**5)
        
        # Add noise to increase robustness testing
        noise = 0.025 * np.random.normal(0, 1, self.dim)
        
        # Cross-dimensional coupling with trigonometric interaction
        cross_term = 0.2 * np.sum(np.sin(1.5 * x_norm[:-1] + 1.2 * x_norm[1:]) * 
                                np.cos(0.8 * x_norm[:-1] - 1.3 * x_norm[1:]))
        
        return chaotic_term + quartic_term + poly_interaction - repulsion_term + cross_term + np.sum(noise)