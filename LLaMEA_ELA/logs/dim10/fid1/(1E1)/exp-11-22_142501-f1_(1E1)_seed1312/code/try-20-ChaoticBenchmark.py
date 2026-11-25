import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Compound exponential decay with adaptive rates
        exp_term = np.sum(np.exp(-0.3 * x_scaled**2) * np.cos(0.4 * x_scaled) * np.sin(0.6 * x_scaled))
        
        # Multi-frequency trigonometric modulation with coupling
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) + 
                          0.7 * np.sin(5 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled) + 
                          0.3 * np.sin(9 * np.pi * x_scaled) * np.cos(11 * np.pi * x_scaled))
        
        # Higher-order polynomial distortion with cross-dimensional interaction
        poly_term = np.sum(x_scaled**8 - 4 * x_scaled**6 + 3 * x_scaled**4 - x_scaled**2)
        
        # Chaotic nested sine-exponential with dynamic phase modulation
        chaotic_term = np.sum(np.sin(np.exp(0.7 * x_scaled) + np.cos(0.5 * x_scaled)) * 
                             np.cos(0.9 * x_scaled) * np.sin(0.4 * x_scaled))
        
        # Logarithmic barrier with adaptive penalty and noise injection
        noise = np.random.normal(0, 0.01, self.dim)
        barrier_term = np.sum((np.log(1.0 + 0.6 * np.abs(x_scaled)) * 
                              np.exp(-0.4 * x_scaled**2) + 
                              0.15 * np.sin(5 * np.pi * x_scaled)) * (1 + noise))
        
        # High-frequency oscillation with amplitude modulation and coupling
        high_freq_term = np.sum(0.9 * np.sin(15 * np.pi * x_scaled) * np.cos(13 * np.pi * x_scaled) + 
                               0.4 * np.sin(18 * np.pi * x_scaled) * np.cos(16 * np.pi * x_scaled) + 
                               0.2 * np.sin(20 * np.pi * x_scaled))
        
        # Cross-dimensional coupling term with interaction weights
        coupling_term = np.sum(np.sin(x_scaled[:-1] + x_scaled[1:]) * np.cos(x_scaled[:-1] - x_scaled[1:]))
        
        # Combine all terms with different weights and add global offset
        return (0.25 * exp_term + 0.3 * trig_term + 0.25 * poly_term + 
                0.1 * chaotic_term + 0.05 * barrier_term + 0.03 * high_freq_term + 
                0.02 * coupling_term + 2.0)