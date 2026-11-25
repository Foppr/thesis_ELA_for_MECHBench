import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with chaotic damping
        r_squared = np.sum(x_scaled**2)
        radial_damping = np.exp(-r_squared / 2.0) * (1.0 + 0.3 * np.sin(10.0 * r_squared))
        
        # Chaotic saddle term using logistic map-like dynamics
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Logistic-like map with parameter modulation
            param = 3.8 + 0.2 * np.sin(5.0 * xi)
            chaotic_term += param * xi * (1.0 - xi**2)
        
        # Embedded periodic attractors with varying frequencies
        periodic_terms = []
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            phase = 0.5 * np.pi * i
            periodic_terms.append(np.sin(freq * x_scaled[i] + phase) * np.cos(freq * x_scaled[i] + phase))
        
        # Combine all terms with conditioning and cross-scale interactions
        periodic_sum = np.sum(periodic_terms)
        cross_scale = np.sum(x_scaled[:-1] * np.sin(10.0 * x_scaled[1:]))
        
        # Final function value with chaotic modulation
        result = radial_damping * (0.5 + 0.3 * chaotic_term + 0.4 * periodic_sum + 0.1 * cross_scale)
        
        return result