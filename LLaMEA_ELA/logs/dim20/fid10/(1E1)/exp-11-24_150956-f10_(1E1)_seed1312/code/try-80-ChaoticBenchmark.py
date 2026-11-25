import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced trigonometric component with multiple frequencies and phase shifts
        trig_term = np.sum(np.sin(6.0 * np.pi * x_scaled) + np.cos(7.0 * np.pi * x_scaled) + 
                          np.sin(2.5 * np.pi * x_scaled**2) + np.cos(3.5 * np.pi * x_scaled**2))
        
        # Exponential decay with variable rates and sine modulation
        exp_term = np.sum(np.exp(-1.3 * np.abs(x_scaled)) * np.sin(8.0 * x_scaled) * 
                         np.cos(1.7 * x_scaled) + np.exp(-0.6 * x_scaled**2) * np.sin(4.5 * x_scaled))
        
        # Higher degree polynomial with cross-terms and non-linear interactions
        poly_term = np.sum(1.2 * x_scaled**6 + 0.9 * x_scaled**4 + 1.0 * x_scaled**3 + 
                          0.7 * x_scaled**2 + 0.5 * x_scaled + 0.3 * x_scaled[:-1] * x_scaled[1:])
        
        # Chaotic component with multiple sine/cosine interactions and dynamic frequencies
        chaotic_term = np.sum(np.sin(x_scaled**3) * np.cos(x_scaled**2) + 
                            0.4 * np.sin(6.0 * x_scaled) * np.cos(4.0 * x_scaled) + 
                            0.15 * np.sin(9.0 * x_scaled**2) * np.cos(2.5 * x_scaled))
        
        # Advanced interaction term with higher-order dimension coupling
        interaction_term = np.sum(np.sin(3.5 * (x_scaled[:-1] - x_scaled[1:])) * 
                                np.cos(1.4 * (x_scaled[:-1] + x_scaled[1:])) + 
                                0.6 * np.sin(2.8 * (x_scaled[:-2] - x_scaled[2:])) * 
                                np.cos(0.9 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Novel cross-dimensional coupling with exponential weights
        coupling_term = np.sum(np.exp(-2.2 * np.abs(x_scaled[:-1] - x_scaled[1:])) * 
                             np.sin(4.5 * (x_scaled[:-1] + x_scaled[1:])) + 
                             np.exp(-1.7 * np.abs(x_scaled[:-2] - x_scaled[2:])) * 
                             np.cos(3.5 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Combined weighted sum with additional bias term
        return 0.45 * trig_term + 0.35 * exp_term + 0.18 * poly_term + 0.08 * chaotic_term + \
               0.06 * interaction_term + 0.04 * coupling_term + 2.2