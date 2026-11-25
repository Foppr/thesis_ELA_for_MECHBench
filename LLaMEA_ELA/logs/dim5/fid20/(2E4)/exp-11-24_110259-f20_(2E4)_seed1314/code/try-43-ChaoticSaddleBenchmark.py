import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with enhanced chaotic damping and multi-scale oscillations
        r_squared = np.sum(x_scaled**2)
        radial_damping = np.exp(-r_squared / 3.0) * (1.0 + 0.5 * np.sin(15.0 * r_squared) + 0.2 * np.cos(7.0 * r_squared))
        
        # Chaotic saddle term with higher sensitivity to initial conditions
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Enhanced logistic-like map with time-varying parameter and cross-dimensional coupling
            param = 3.9 + 0.3 * np.sin(8.0 * xi) + 0.1 * np.cos(3.0 * x_scaled[(i+1) % self.dim])
            chaotic_term += param * xi * (1.0 - xi**2) * (1.0 + 0.1 * np.sin(12.0 * xi))
        
        # Embedded periodic attractors with frequency modulation and phase coupling
        periodic_terms = []
        for i in range(self.dim):
            freq = 3.0 + 4.0 * np.sin(0.7 * i + 0.5 * r_squared)
            phase = 0.3 * np.pi * i + 0.2 * np.sin(2.0 * r_squared)
            periodic_terms.append(np.sin(freq * x_scaled[i] + phase) * np.cos(freq * x_scaled[i] + phase))
        
        # Cross-scale interactions with enhanced non-linearity
        cross_scale = 0.0
        for i in range(self.dim - 1):
            cross_scale += (x_scaled[i] ** 2) * np.sin(15.0 * x_scaled[i+1]) * np.cos(8.0 * x_scaled[i])
        
        # Additional high-frequency oscillatory component
        high_freq = np.sum(np.sin(20.0 * x_scaled) + np.cos(18.0 * x_scaled))
        
        # Final function value with enhanced chaotic modulation and complex interactions
        result = radial_damping * (0.4 + 0.5 * chaotic_term + 0.3 * np.sum(periodic_terms) + 0.2 * cross_scale + 0.1 * high_freq)
        
        return result