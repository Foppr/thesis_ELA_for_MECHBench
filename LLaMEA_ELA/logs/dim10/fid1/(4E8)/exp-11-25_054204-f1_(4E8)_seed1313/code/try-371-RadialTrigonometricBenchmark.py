import numpy as np

class RadialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers and widths
        self.centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        # Trigonometric frequencies
        self.freqs = np.arange(1, dim + 1)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component
        rbf = 0.0
        for i in range(10):
            diff = x - self.centers[i]
            rbf += self.widths[i] * np.exp(-0.5 * np.sum(diff**2))
        
        # Trigonometric coupling component
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_coupling += np.sin(self.freqs[i] * x[i]) * np.cos(self.freqs[j] * x[j])
        
        # Adaptive conditioning based on dimensionality
        cond_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Cross-dimensional polynomial interactions
        poly_interaction = 0.0
        for i in range(self.dim):
            poly_interaction += (x[i]**2 + x[(i+1) % self.dim]**2) * np.sin(x[i] * x[(i+1) % self.dim])
        
        # Multi-scale harmonic modulation
        harmonic_mod = 0.0
        for i in range(self.dim):
            harmonic_mod += np.sin(3.0 * self.freqs[i] * x[i]) + np.cos(2.0 * self.freqs[i] * x[i])
        
        # Local optima density variation
        density = 0.0
        for i in range(self.dim):
            density += np.sin(0.5 * x[i])**2 + np.cos(0.3 * x[i])**2
        
        # Combined function with adaptive weights
        return cond_factor * (0.6 * rbf + 0.4 * trig_coupling + 
                             0.3 * poly_interaction + 0.2 * harmonic_mod + 
                             0.1 * density)