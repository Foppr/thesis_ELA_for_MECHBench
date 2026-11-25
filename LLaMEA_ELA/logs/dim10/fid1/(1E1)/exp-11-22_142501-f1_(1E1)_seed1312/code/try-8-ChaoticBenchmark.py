import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced exponential decay with variable rates
        exp_term = np.sum(np.exp(-0.3 * x_scaled**2) * np.cos(0.4 * x_scaled))
        
        # Augmented trigonometric modulation with multiple frequencies
        trig_term = np.sum(np.sin(2.5 * np.pi * x_scaled) * np.cos(3.5 * np.pi * x_scaled) + 
                          0.6 * np.sin(5.5 * np.pi * x_scaled) * np.cos(7.5 * np.pi * x_scaled))
        
        # Refined polynomial distortion with higher-order terms
        poly_term = np.sum(1.5 * x_scaled**6 - 3.5 * x_scaled**4 + 1.8 * x_scaled**2)
        
        # Enhanced chaotic component using nested sine and exponential
        chaotic_term = np.sum(np.sin(np.exp(0.6 * x_scaled)) * np.cos(0.8 * x_scaled))
        
        # Improved logarithmic barrier terms with additional penalty
        barrier_term = np.sum(np.log(1.0 + 0.6 * np.abs(x_scaled)) * np.exp(-0.4 * x_scaled**2) + 
                             0.15 * np.sin(4.5 * np.pi * x_scaled))
        
        # Additional high-frequency oscillation component with variable amplitude
        high_freq_term = np.sum(0.9 * np.sin(13 * np.pi * x_scaled) * np.cos(9.5 * np.pi * x_scaled) + 
                               0.35 * np.sin(15.5 * np.pi * x_scaled))
        
        # Combine all terms with different weights
        return 0.25 * exp_term + 0.3 * trig_term + 0.18 * poly_term + 0.18 * chaotic_term + 0.06 * barrier_term + 0.07 * high_freq_term + 1.4