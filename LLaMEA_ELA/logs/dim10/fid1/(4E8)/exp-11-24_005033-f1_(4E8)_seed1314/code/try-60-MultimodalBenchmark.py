import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic spiral structure with multiple frequency components
        spiral_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            spiral_term += (xi**2 + 1e-8) * np.sin(15 * np.pi * xi) * np.cos(7 * np.pi * xi) * \
                          np.sin(3 * np.pi * xi**2) * np.cos(2 * np.pi * xi**3)
        
        # Enhanced dynamic conditioning with exponential scaling
        condition_term = 0.0
        for i in range(self.dim):
            condition_term += (i + 1)**2 * np.exp(0.5 * x[i]**2) * x[i]**4
        
        # Adaptive noise with chaotic modulation
        noise_term = 0.0
        for i in range(self.dim):
            noise_term += np.sin(25 * x[i]) * np.cos(20 * x[i]) * np.sin(10 * x[i]**2) * \
                         (1.0 / (1.0 + np.exp(-x[i]**3)))
        
        # Complex cross-dimensional coupling with multiple interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2)) * \
                              np.exp(-0.1 * (x[i]**2 + x[j]**2)) * \
                              np.sin(0.3 * (x[i] + x[j])**2) * \
                              np.cos(0.7 * (x[i] - x[j])**3)
        
        # Additional quartic and quintic coupling terms for enhanced multimodality
        quartic_term = 0.0
        for i in range(self.dim):
            quartic_term += x[i]**4 * np.sin(5 * x[i])
        
        quintic_term = 0.0
        for i in range(self.dim):
            quintic_term += x[i]**5 * np.cos(3 * x[i])
        
        # Combined result with modified scaling factors
        result = 1.5 * spiral_term + 0.8 * condition_term + 1.2 * noise_term + \
                 0.7 * cross_term + 0.3 * quartic_term + 0.4 * quintic_term
        
        # Global minimum at origin with enhanced penalty for distance from origin
        result += 0.2 * np.sum(x**6) + 0.1 * np.sum(np.abs(x)**3) + 0.05 * np.sum(x**8)
        
        return result