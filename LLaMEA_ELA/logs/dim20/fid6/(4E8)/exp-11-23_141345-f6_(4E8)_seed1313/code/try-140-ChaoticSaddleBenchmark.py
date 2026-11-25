import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic saddle point terms with modified logistic map
        chaotic_term = np.sum(3.5 * x * (1.0 - x**2) + 0.15 * np.sin(12.0 * x) * np.cos(6.0 * x))
        
        # Radial symmetry breaking with cubic distortion and adaptive scaling
        radial_break = np.sum((x**3 + 0.4 * x**5) * np.exp(-0.12 * np.sum(x**2)))
        
        # Adaptive cross-dimensional coupling with dynamic weights based on position
        coupling_term = 0.0
        for i in range(self.dim - 1):
            weight1 = 0.6 + 0.2 * np.sin(0.15 * i + x[i] * x[i+1])
            weight2 = 0.5 + 0.3 * np.cos(0.2 * i - x[i] * x[i+1])
            coupling_term += weight1 * x[i]**2 * x[i+1] + weight2 * x[i] * x[i+1]**2
            
        # Sharp directional change with piecewise hyperbolic modulation
        sharp_term = np.sum(np.tanh(6.0 * x) * np.exp(-0.25 * x**2) * np.sin(4.0 * x))
        
        # Multi-scale oscillation with frequency and amplitude modulation
        oscillation_term = np.sum(np.sin(10.0 * x + 0.6 * np.sin(15.0 * x)) * 
                                 (1.2 + 0.3 * np.cos(7.0 * x)) * 
                                 np.exp(-0.2 * x**2))
        
        # Non-linear interaction with polynomial and exponential components
        nonlinear_term = np.sum(np.exp(0.6 * x) - 1.0 + 0.4 * np.sin(x) * np.cos(3.0 * x))
        
        # Ruggedness through mixed polynomial terms with varying exponents
        rugged_term = np.sum(0.7 * x**4.2 - 0.5 * x**3.8 + 0.3 * x**2.8)
        
        # Combined function with optimized weights for improved challenge and fitness
        return 0.28 * chaotic_term + 0.27 * radial_break + 0.22 * coupling_term + \
               0.13 * sharp_term + 0.09 * oscillation_term + 0.04 * nonlinear_term + 0.07 * rugged_term