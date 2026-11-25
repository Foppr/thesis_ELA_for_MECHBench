import numpy as np

class MultimodalBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced spherical harmonic component with higher frequency
        r = np.sqrt(np.sum(x_scaled**2))
        spherical_harmonic = np.sin(5.0 * r) * np.cos(3.0 * r)
        
        # Improved exponential decay barriers with more pronounced minima
        barrier_term = 0.0
        for i in range(self.dim):
            # Create sharper attractive regions
            barrier_term += 2.0 * (np.exp(-3.0 * (x_scaled[i] - 1.0)**2) + 
                                  np.exp(-3.0 * (x_scaled[i] + 1.0)**2) + 
                                  np.exp(-1.5 * x_scaled[i]**2))
        
        # Enhanced cross-dimensional sinusoidal interactions with adaptive frequencies
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 3.0 + 0.8 * np.sin(x_scaled[i] * 0.5)
                cross_term += np.sin(freq * x_scaled[i] + 2.0 * x_scaled[j]) * \
                             np.cos(1.5 * x_scaled[i] - 1.0 * x_scaled[j])
        
        # Enhanced multimodal oscillatory component with more complex structure
        multimodal_term = 0.0
        for i in range(self.dim):
            multimodal_term += (np.sin(7.0 * x_scaled[i]) + 
                               0.7 * np.sin(14.0 * x_scaled[i]) + 
                               0.5 * np.sin(21.0 * x_scaled[i]) +
                               0.3 * np.sin(28.0 * x_scaled[i]))
        
        # Modified radial exponential decay with stronger sinusoidal modulation
        radial_decay = np.exp(-r**2) * (1.0 + 0.6 * np.sin(5.0 * r))
        
        # Additional landscape component for increased complexity
        additional_term = 0.0
        for i in range(self.dim):
            additional_term += np.sin(4.0 * x_scaled[i])**2 + 0.5 * np.cos(8.0 * x_scaled[i])
        
        # Combined landscape with optimized weights
        return 2.0 * spherical_harmonic + 1.2 * barrier_term + 0.8 * cross_term + \
               1.0 * multimodal_term + 1.1 * radial_decay + 0.7 * additional_term + 2.5