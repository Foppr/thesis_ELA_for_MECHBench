import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Trigonometric component with multiple frequencies and phase shifts
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled) + np.cos(3 * np.pi * x_scaled) + 
                          0.5 * np.sin(4 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Exponential decay component with adaptive weights
        exp_term = np.sum(np.exp(-np.abs(x_scaled)) * (np.sin(5 * x_scaled) + 0.3 * np.cos(7 * x_scaled)))
        
        # Enhanced polynomial term with mixed interaction and higher-order terms
        poly_term = np.sum(x_scaled**6 + 0.4 * x_scaled**4 + 0.6 * x_scaled**3 + 0.2 * x_scaled**2)
        
        # Chaotic component using sine of squared terms with non-linear coupling
        chaotic_term = np.sum(np.sin(x_scaled**2) * np.cos(x_scaled) + 
                             0.3 * np.sin(4 * x_scaled) * np.cos(2 * x_scaled) + 
                             0.1 * np.sin(x_scaled**3))
        
        # Additional interaction term with cross-dimension coupling and non-linearity
        interaction_term = np.sum(np.sin(x_scaled[:-1] - x_scaled[1:]) * 
                                np.cos(x_scaled[:-1] + x_scaled[1:]) * 
                                (x_scaled[:-1]**2 + x_scaled[1:]**2))
        
        # Novel gradient structure with sigmoidal modulation
        grad_term = np.sum(1 / (1 + np.exp(-x_scaled)) * np.sin(3 * x_scaled) * np.cos(x_scaled))
        
        # Combine all terms with optimized weights and add constant offset
        return 0.2 * trig_term + 0.3 * exp_term + 0.2 * poly_term + 0.15 * chaotic_term + 0.1 * interaction_term + 0.05 * grad_term + 1.5