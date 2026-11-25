import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic map parameters
        self.a = 3.9
        self.b = 0.5
        self.c = 0.3
        
    def f(self, x):
        # Scale input to [-1, 1]
        x_scaled = x / 5.0
        
        # Chaotic logistic map component
        chaotic_term = 0.0
        for i in range(min(3, self.dim)):
            xi = x_scaled[i] if i < len(x_scaled) else 0.0
            chaotic_term += np.sin(self.a * xi * (1 - xi)) * np.cos(self.b * xi)
        
        # Fractal-like interaction using multiple sine waves with different frequencies
        fractal_term = 0.0
        for i in range(self.dim):
            freqs = [2**(j+1) for j in range(4)]
            for f in freqs:
                fractal_term += np.sin(f * x_scaled[i]) * np.cos(f * x_scaled[i] * 0.5)
        
        # Multi-scale radial basis with chaotic centers
        radial_term = 0.0
        for i in range(min(4, self.dim)):
            center = (np.sin(i * self.a) + np.cos(i * self.b)) / 2.0
            width = 0.1 + 0.05 * np.sin(i * self.c)
            radial_term += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Non-smooth landscape with absolute value and step functions
        smoothness_term = 0.0
        for i in range(self.dim):
            smoothness_term += np.abs(x_scaled[i])**1.7 + np.abs(x_scaled[i])**0.8
        
        # Cross-dimensional coupling with fractal scaling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += (np.sin(x_scaled[i] * x_scaled[j]) + 
                                np.cos(x_scaled[i] + x_scaled[j])) * \
                               np.log(1 + np.abs(i - j))
        
        # Asymmetric saddle with multiple peaks
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x_scaled[i]**4 - 2*x_scaled[i]**2 + 0.5) * \
                          np.sin(3 * x_scaled[i]) * np.cos(2 * x_scaled[i])
        
        # High-frequency noise component
        noise_term = 0.0
        for i in range(self.dim):
            noise_term += np.sin(100 * x_scaled[i]) * np.random.uniform(-0.1, 0.1)
        
        return chaotic_term + fractal_term + radial_term + smoothness_term + \
               coupling_term + saddle_term + noise_term