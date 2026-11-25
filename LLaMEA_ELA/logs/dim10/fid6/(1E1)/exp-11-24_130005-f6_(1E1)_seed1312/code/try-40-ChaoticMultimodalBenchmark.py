import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(2.0 * np.pi * x_scaled[i]) * np.cos(3.0 * np.pi * x_scaled[i]) + \
                           0.5 * np.sin(5.0 * np.pi * x_scaled[i]) * np.cos(7.0 * np.pi * x_scaled[i])
        
        # Power-law decay with exponential modulation
        power_term = 0.0
        for i in range(self.dim):
            power_term += (np.abs(x_scaled[i])**1.5) * np.exp(-0.5 * x_scaled[i]**2)
        
        # Cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(4.0 * x_scaled[i] * x_scaled[j]) * \
                             np.cos(2.5 * x_scaled[i]**2 + 1.3 * x_scaled[j]**2) + \
                             0.3 * np.sin(1.7 * x_scaled[i] * x_scaled[j]) * \
                             np.cos(3.2 * x_scaled[i] + 2.8 * x_scaled[j])
        
        # Multimodal sine-cosine combination with varying amplitudes
        multi_term = 0.0
        for i in range(self.dim):
            multi_term += (np.sin(12.0 * x_scaled[i]) * np.cos(8.0 * x_scaled[i]) + 
                          0.7 * np.sin(6.0 * x_scaled[i]) * np.cos(4.0 * x_scaled[i]) + 
                          0.4 * np.sin(3.0 * x_scaled[i]) * np.cos(2.0 * x_scaled[i]))
        
        # Fractional power and logarithmic modulation
        log_term = 0.0
        for i in range(self.dim):
            if np.abs(x_scaled[i]) > 1e-6:
                log_term += (np.log(np.abs(x_scaled[i])) * np.sin(2.0 * np.pi * x_scaled[i]))**2
        
        # Combine all terms with carefully chosen weights
        return 0.8 * chaotic_term + 0.4 * power_term + 0.6 * cross_term + \
               0.7 * multi_term + 0.3 * log_term + 1.5