import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.9
        self.b = 0.1
        self.c = 0.5
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic logistic map component for non-linearity
        chaotic_component = np.sum(
            (self.a * x_scaled * (1 - x_scaled)) + 
            self.b * np.sin(self.c * x_scaled) + 
            0.05 * np.cos(2 * np.pi * x_scaled)
        )
        
        # Fractional Brownian motion inspired irregularities
        fbm_irregularity = np.sum(
            0.3 * np.sin(10 * x_scaled) * np.exp(-0.5 * x_scaled**2) +
            0.2 * np.cos(8 * x_scaled) * np.exp(-0.3 * x_scaled**2) +
            0.1 * np.sin(15 * x_scaled**2) * np.exp(-0.1 * x_scaled**4)
        )
        
        # High-order polynomial cross-dimensional interactions
        poly_interaction = np.sum(
            (x_scaled[:-1]**4 + x_scaled[1:]**4) * 
            np.sin(2.0 * (x_scaled[:-1] + x_scaled[1:])) +
            (x_scaled[:-2]**5 + x_scaled[2:]**5) * 
            np.cos(1.5 * (x_scaled[:-2] - x_scaled[2:]))
        )
        
        # Time-delayed feedback terms
        delayed_feedback = np.sum(
            0.4 * np.sin(x_scaled[:-1] - 0.3 * x_scaled[1:]) +
            0.3 * np.cos(x_scaled[:-2] + 0.2 * x_scaled[2:])
        )
        
        # Asymmetric saddle point structure
        saddle_structure = np.sum(
            (x_scaled**2 - 1)**3 + 
            0.5 * (x_scaled**3 - x_scaled)**2 +
            0.1 * np.sin(5 * x_scaled)
        )
        
        # Combined landscape with varying weights
        return (
            0.4 * chaotic_component +
            0.25 * fbm_irregularity +
            0.2 * poly_interaction +
            0.1 * delayed_feedback +
            0.05 * saddle_structure +
            2.1
        )