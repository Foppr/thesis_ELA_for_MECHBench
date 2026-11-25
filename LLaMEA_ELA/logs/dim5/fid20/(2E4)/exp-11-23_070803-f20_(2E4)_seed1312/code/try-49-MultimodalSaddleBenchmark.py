import numpy as np

class MultimodalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Chaotic sinusoidal oscillation component with fractional frequencies
        sin_term = 0
        for i in range(self.dim):
            freq1 = 7.5 + 2.5 * np.sin(i)
            freq2 = 9.2 + 1.8 * np.cos(i)
            sin_term += (np.sin(freq1 * x_norm[i]) * np.cos(freq2 * x_norm[i]) + 
                        np.sin(freq2 * x_norm[i]**2.5) * np.cos(freq1 * x_norm[i]**2.5)) * \
                       (1 + 0.3 * np.sin(3 * i))
        
        # Multiple radial basis functions with chaotic centers and varying widths
        rbf_term = 0
        for i in range(min(7, self.dim)):
            center = np.sin(i * 1.234) * 0.9 + np.cos(i * 0.567) * 0.1
            width = 0.15 + 0.25 * np.sin(i * 0.891)
            diff = x_norm[i] - center
            rbf_term += np.exp(-0.5 * (diff**2) / width**2) * \
                       (1 + 0.4 * np.sin(7 * diff) + 0.3 * np.cos(5 * diff))
        
        # Asymmetric saddle point component with chaotic polynomial terms
        saddle_term = 0
        for i in range(self.dim):
            poly_term = x_norm[i]**6 - 3 * x_norm[i]**4 + 2 * x_norm[i]**2
            exp_term = np.exp(-0.3 * np.abs(x_norm[i])) * np.sin(5 * x_norm[i])
            asym_factor = 1.0 + 0.5 * np.sin(i * 0.789)
            saddle_term += (poly_term * asym_factor + exp_term) * \
                          (1 + 0.2 * np.cos(4 * i))
        
        # Cross-dimensional coupling with chaotic interaction patterns
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.8 + 0.4 * np.sin(i * 0.678 + j * 0.345)
                interaction = np.sin(5 * x_norm[i] + 3 * x_norm[j]) * \
                             np.cos(4 * x_norm[i] - 2 * x_norm[j])
                cross_term += coupling_strength * interaction
        
        # Add a chaotic noise component
        chaos_noise = 0
        for i in range(self.dim):
            chaos_noise += np.sin(13 * x_norm[i]) * np.cos(11 * x_norm[i]) * \
                          (0.05 + 0.02 * np.sin(i))
        
        # Combine all components with chaotic weights
        result = 2.0 * sin_term + 2.5 * rbf_term + 2.2 * saddle_term + 1.2 * cross_term + 0.3 * chaos_noise
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise