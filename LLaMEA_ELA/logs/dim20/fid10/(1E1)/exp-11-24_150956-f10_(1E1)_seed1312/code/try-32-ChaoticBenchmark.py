import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Multi-frequency trigonometric component with chaotic modulation
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled) + 
                          np.cos(3 * np.pi * x_scaled) + 
                          0.5 * np.sin(7 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Exponential decay with sinusoidal modulation
        exp_term = np.sum(np.exp(-np.abs(x_scaled)) * 
                         (np.sin(5 * x_scaled) + 0.3 * np.sin(10 * x_scaled)))
        
        # High-degree polynomial with mixed interaction terms
        poly_term = np.sum(x_scaled**7 + 0.4 * x_scaled**5 + 0.6 * x_scaled**3 + 0.8 * x_scaled**2)
        
        # Nested chaotic component with multiple sine-wave interactions
        chaotic_term = np.sum(np.sin(x_scaled**2) * 
                             (np.cos(x_scaled) + 0.3 * np.sin(3 * x_scaled)) + 
                             0.15 * np.sin(4 * x_scaled) * np.cos(2 * x_scaled) * np.sin(x_scaled**3))
        
        # Cross-dimensional interaction with exponential coupling
        interaction_term = np.sum(np.exp(-np.abs(x_scaled[:-1] - x_scaled[1:])) * 
                                np.sin(x_scaled[:-1] + x_scaled[1:]) * 
                                np.cos(x_scaled[:-1] * x_scaled[1:]))
        
        # Additional high-frequency oscillation component
        high_freq_term = np.sum(0.2 * np.sin(15 * x_scaled) * np.cos(8 * x_scaled) + 
                               0.1 * np.sin(20 * x_scaled**2))
        
        # Combine all terms with varying weights and add constant offset
        return (0.3 * trig_term + 
                0.25 * exp_term + 
                0.2 * poly_term + 
                0.15 * chaotic_term + 
                0.05 * interaction_term + 
                0.05 * high_freq_term + 
                3.0)