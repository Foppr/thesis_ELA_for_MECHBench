import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Dynamic scaling corridors with chaotic modulation
        corridor_term = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(7.0 * x_scaled[i]) * np.cos(3.0 * x_scaled[i])
            corridor_term += scale_factor * np.exp(-np.abs(x_scaled[i]) * 2.0) * np.sin(5.0 * x_scaled[i])
        
        # Multi-resolution sinusoidal structure with varying frequencies
        sin_term = 0.0
        frequencies = [2.0, 4.0, 8.0, 16.0]
        for i in range(self.dim):
            freq_idx = i % len(frequencies)
            sin_term += np.sin(frequencies[freq_idx] * x_scaled[i]) * np.cos(frequencies[freq_idx] * x_scaled[i])
        
        # Nested chaotic oscillations with adaptive coupling
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_mod = 1.0 + 0.3 * np.sin(10.0 * x_scaled[i]) * np.cos(8.0 * x_scaled[i])
            chaotic_term += chaotic_mod * np.sin(20.0 * x_scaled[i]) * np.exp(-0.5 * x_scaled[i]**2)
        
        # Cross-dimensional coupling with dynamic weights
        coupling_term = 0.0
        for i in range(self.dim):
            weight = 0.5 + 0.5 * np.sin(3.0 * x_scaled[i])
            for j in range(i+1, self.dim):
                coupling_strength = 0.8 + 0.2 * np.cos(5.0 * (x_scaled[i] - x_scaled[j]))
                coupling_term += coupling_strength * weight * np.sin(6.0 * (x_scaled[i] + x_scaled[j]))
        
        # Adaptive gradient modulation with chaotic feedback
        grad_mod = 1.0
        for i in range(self.dim):
            feedback = 0.5 + 0.5 * np.sin(9.0 * x_scaled[i])
            grad_mod *= (1.0 + 0.3 * feedback * np.cos(4.0 * x_scaled[i]))
        
        # Combined result with dynamic weighting
        result = (0.25 * corridor_term + 
                 0.30 * sin_term + 
                 0.25 * chaotic_term + 
                 0.20 * coupling_term) * grad_mod
        
        return result