import numpy as np

class MultimodalBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Spherical harmonic component with varying degrees and added chaos
        r = np.sqrt(np.sum(x_scaled**2))
        spherical_harmonic = np.sin(3.0 * r) * np.cos(2.0 * r) * np.exp(-0.5 * r)
        
        # Exponential decay barriers around multiple global minima with chaotic modulation
        barrier_term = 0.0
        for i in range(self.dim):
            # Create attractive regions with exponential decay and chaotic perturbations
            barrier_term += np.exp(-5.0 * (x_scaled[i] - 1.0)**2) + \
                           np.exp(-5.0 * (x_scaled[i] + 1.0)**2) + \
                           np.exp(-2.0 * x_scaled[i]**2) + \
                           0.3 * np.sin(10.0 * x_scaled[i]) * np.cos(7.0 * x_scaled[i])
        
        # Cross-dimensional sinusoidal interactions with chaotic frequency modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 2.0 + 0.5 * np.sin(x_scaled[i]) + 0.2 * np.cos(3.0 * x_scaled[j])
                cross_term += np.sin(freq * x_scaled[i] + 1.5 * x_scaled[j]) * \
                             np.cos(1.2 * x_scaled[i] - 0.8 * x_scaled[j]) + \
                             0.1 * np.sin(5.0 * x_scaled[i] * x_scaled[j])
        
        # Multimodal oscillatory component with multiple local optima and fractal modulation
        multimodal_term = 0.0
        for i in range(self.dim):
            multimodal_term += (np.sin(5.0 * x_scaled[i]) + 
                               0.5 * np.sin(10.0 * x_scaled[i]) + 
                               0.3 * np.sin(15.0 * x_scaled[i]) + 
                               0.2 * np.sin(20.0 * x_scaled[i]))
        
        # Radial exponential decay with sinusoidal modulation and fractal noise
        radial_decay = np.exp(-r**2) * (1.0 + 0.4 * np.sin(4.0 * r)) * (1.0 + 0.1 * np.cos(8.0 * r))
        
        # Chaotic component based on logistic map iterations with enhanced non-linearity
        chaotic_term = 0.0
        for i in range(self.dim):
            x_logistic = 0.5
            for _ in range(20):
                x_logistic = 3.9 * x_logistic * (1 - x_logistic)
            chaotic_term += np.sin(25.0 * x_logistic * x_scaled[i]) * np.cos(20.0 * x_logistic * x_scaled[i]) + \
                           0.1 * np.sin(40.0 * x_logistic * x_scaled[i])
        
        # Additional non-separable component with fractal-like structure
        non_sep = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                non_sep += np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j]) * \
                          (1.0 + 0.2 * np.sin(5.0 * x_scaled[i] * x_scaled[j]))
        
        # Fractal-like structure using fractional Brownian motion approximation with noise
        fbm_term = 0.0
        for i in range(self.dim):
            fbm_term += (np.sin(7.0 * x_scaled[i]) + 
                        0.7 * np.sin(14.0 * x_scaled[i]) + 
                        0.4 * np.sin(21.0 * x_scaled[i]) + 
                        0.2 * np.sin(28.0 * x_scaled[i]) + 
                        0.1 * np.sin(35.0 * x_scaled[i]))
        
        # Introduce additional noise and fractal-like perturbations with chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(13.0 * x_scaled[i]) * np.cos(9.0 * x_scaled[i]) + \
                     0.3 * np.sin(27.0 * x_scaled[i]) * np.cos(18.0 * x_scaled[i]) + \
                     0.2 * np.sin(45.0 * x_scaled[i])
        
        # Enhanced non-separability with higher-order interactions and fractal components
        enhanced_non_sep = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    enhanced_non_sep += np.sin(x_scaled[i] + x_scaled[j] + x_scaled[k]) * \
                                       np.cos(x_scaled[i] - x_scaled[j] + x_scaled[k]) * \
                                       (1.0 + 0.1 * np.sin(3.0 * x_scaled[i] * x_scaled[j] * x_scaled[k]))
        
        # Add even higher-order interaction terms to increase complexity with fractal modulation
        high_order_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    for l in range(k+1, self.dim):
                        high_order_term += np.sin(x_scaled[i] * x_scaled[j] + x_scaled[k] * x_scaled[l]) * \
                                          np.cos(x_scaled[i] * x_scaled[k] - x_scaled[j] * x_scaled[l]) * \
                                          (1.0 + 0.05 * np.sin(7.0 * x_scaled[i] * x_scaled[j] * x_scaled[k] * x_scaled[l]))
        
        # Add ultra-high-order interaction terms with chaotic modulation
        ultra_high_order_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    for l in range(k+1, self.dim):
                        for m in range(l+1, self.dim):
                            ultra_high_order_term += np.sin(x_scaled[i] * x_scaled[j] * x_scaled[k] + 
                                                           x_scaled[l] * x_scaled[m]) * \
                                                   np.cos(x_scaled[i] * x_scaled[l] - x_scaled[j] * x_scaled[m]) * \
                                                   (1.0 + 0.02 * np.sin(11.0 * x_scaled[i] * x_scaled[j] * x_scaled[k] * x_scaled[l] * x_scaled[m]))
        
        # Add a new component with ultra-high dimensional interaction and fractal chaos
        fractal_chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    for l in range(k+1, self.dim):
                        for m in range(l+1, self.dim):
                            fractal_chaos += np.sin(x_scaled[i] * x_scaled[j] * x_scaled[k] * x_scaled[l] * 
                                                   x_scaled[m] * x_scaled[n]) * \
                                           np.cos(2.0 * x_scaled[i] + 3.0 * x_scaled[j] - x_scaled[k] + 
                                                  0.5 * x_scaled[l] * x_scaled[m] * x_scaled[n]) * \
                                           (1.0 + 0.01 * np.sin(17.0 * x_scaled[i] * x_scaled[j] * x_scaled[k] * 
                                                               x_scaled[l] * x_scaled[m] * x_scaled[n]))
        
        # Combine all components with adjusted weights and add a new global scaling factor
        return 2.0 * spherical_harmonic + 1.0 * barrier_term + 0.8 * cross_term + \
               0.9 * multimodal_term + 1.2 * radial_decay + 3.0 + 0.6 * chaotic_term + 0.5 * non_sep + \
               0.7 * fbm_term + 0.4 * noise + 0.3 * enhanced_non_sep + 0.3 * high_order_term + 0.2 * ultra_high_order_term + 0.15 * fractal_chaos