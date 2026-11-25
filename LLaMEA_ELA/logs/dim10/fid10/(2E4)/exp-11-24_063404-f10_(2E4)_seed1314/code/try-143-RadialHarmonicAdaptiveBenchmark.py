import numpy as np

class RadialHarmonicAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive conditioning parameters
        self.conditioning = 1.0 + 2.0 * np.random.rand(dim)
        # Initialize harmonic frequencies and phases
        self.frequencies = 2.0 + 3.0 * np.random.rand(dim)
        self.phases = 2.0 * np.pi * np.random.rand(dim)
        # Initialize radial basis centers and widths
        self.centers = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.widths = 0.5 + 1.5 * np.random.rand(dim)
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial basis function component
        rb_term = 0.0
        for i in range(self.dim):
            center = self.centers[i]
            width = self.widths[i]
            diff = x_scaled - center
            rb_term += np.exp(-0.5 * np.sum((diff / width)**2))
        
        # Harmonic interaction component with adaptive frequencies
        harmonic_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            freq = self.frequencies[i] * self.conditioning[i]
            harmonic_term += np.sin(freq * xi + self.phases[i]) * \
                           np.cos(freq * xi + self.phases[i])
        
        # Cross-dimensional coupling with adaptive conditioning
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cond_i = self.conditioning[i]
                cond_j = self.conditioning[j]
                cross_term += (np.sin(cond_i * x_scaled[i]) * np.cos(cond_j * x_scaled[j]) + 
                              np.cos(cond_i * x_scaled[i]) * np.sin(cond_j * x_scaled[j]))
        
        # Adaptive conditioning component
        cond_term = 0.0
        for i in range(self.dim):
            cond_term += self.conditioning[i] * (x_scaled[i]**4 - 2*x_scaled[i]**2)
        
        # Sharp transition component
        sharp_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            sharp_term += np.tanh(10 * xi) * np.sin(5 * xi) * np.exp(-0.5 * xi**2)
        
        # Combined objective with weighted components
        return 0.35 * rb_term + 0.25 * harmonic_term + 0.20 * cross_term + \
               0.10 * cond_term + 0.10 * sharp_term