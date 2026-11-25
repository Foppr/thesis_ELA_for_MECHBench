import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced exponential decay with variable rates
        exp_term = np.sum(np.exp(-0.5 * x_scaled**2) * np.cos(0.3 * x_scaled))
        
        # Augmented trigonometric modulation with multiple frequencies
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) + 
                          0.5 * np.sin(5 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Refined polynomial distortion with higher-order terms
        poly_term = np.sum(x_scaled**6 - 3 * x_scaled**4 + 2 * x_scaled**2)
        
        # Enhanced chaotic component using nested sine and exponential
        chaotic_term = np.sum(np.sin(np.exp(0.5 * x_scaled)) * np.cos(0.7 * x_scaled))
        
        # Improved logarithmic barrier terms with additional penalty
        barrier_term = np.sum(np.log(1.0 + 0.5 * np.abs(x_scaled)) * np.exp(-0.3 * x_scaled**2) + 
                             0.1 * np.sin(4 * np.pi * x_scaled))
        
        # Additional high-frequency oscillation component with variable amplitude
        high_freq_term = np.sum(0.8 * np.sin(12 * np.pi * x_scaled) * np.cos(9 * np.pi * x_scaled) + 
                               0.3 * np.sin(15 * np.pi * x_scaled))
        
        # Combine all terms with different weights
        return 0.3 * exp_term + 0.25 * trig_term + 0.2 * poly_term + 0.15 * chaotic_term + 0.05 * barrier_term + 0.05 * high_freq_term + 1.5