import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with chaotic damping and memory effects
        r_squared = np.sum(x_scaled**2)
        radial_damping = np.exp(-r_squared / 2.0) * (1.0 + 0.3 * np.sin(10.0 * r_squared))
        
        # Chaotic saddle term using a modified Henon map with time-dependent parameters
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Time-dependent parameter modulation based on previous coordinates
            if i > 0:
                param = 3.8 + 0.2 * np.sin(5.0 * x_scaled[i-1]) + 0.1 * np.cos(3.0 * r_squared)
            else:
                param = 3.8 + 0.2 * np.sin(5.0 * xi)
            chaotic_term += param * xi * (1.0 - xi**2) + 0.05 * np.sin(15.0 * xi)
        
        # Embedded periodic attractors with quantum-like interference
        periodic_terms = []
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i) + 0.5 * np.cos(0.3 * r_squared)
            phase = 0.5 * np.pi * i + 0.2 * np.sin(2.0 * r_squared)
            # Quantum interference pattern
            interference = np.sin(freq * x_scaled[i] + phase) * np.cos(freq * x_scaled[i] + phase) + \
                          0.3 * np.sin(2.0 * freq * x_scaled[i] + 2.0 * phase)
            periodic_terms.append(interference)
        
        # Cross-scale interactions with memory-dependent coupling
        cross_scale = 0.0
        for i in range(self.dim - 1):
            coupling_strength = 0.5 + 0.3 * np.sin(0.7 * r_squared)
            cross_scale += coupling_strength * x_scaled[i] * np.sin(10.0 * x_scaled[i+1]) * np.cos(5.0 * x_scaled[i])
        
        # Memory-dependent basin structure
        memory_effect = 0.0
        if self.dim > 2:
            for i in range(self.dim - 2):
                memory_effect += (x_scaled[i] * x_scaled[i+1] * x_scaled[i+2]) * np.exp(-0.5 * r_squared)
        
        # Final function value with chaotic modulation and quantum interference
        periodic_sum = np.sum(periodic_terms)
        result = radial_damping * (0.5 + 0.3 * chaotic_term + 0.4 * periodic_sum + 
                                  0.1 * cross_scale + 0.05 * memory_effect)
        
        # Add a global scaling factor that varies with dimensionality
        result *= (1.0 + 0.1 * np.sin(0.2 * self.dim))
        
        return result