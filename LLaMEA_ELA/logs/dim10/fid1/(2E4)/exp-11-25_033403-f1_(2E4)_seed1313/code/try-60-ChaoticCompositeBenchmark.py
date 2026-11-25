import numpy as np

class ChaoticCompositeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.sin_freq = 3.0
        self.poly_degree = 4
        self.barrier_strength = 2.0
        self.mixing_factor = 0.5
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with chaotic frequency modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.3 * np.sin(i * 0.7)
            sin_term += np.sin(freq_mod * self.sin_freq * x[i])**2
        
        # Polynomial conditioning with dimensionality-dependent exponents
        poly_term = 0.0
        for i in range(self.dim):
            exp_factor = 1.0 + (i / self.dim) * (self.poly_degree - 1)
            poly_term += (x[i]**exp_factor)**2
            
        # Exponential barrier terms with adaptive strength
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_term += self.barrier_strength * np.exp(0.5 * np.abs(x[i])) * np.sin(0.3 * x[i])**2
            
        # Cross-dimensional coupling with chaotic mixing
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mix_factor = self.mixing_factor * (1.0 + 0.2 * np.sin(i * j))
                cross_term += mix_factor * np.sin(x[i] + x[j]) * np.cos(0.5 * (x[i] - x[j]))
                
        # Adaptive dimensionality scaling with chaotic modulation
        dim_scaling = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(i * 0.3) * (i / self.dim)
            dim_scaling += scale_factor * x[i]**3
            
        # Chaotic noise component with varying amplitude
        noise_term = 0.0
        for i in range(self.dim):
            noise_amp = 0.1 + 0.05 * np.sin(i * 1.3)
            noise_term += noise_amp * np.cos(5 * x[i])**2
            
        # Non-convex valley structure with exponential modulation
        valley_term = 0.0
        for i in range(self.dim):
            valley_depth = 1.0 + 0.4 * np.sin(2 * x[i])
            valley_width = 1.0 + 0.3 * np.cos(x[i])
            valley_term += valley_depth * (x[i] - np.sin(x[i]))**2 * valley_width
            
        # Final composite function with weighted components
        total = 0.5 * sin_term + 0.3 * poly_term + 0.2 * barrier_term + 0.1 * cross_term + 0.15 * dim_scaling + 0.05 * noise_term + 0.25 * valley_term
        
        return total