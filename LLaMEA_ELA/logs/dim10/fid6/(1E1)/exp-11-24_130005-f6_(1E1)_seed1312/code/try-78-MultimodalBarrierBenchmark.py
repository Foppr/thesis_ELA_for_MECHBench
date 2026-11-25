import numpy as np

class MultimodalBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Spherical harmonic component with varying degrees
        r = np.sqrt(np.sum(x_scaled**2))
        spherical_harmonic = np.sin(3.0 * r) * np.cos(2.0 * r)
        
        # Exponential decay barriers around multiple global minima
        barrier_term = 0.0
        for i in range(self.dim):
            # Create attractive regions with exponential decay
            barrier_term += np.exp(-4.0 * (x_scaled[i] - 1.0)**2) + \
                           np.exp(-4.0 * (x_scaled[i] + 1.0)**2) + \
                           np.exp(-1.5 * x_scaled[i]**2)
        
        # Cross-dimensional sinusoidal interactions with varying frequencies
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 3.0 + 0.3 * np.sin(x_scaled[i] * x_scaled[j])
                cross_term += np.sin(freq * x_scaled[i] + 1.2 * x_scaled[j]) * \
                             np.cos(1.5 * x_scaled[i] - 0.6 * x_scaled[j])
        
        # Multimodal oscillatory component with multiple local optima
        multimodal_term = 0.0
        for i in range(self.dim):
            multimodal_term += (np.sin(6.0 * x_scaled[i]) + 
                               0.6 * np.sin(12.0 * x_scaled[i]) + 
                               0.4 * np.sin(18.0 * x_scaled[i]))
        
        # Radial exponential decay with sinusoidal modulation
        radial_decay = np.exp(-r**2) * (1.0 + 0.5 * np.sin(3.0 * r))
        
        # Combined landscape with adjusted weights
        return 1.8 * spherical_harmonic + 0.9 * barrier_term + 0.7 * cross_term + \
               0.8 * multimodal_term + 1.1 * radial_decay + 2.5