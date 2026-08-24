import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis component with Gaussian-like decay
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-0.5 * r**2) * (1.0 + 0.3 * np.sin(5 * r))
        
        # Trigonometric mixture with varying frequencies and phases
        trig_sum = 0.0
        for i in range(self.dim):
            freq = (i + 1) * 2
            phase = i * np.pi / 4
            trig_sum += np.sin(freq * x_norm[i] + phase) * np.cos(freq * x_norm[i] + phase)
        
        # Asymmetric saddle point terms
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x_norm[i]**2 - 0.5 * x_norm[i])**2
        
        # Cross-term interaction
        cross_term = np.sum(x_norm[:-1] * x_norm[1:]) * np.sin(np.pi * r)
        
        # Combine all components
        return 0.4 * radial + 0.3 * trig_sum + 0.2 * saddle + 0.1 * cross_term + 2.0