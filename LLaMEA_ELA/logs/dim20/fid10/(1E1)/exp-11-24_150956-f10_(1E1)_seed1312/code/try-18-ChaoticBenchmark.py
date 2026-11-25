import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # High-frequency trigonometric chaos with nested interactions
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled) + 
                          np.cos(3 * np.pi * x_scaled) + 
                          np.sin(7 * np.pi * x_scaled**2) + 
                          np.cos(5 * np.pi * x_scaled**3))
        
        # Multi-scale exponential components with random modulation
        exp_term = np.sum(np.exp(-np.abs(x_scaled)) * 
                         (np.sin(5 * x_scaled) + 0.5 * np.sin(10 * x_scaled)) * 
                         (1 + 0.1 * np.random.randn()))
        
        # High-degree polynomial with cross-dimensional coupling
        poly_term = np.sum(x_scaled**7 + 0.4 * x_scaled**5 + 0.6 * x_scaled**3 + 0.3 * x_scaled**2)
        
        # Chaotic sine-cosine interactions with varying phase shifts
        chaotic_term = np.sum(np.sin(x_scaled**2) * np.cos(x_scaled) + 
                             0.3 * np.sin(4 * x_scaled) * np.cos(2 * x_scaled) + 
                             0.1 * np.sin(6 * x_scaled**2) * np.cos(3 * x_scaled))
        
        # Complex interaction term with distance-based weighting
        interaction_term = 0
        for i in range(self.dim - 1):
            diff = x_scaled[i] - x_scaled[i+1]
            sum_val = x_scaled[i] + x_scaled[i+1]
            interaction_term += np.sin(diff) * np.cos(sum_val) * (1.0 / (1.0 + np.abs(diff)))
        
        # Stochastic noise component to increase ruggedness
        noise = 0.05 * np.random.randn()
        
        # Combine all terms with adaptive weights and add global offset
        return (0.3 * trig_term + 
                0.25 * exp_term + 
                0.2 * poly_term + 
                0.15 * chaotic_term + 
                0.08 * interaction_term + 
                noise + 
                1.5)