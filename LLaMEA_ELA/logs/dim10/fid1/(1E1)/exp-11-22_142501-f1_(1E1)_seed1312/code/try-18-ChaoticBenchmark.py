import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced exponential decay with variable rates and cross-terms
        exp_term = np.sum(np.exp(-0.3 * x_scaled**2) * np.cos(0.4 * x_scaled) * np.sin(0.6 * x_scaled))
        
        # Augmented trigonometric modulation with multiple frequencies and phase shifts
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled + 0.5) * np.cos(3 * np.pi * x_scaled - 0.3) + 
                          0.4 * np.sin(5 * np.pi * x_scaled + 1.2) * np.cos(7 * np.pi * x_scaled + 0.8))
        
        # Refined polynomial distortion with higher-order terms and interaction components
        poly_term = np.sum(x_scaled**6 - 2.5 * x_scaled**4 + 1.8 * x_scaled**2 + 0.3 * x_scaled**3 * x_scaled[::-1])
        
        # Enhanced chaotic component using nested sine and exponential with coupling
        chaotic_term = np.sum(np.sin(np.exp(0.6 * x_scaled)) * np.cos(0.8 * x_scaled) + 
                             0.2 * np.sin(np.exp(-0.4 * x_scaled**2)) * np.cos(1.1 * x_scaled))
        
        # Improved logarithmic barrier terms with additional penalty and adaptive scaling
        barrier_term = np.sum(np.log(1.0 + 0.4 * np.abs(x_scaled)) * np.exp(-0.2 * x_scaled**2) + 
                             0.15 * np.sin(3 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Additional high-frequency oscillation component with variable amplitude and coupling
        high_freq_term = np.sum(0.7 * np.sin(15 * np.pi * x_scaled) * np.cos(11 * np.pi * x_scaled) + 
                               0.25 * np.sin(18 * np.pi * x_scaled) * np.cos(14 * np.pi * x_scaled))
        
        # Cross-dimensional interaction terms for increased conditioning
        cross_term = np.sum((x_scaled[:-1] - x_scaled[1:])**2 * np.exp(-0.1 * (x_scaled[:-1] + x_scaled[1:])**2))
        
        # Combine all terms with different weights
        return 0.25 * exp_term + 0.2 * trig_term + 0.25 * poly_term + 0.15 * chaotic_term + 0.05 * barrier_term + 0.05 * high_freq_term + 0.05 * cross_term + 1.3