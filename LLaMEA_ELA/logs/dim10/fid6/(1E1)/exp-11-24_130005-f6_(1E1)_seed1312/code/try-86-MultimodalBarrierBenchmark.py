import numpy as np

class MultimodalBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced spherical harmonic component with variable frequency
        r = np.sqrt(np.sum(x_scaled**2))
        spherical_harmonic = np.sin(4.0 * r) * np.cos(3.0 * r) + 0.3 * np.sin(7.0 * r)
        
        # Improved exponential decay barriers with asymmetric minima
        barrier_term = 0.0
        for i in range(self.dim):
            # Asymmetric attractive regions
            barrier_term += 1.5 * np.exp(-4.0 * (x_scaled[i] - 0.8)**2) + \
                           1.2 * np.exp(-4.0 * (x_scaled[i] + 0.8)**2) + \
                           0.8 * np.exp(-3.0 * x_scaled[i]**2)
        
        # Novel cross-dimensional interactions with frequency modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.5 + 0.8 * np.cos(x_scaled[i])
                freq_j = 2.0 + 0.6 * np.sin(x_scaled[j])
                cross_term += np.sin(freq_i * x_scaled[i] + freq_j * x_scaled[j]) * \
                             np.cos(0.5 * x_scaled[i] - 0.3 * x_scaled[j]) * \
                             (1.0 + 0.2 * np.sin(x_scaled[i] + x_scaled[j]))
        
        # Enhanced multimodal oscillatory component with varying amplitudes
        multimodal_term = 0.0
        for i in range(self.dim):
            multimodal_term += (np.sin(6.0 * x_scaled[i]) + 
                               0.6 * np.sin(12.0 * x_scaled[i]) + 
                               0.4 * np.sin(18.0 * x_scaled[i]) +
                               0.2 * np.sin(24.0 * x_scaled[i]))
        
        # Modified radial exponential decay with enhanced sinusoidal modulation
        radial_decay = np.exp(-r**2) * (1.0 + 0.5 * np.sin(5.0 * r) + 0.3 * np.cos(8.0 * r))
        
        # Combined landscape with optimized weights for better conditioning
        return 2.0 * spherical_harmonic + 1.0 * barrier_term + 0.7 * cross_term + \
               0.9 * multimodal_term + 1.2 * radial_decay + 2.5