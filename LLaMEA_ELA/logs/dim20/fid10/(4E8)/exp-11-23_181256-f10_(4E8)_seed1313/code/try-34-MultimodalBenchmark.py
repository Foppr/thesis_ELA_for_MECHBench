import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_norm = x / 5.0
        
        # Higher-order polynomial terms to increase curvature and complexity
        poly_term = np.sum(0.8 * x_norm**6 + 0.5 * x_norm**5 + 0.3 * x_norm**4 + 0.1 * x_norm**3)
        
        # Exponential terms with multiple decay rates to create diverse valley shapes
        exp_term = np.sum(np.exp(-2.0 * x_norm**2) + np.exp(-0.5 * x_norm**2) - 2.0)
        
        # Nested trigonometric terms with varying frequencies and modulation to increase local optima density
        trig_term = np.sum(np.sin(15 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Complex cross-dimensional interaction using product of sinusoids with phase shifts
        cross_term = np.sum(np.sin(np.pi * x_norm[:-1]) * np.cos(np.pi * x_norm[1:]) * 
                           np.sin(2 * np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # Additional interaction term with non-linear coupling between dimensions
        nonlinear_cross_term = np.sum((x_norm[:-1]**2 + x_norm[1:]**2) * np.exp(-0.5 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Combine all terms with carefully tuned weights to produce a highly complex landscape
        return 0.4 * poly_term + 0.3 * exp_term + 0.2 * trig_term + 0.05 * cross_term + 0.05 * nonlinear_cross_term