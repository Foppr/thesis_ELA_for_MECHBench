import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Multi-frequency trigonometric component with nested interactions
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled) + 
                          np.cos(3 * np.pi * x_scaled) + 
                          np.sin(5 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Exponential decay with oscillatory modulation
        exp_term = np.sum(np.exp(-np.abs(x_scaled)) * (np.sin(5 * x_scaled) + 0.5 * np.cos(10 * x_scaled)))
        
        # Multilevel polynomial with mixed degrees and cross-terms
        poly_term = np.sum(x_scaled**6 + 0.4 * x_scaled**4 + 0.3 * x_scaled**3 + 
                          0.2 * x_scaled**2 + 0.1 * x_scaled)
        
        # Nested chaotic component with multiple sine-wave interactions
        chaotic_term = np.sum(np.sin(x_scaled**2) * np.cos(x_scaled) + 
                             0.3 * np.sin(4 * x_scaled) * np.cos(2 * x_scaled) + 
                             0.1 * np.sin(x_scaled**3) * np.cos(x_scaled**2))
        
        # Cross-dimensional coupling with higher-order interactions
        interaction_term = np.sum(np.sin(x_scaled[:-1] - x_scaled[1:]) * 
                                np.cos(x_scaled[:-1] + x_scaled[1:]) * 
                                np.sin(0.5 * (x_scaled[:-1]**2 + x_scaled[1:]**2)))
        
        # Additional high-frequency chaotic modulation
        high_freq_term = np.sum(np.sin(15 * x_scaled) * np.cos(13 * x_scaled) * 
                               np.exp(-0.5 * np.abs(x_scaled)))
        
        # Combine all terms with varying weights and add constant offset
        return (0.2 * trig_term + 
                0.25 * exp_term + 
                0.2 * poly_term + 
                0.15 * chaotic_term + 
                0.1 * interaction_term + 
                0.1 * high_freq_term + 
                3.0)