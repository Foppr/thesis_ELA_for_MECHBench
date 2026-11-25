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
            barrier_term += np.exp(-5.0 * (x_scaled[i] - 1.0)**2) + \
                           np.exp(-5.0 * (x_scaled[i] + 1.0)**2) + \
                           np.exp(-2.0 * x_scaled[i]**2)
        
        # Cross-dimensional sinusoidal interactions with varying frequencies
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 2.0 + 0.5 * np.sin(x_scaled[i])
                cross_term += np.sin(freq * x_scaled[i] + 1.5 * x_scaled[j]) * \
                             np.cos(1.2 * x_scaled[i] - 0.8 * x_scaled[j])
        
        # Multimodal oscillatory component with multiple local optima
        multimodal_term = 0.0
        for i in range(self.dim):
            multimodal_term += (np.sin(5.0 * x_scaled[i]) + 
                               0.5 * np.sin(10.0 * x_scaled[i]) + 
                               0.3 * np.sin(15.0 * x_scaled[i]))
        
        # Radial exponential decay with sinusoidal modulation
        radial_decay = np.exp(-r**2) * (1.0 + 0.4 * np.sin(4.0 * r))
        
        # Chaotic component based on logistic map iterations for extreme multimodality
        chaotic_term = 0.0
        for i in range(self.dim):
            x_logistic = 0.5
            for _ in range(20):  # Increased iterations for more chaos
                x_logistic = 3.9 * x_logistic * (1 - x_logistic)  # Higher chaos parameter
            chaotic_term += np.sin(25.0 * x_logistic * x_scaled[i]) * np.cos(20.0 * x_logistic * x_scaled[i])
        
        # Additional non-separable component for increased complexity
        non_sep = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                non_sep += np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j])
        
        # Enhanced fractal-like structure using fractional Brownian motion approximation
        fbm_term = 0.0
        for i in range(self.dim):
            fbm_term += (np.sin(8.0 * x_scaled[i]) + 
                        0.8 * np.sin(16.0 * x_scaled[i]) + 
                        0.5 * np.sin(24.0 * x_scaled[i]) + 
                        0.3 * np.sin(32.0 * x_scaled[i]) + 
                        0.1 * np.sin(40.0 * x_scaled[i]))  # More frequencies for complexity
        
        # Add a new twist: incorporate a hybrid chaotic component with tent map
        tent_term = 0.0
        for i in range(self.dim):
            x_tent = 0.3
            for _ in range(18):
                if x_tent < 0.5:
                    x_tent = 2.0 * x_tent
                else:
                    x_tent = 2.0 * (1.0 - x_tent)
            tent_term += np.sin(18.0 * x_tent * x_scaled[i]) * np.cos(12.0 * x_tent * x_scaled[i])
        
        # Combined landscape with adjusted weights
        return 1.8 * spherical_harmonic + 1.0 * barrier_term + 0.7 * cross_term + \
               0.8 * multimodal_term + 1.1 * radial_decay + 2.5 + 0.5 * chaotic_term + 0.4 * non_sep + 0.6 * fbm_term + 0.3 * tent_term