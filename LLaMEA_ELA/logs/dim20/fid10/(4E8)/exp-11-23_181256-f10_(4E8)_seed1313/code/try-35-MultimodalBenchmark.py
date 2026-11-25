import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_norm = x / 5.0
        
        # Polynomial terms with varying degrees to create diverse curvature
        poly_term = np.sum(0.8 * x_norm**6 + 0.5 * x_norm**4 + 0.3 * x_norm**2)
        
        # Enhanced exponential terms with multiple decay rates
        exp_term = np.sum(np.exp(-2.0 * x_norm**2) + 0.5 * np.exp(-0.5 * x_norm**2) - 1.5)
        
        # High-frequency trigonometric terms to increase local minima density
        trig_term = np.sum(np.sin(15 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm) + 
                          0.5 * np.sin(20 * np.pi * x_norm))
        
        # Complex cross-terms with interaction weights that vary by dimension
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x_norm[i] * x_norm[i+1] * 
                          np.sin(3 * np.pi * x_norm[i]) * 
                          np.cos(2 * np.pi * x_norm[i+1]))
        
        # Additional interaction term that creates asymmetric valleys
        asym_term = np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * np.exp(-x_norm[:-1]**2))
        
        # Combine all terms with adjusted weights for increased challenge
        return 0.4 * poly_term + 0.3 * exp_term + 0.25 * trig_term + 0.05 * cross_term + 0.05 * asym_term