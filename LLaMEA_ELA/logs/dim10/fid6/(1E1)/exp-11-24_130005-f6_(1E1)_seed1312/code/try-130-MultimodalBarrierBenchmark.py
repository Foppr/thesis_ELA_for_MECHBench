import numpy as np

class MultimodalBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced spherical harmonic component with variable degree and phase
        r = np.sqrt(np.sum(x_scaled**2))
        spherical_harmonic = np.sin(4.0 * r) * np.cos(3.0 * r) + 0.5 * np.sin(7.0 * r)
        
        # Exponential decay barriers with adaptive widths and multiple global minima
        barrier_term = 0.0
        for i in range(self.dim):
            # Create attractive regions with varying exponential decay rates
            barrier_term += np.exp(-3.0 * (x_scaled[i] - 1.5)**2) + \
                           np.exp(-4.0 * (x_scaled[i] + 1.5)**2) + \
                           np.exp(-1.5 * x_scaled[i]**2) + \
                           np.exp(-2.5 * (x_scaled[i] - 0.5)**2)
        
        # Cross-dimensional sinusoidal interactions with frequency modulation and coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 3.0 + 0.7 * np.sin(x_scaled[i])
                freq_j = 2.5 + 0.6 * np.cos(x_scaled[j])
                cross_term += np.sin(freq_i * x_scaled[i] + freq_j * x_scaled[j]) * \
                             np.cos(1.8 * x_scaled[i] - 1.2 * x_scaled[j]) * \
                             np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Multimodal oscillatory component with increased complexity and higher harmonics
        multimodal_term = 0.0
        for i in range(self.dim):
            multimodal_term += (np.sin(6.0 * x_scaled[i]) + 
                               0.6 * np.sin(12.0 * x_scaled[i]) + 
                               0.4 * np.sin(18.0 * x_scaled[i]) +
                               0.2 * np.sin(24.0 * x_scaled[i]))
        
        # Radial exponential decay with enhanced sinusoidal modulation and adaptive amplitude
        radial_decay = np.exp(-r**2) * (1.0 + 0.6 * np.sin(5.0 * r) + 0.3 * np.cos(3.0 * r))
        
        # Chaotic component based on logistic map iterations with increased sensitivity and coupling
        chaotic_term = 0.0
        for i in range(self.dim):
            x_logistic = 0.4
            for _ in range(20):
                x_logistic = 3.9 * x_logistic * (1 - x_logistic)
            chaotic_term += np.sin(25.0 * x_logistic * x_scaled[i]) * np.cos(20.0 * x_logistic * x_scaled[i]) + \
                           0.5 * np.sin(30.0 * x_logistic * x_scaled[i])
        
        # Additional non-separable component with enhanced coupling and fractal-like structure
        non_sep = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                non_sep += np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j]) * \
                          (1.0 + 0.2 * np.sin(5.0 * x_scaled[i])) * \
                          (1.0 + 0.3 * np.cos(4.0 * x_scaled[j]))
        
        # Fractal-like structure using fractional Brownian motion approximation with additional harmonics
        fbm_term = 0.0
        for i in range(self.dim):
            fbm_term += (np.sin(8.0 * x_scaled[i]) + 
                        0.8 * np.sin(16.0 * x_scaled[i]) + 
                        0.5 * np.sin(24.0 * x_scaled[i]) + 
                        0.3 * np.sin(32.0 * x_scaled[i]) +
                        0.1 * np.sin(40.0 * x_scaled[i]))
        
        # Additional noise and fractal-like perturbations with increased complexity
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(15.0 * x_scaled[i]) * np.cos(10.0 * x_scaled[i]) + \
                     0.4 * np.sin(30.0 * x_scaled[i]) * np.cos(20.0 * x_scaled[i]) + \
                     0.2 * np.sin(45.0 * x_scaled[i]) * np.cos(30.0 * x_scaled[i])
        
        # Enhanced non-separability with higher-order interactions and adaptive coupling
        enhanced_non_sep = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    enhanced_non_sep += np.sin(x_scaled[i] + x_scaled[j] + x_scaled[k]) * \
                                       np.cos(x_scaled[i] - x_scaled[j] + x_scaled[k]) * \
                                       (1.0 + 0.3 * np.sin(3.0 * x_scaled[i])) * \
                                       (1.0 + 0.2 * np.cos(2.0 * x_scaled[j]))
        
        # Add a new component for increased multimodality and complexity
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += (np.sin(3.0 * x_scaled[i]) + np.cos(2.0 * x_scaled[j])) * \
                               (np.cos(4.0 * x_scaled[i]) + np.sin(5.0 * x_scaled[j]))
        
        # Combine all components with adjusted weights and add a new global scaling factor
        return 1.8 * spherical_harmonic + 1.0 * barrier_term + 0.7 * cross_term + \
               0.9 * multimodal_term + 1.1 * radial_decay + 2.5 + 0.5 * chaotic_term + 0.4 * non_sep + \
               0.6 * fbm_term + 0.3 * noise + 0.15 * enhanced_non_sep + 0.25 * coupling_term