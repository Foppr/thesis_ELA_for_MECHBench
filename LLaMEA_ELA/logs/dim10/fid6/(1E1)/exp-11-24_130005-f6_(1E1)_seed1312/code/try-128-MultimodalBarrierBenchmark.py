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
            for _ in range(15):
                x_logistic = 3.8 * x_logistic * (1 - x_logistic)
            chaotic_term += np.sin(20.0 * x_logistic * x_scaled[i]) * np.cos(15.0 * x_logistic * x_scaled[i])
        
        # Additional non-separable component for increased complexity
        non_sep = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                non_sep += np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j])
        
        # Enhanced fractal-like structure using modified fractional Brownian motion approximation
        fbm_term = 0.0
        for i in range(self.dim):
            fbm_term += (np.sin(7.0 * x_scaled[i]) + 
                        0.7 * np.sin(14.0 * x_scaled[i]) + 
                        0.4 * np.sin(21.0 * x_scaled[i]) + 
                        0.2 * np.sin(28.0 * x_scaled[i]))
        
        # Introduce additional noise and fractal-like perturbations
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(13.0 * x_scaled[i]) * np.cos(9.0 * x_scaled[i]) + \
                     0.3 * np.sin(27.0 * x_scaled[i]) * np.cos(18.0 * x_scaled[i])
        
        # Enhanced non-separability with higher-order interactions
        enhanced_non_sep = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    enhanced_non_sep += np.sin(x_scaled[i] + x_scaled[j] + x_scaled[k]) * \
                                       np.cos(x_scaled[i] - x_scaled[j] + x_scaled[k])
        
        # New component: Improved chaotic modulation with dynamic scaling
        dynamic_chaotic = 0.0
        for i in range(self.dim):
            x_dyn = 0.5
            for _ in range(20):
                x_dyn = 3.9 * x_dyn * (1 - x_dyn)
            dynamic_chaotic += np.sin(25.0 * x_dyn * x_scaled[i]) * np.cos(20.0 * x_dyn * x_scaled[i])
        
        # New component: Enhanced radial modulation with multiple frequencies
        radial_mod = 0.0
        for i in range(self.dim):
            radial_mod += (np.sin(6.0 * x_scaled[i]) + 
                          0.8 * np.sin(12.0 * x_scaled[i]) + 
                          0.5 * np.sin(18.0 * x_scaled[i]))
        
        # Combine all components with adjusted weights and add a new global scaling factor
        return 1.5 * spherical_harmonic + 0.8 * barrier_term + 0.6 * cross_term + \
               0.7 * multimodal_term + 0.9 * radial_decay + 2.3 + 0.4 * chaotic_term + 0.3 * non_sep + \
               0.5 * fbm_term + 0.2 * noise + 0.1 * enhanced_non_sep + 0.6 * dynamic_chaotic + 0.4 * radial_mod