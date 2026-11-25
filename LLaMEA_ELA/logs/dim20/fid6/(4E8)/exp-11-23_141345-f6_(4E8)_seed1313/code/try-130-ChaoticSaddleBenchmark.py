import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic saddle point terms with logistic map modulation
        chaotic_term = np.sum(4.0 * x * (1.0 - x) + 0.1 * np.sin(10.0 * x) * np.cos(5.0 * x))
        
        # Radial symmetry breaking with polynomial distortion
        radial_break = np.sum((x**2 + 0.5 * x**4) * np.exp(-0.1 * np.sum(x**2)))
        
        # Adaptive cross-dimensional coupling with time-varying weights
        coupling_term = 0.0
        for i in range(self.dim - 1):
            coupling_term += (0.5 + 0.3 * np.sin(0.1 * i)) * x[i]**2 * x[i+1] + \
                           (0.4 + 0.2 * np.cos(0.15 * i)) * x[i] * x[i+1]**2
            
        # Sharp directional change through hyperbolic tangent modulation
        sharp_term = np.sum(np.tanh(5.0 * x) * np.exp(-0.3 * x**2) * np.sin(3.0 * x))
        
        # Multi-scale oscillation with amplitude and frequency modulation
        oscillation_term = np.sum(np.sin(8.0 * x + 0.5 * np.sin(12.0 * x)) * 
                                 (1.0 + 0.4 * np.cos(6.0 * x)) * 
                                 np.exp(-0.15 * x**2))
        
        # Non-linear interaction with exponential scaling
        nonlinear_term = np.sum(np.exp(0.5 * x) - 1.0 + 0.3 * np.sin(x) * np.cos(2.0 * x))
        
        # Ruggedness through fractional polynomial terms
        rugged_term = np.sum(0.6 * x**4.5 - 0.4 * x**3.5 + 0.2 * x**2.5)
        
        # Combined function with optimized weights for chaos and multimodality
        return 0.30 * chaotic_term + 0.25 * radial_break + 0.20 * coupling_term + \
               0.12 * sharp_term + 0.10 * oscillation_term + 0.03 * nonlinear_term + 0.00 * rugged_term