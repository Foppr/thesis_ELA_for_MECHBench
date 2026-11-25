import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Higher-order polynomial term with mixed degrees
        poly_term = np.sum(0.7 * x_scaled**6 + 0.5 * x_scaled**5 + 0.3 * x_scaled**4 + 0.1 * x_scaled**3)
        
        # Enhanced trigonometric terms with multiple frequencies and modulations
        trig_term = np.sum(np.sin(7 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled) * np.sin(2 * np.pi * x_scaled))
        
        # Radial basis function component with multiple centers
        rbf_term = np.sum(np.exp(-5.0 * (x_scaled**2 + 0.5 * x_scaled**4)))
        
        # Exponential interaction term with more complex structure
        exp_interaction = np.sum(np.exp(-(x_scaled[:-1]**2 + x_scaled[1:]**2)) * np.cos(3 * np.pi * x_scaled[:-1] * x_scaled[1:]))
        
        # Cross-term with higher-order interactions and sine modulation
        cross_term = np.sum(x_scaled[:-1]**2 * x_scaled[1:]**2 * np.sin(3 * np.pi * x_scaled[:-1]))
        
        # Shifted global minimum to (0.2, -0.1, 0.3, ..., 0.05) for varied difficulty
        shift = np.sum((x_scaled - 0.04)**2 + 0.2 * np.sin(5 * np.pi * x_scaled))
        
        # Additional noise-like term to increase landscape complexity
        noise_term = np.sum(0.1 * np.sin(10 * np.pi * x_scaled) * np.cos(8 * np.pi * x_scaled))
        
        # Combine all terms with carefully adjusted weights
        return 0.9 * poly_term + 0.5 * trig_term + 0.3 * rbf_term + 0.2 * exp_interaction + 0.15 * cross_term + 0.08 * shift + 0.05 * noise_term