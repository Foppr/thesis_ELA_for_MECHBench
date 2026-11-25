import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sine-cosine interactions with varying frequencies
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += np.sin(15.0 * x_scaled[i]) * np.cos(12.0 * x_scaled[i]) + \
                          0.5 * np.sin(25.0 * x_scaled[i]) * np.cos(20.0 * x_scaled[i])
        
        # Radial Gaussian decay with multiple peaks
        r = np.sqrt(np.sum(x_scaled**2))
        gaussian_decay = np.exp(-r**2 / 2.0) * (1.0 + 0.5 * np.sin(10.0 * r))
        
        # Cross-dimensional coupling with sine-cosine modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.01)
                cross_coupling += np.sin(8.0 * dist) * np.cos(6.0 * dist) * np.exp(-dist**2 / 2.0)
        
        # Multi-scale harmonic interactions with varying amplitudes
        harmonic_sum = 0.0
        for i in range(self.dim):
            harmonic_sum += (1.0 + 0.3 * np.sin(5.0 * x_scaled[i])) * \
                           (np.sin(18.0 * x_scaled[i]) + 0.7 * np.cos(14.0 * x_scaled[i]))
        
        # Saddle point structure with implicit constraint
        saddle_penalty = 0.0
        for i in range(self.dim):
            saddle_penalty += (x_scaled[i]**2 - 0.25)**2
        
        # Deceptive fitness landscape with dynamic conditioning
        conditioning_factor = 1.0 + 1.5 * np.sin(3.0 * r) * np.cos(2.0 * r)
        
        # Combine all components
        result = (conditioning_factor * 
                 (0.4 * chaotic_sum + 0.3 * gaussian_decay + 0.2 * cross_coupling + 0.1 * harmonic_sum) + 
                 0.5 * saddle_penalty)
        
        return result