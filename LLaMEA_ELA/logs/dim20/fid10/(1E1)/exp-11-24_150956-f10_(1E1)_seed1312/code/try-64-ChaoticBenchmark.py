import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Multi-frequency trigonometric component with nested interactions
        trig_term = np.sum(np.sin(3.2 * np.pi * x_scaled) + 
                          np.cos(4.1 * np.pi * x_scaled) + 
                          np.sin(1.7 * np.pi * x_scaled**2) + 
                          np.cos(2.3 * np.pi * x_scaled**3))
        
        # Multi-modal exponential decay with variable rates
        exp_term = np.sum(np.exp(-0.3 * np.abs(x_scaled)) * 
                         (np.sin(5 * x_scaled) + 0.5 * np.sin(8 * x_scaled)) + 
                         np.exp(-0.7 * np.abs(x_scaled)) * 
                         np.cos(2.1 * x_scaled))
        
        # High-degree polynomial with cross-dimensional interactions
        poly_term = np.sum(0.9 * x_scaled**6 + 0.5 * x_scaled**4 + 0.7 * x_scaled**3 + 
                          0.4 * x_scaled**2 + 0.3 * x_scaled + 
                          0.1 * np.sum(x_scaled[:-1] * x_scaled[1:]))
        
        # Enhanced chaotic component with multiple sine/cosine combinations
        chaotic_term = np.sum(np.sin(x_scaled**2) * np.cos(x_scaled) + 
                             0.2 * np.sin(4.2 * x_scaled) * np.cos(1.8 * x_scaled) + 
                             0.15 * np.sin(2.7 * x_scaled**2) * np.cos(3.1 * x_scaled))
        
        # Complex interaction term between dimensions with varying coupling strengths
        interaction_term = np.sum(np.sin(2.0 * (x_scaled[:-1] - x_scaled[1:])) * 
                                np.cos(0.7 * (x_scaled[:-1] + x_scaled[1:])) + 
                                0.3 * np.sin(1.2 * (x_scaled[:-1]**2 - x_scaled[1:]**2)) * 
                                np.cos(1.5 * (x_scaled[:-1] + x_scaled[1:])))
        
        # Additional cross-dimensional coupling with exponential weighting
        cross_term = np.sum(np.exp(-0.5 * np.abs(x_scaled[:-1] - x_scaled[1:])) * 
                           np.sin(3.0 * (x_scaled[:-1] + x_scaled[1:])))
        
        # Combine all terms with adaptive weights
        return 0.25 * trig_term + 0.25 * exp_term + 0.2 * poly_term + 0.15 * chaotic_term + 0.1 * interaction_term + 0.05 * cross_term + 2.0