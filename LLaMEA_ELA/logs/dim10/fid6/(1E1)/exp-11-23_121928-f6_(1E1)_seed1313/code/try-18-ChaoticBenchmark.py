import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Exponential term creating steep gradients
        exp_term = np.sum(np.exp(2 * np.abs(x_scaled)) - 1)
        
        # Logarithmic barrier preventing boundary escape
        log_barrier = np.sum(np.log(1 + np.abs(x_scaled)) + 0.1 * np.log(1 + x_scaled**2))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_mod = np.sum(np.sin(5 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) * 
                        (1 + 0.5 * np.sin(7 * np.pi * x_scaled)))
        
        # Hyperbolic tangent shaping for nonlinearity
        tanh_term = np.sum(np.tanh(x_scaled)**2)
        
        # Polynomial interaction with chaotic coefficients
        poly_interaction = np.sum((x_scaled**4 + 0.5 * x_scaled**3 - 0.2 * x_scaled**2 + 
                                 0.1 * x_scaled) * np.sin(2 * np.pi * x_scaled))
        
        # Combine all terms with different weights
        return 0.3 * exp_term + 0.4 * log_barrier - 0.2 * sin_mod + 0.1 * tanh_term + 0.05 * poly_interaction