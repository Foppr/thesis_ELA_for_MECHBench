import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sinusoidal components with dynamic frequencies
        chaotic_terms = np.sum(np.sin(20.0 * np.sin(5.0 * x_scaled)) * 
                              np.cos(15.0 * np.cos(3.0 * x_scaled)) + 
                              0.7 * np.sin(25.0 * np.tan(2.0 * x_scaled)) * 
                              np.cos(18.0 * np.tan(4.0 * x_scaled)))
        
        # Saddle-point attractor terms with hyperbolic tangents
        saddle_terms = np.sum(np.tanh(3.0 * x_scaled) * np.tanh(2.0 * x_scaled**2) + 
                            0.5 * np.tanh(4.0 * x_scaled**3) * np.tanh(3.0 * x_scaled**4))
        
        # Dynamic gradient modulation with time-varying weights
        grad_mod = np.sum((1.0 + 0.3 * np.sin(10.0 * x_scaled)) * 
                         (x_scaled**2 + 0.5 * x_scaled**4) * 
                         np.exp(-0.5 * x_scaled**2))
        
        # Cross-dimensional coupling with chaotic interaction coefficients
        cross_coupling = np.sum(np.sin(8.0 * (x_scaled[:-1] + x_scaled[1:])) * 
                              np.cos(6.0 * (x_scaled[:-1] - x_scaled[1:])) * 
                              np.exp(-0.3 * (x_scaled[:-1]**2 + x_scaled[1:]**2)))
        
        # Multi-scale chaotic interference with asymmetric peaks
        multi_scale = np.sum(np.sin(12.0 * x_scaled**2) * np.cos(9.0 * x_scaled**3) + 
                           0.6 * np.sin(15.0 * x_scaled**4) * np.cos(13.0 * x_scaled**5) + 
                           0.3 * np.sin(20.0 * x_scaled**6) * np.cos(18.0 * x_scaled**7))
        
        # Asymmetric landscape with weighted sum and global shift
        return 0.4 * chaotic_terms + 0.25 * saddle_terms + 0.2 * grad_mod + 0.1 * cross_coupling + 0.05 * multi_scale + 2.1