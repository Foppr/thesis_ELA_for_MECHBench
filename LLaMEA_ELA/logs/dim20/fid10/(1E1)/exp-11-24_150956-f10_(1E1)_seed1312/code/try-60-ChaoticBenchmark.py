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
        
        # High-degree polynomial with mixed interaction terms
        poly_term = np.sum(x_scaled**7 + 0.4 * x_scaled**5 + 0.6 * x_scaled**3 + 0.8 * x_scaled**2 + 0.3 * x_scaled)
        
        # Enhanced chaotic component with nested sine-wave interactions
        chaotic_term = np.sum(np.sin(x_scaled**2) * np.cos(x_scaled) + 
                             0.3 * np.sin(4 * x_scaled) * np.cos(2 * x_scaled) + 
                             0.1 * np.sin(x_scaled**3) * np.cos(x_scaled**2))
        
        # Cross-dimensional coupling with complex interaction patterns
        interaction_term = np.sum(np.sin(x_scaled[:-1] - x_scaled[1:]) * 
                                np.cos(x_scaled[:-1] + x_scaled[1:]) * 
                                np.exp(-0.5 * (x_scaled[:-1]**2 + x_scaled[1:]**2)))
        
        # Additional high-frequency oscillation component
        high_freq_term = np.sum(np.sin(15 * x_scaled) * np.cos(12 * x_scaled) + 
                               0.7 * np.sin(20 * x_scaled) * np.cos(18 * x_scaled))
        
        # Combined function with adaptive weighting
        return (0.3 * trig_term + 
                0.25 * exp_term + 
                0.2 * poly_term + 
                0.15 * chaotic_term + 
                0.05 * interaction_term + 
                0.05 * high_freq_term + 
                1.5)