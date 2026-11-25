import numpy as np

class ExponentialGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.scale_factor = 1.0 + dim * 0.05
        self.gaussian_width = 0.8 + dim * 0.12
        self.harmonic_freq = 2.5 + dim * 0.15
        self.decay_rate = 0.15 + dim * 0.02
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian-shaped basins with varying widths
        gaussian_term = 0.0
        for i in range(self.dim):
            gaussian_term += np.exp(-0.5 * ((x[i] / self.gaussian_width)**2)) * (x[i]**2 + 1.0)
            
        # Multi-scale harmonic modulations
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += np.sin(self.harmonic_freq * x[i]) * np.cos(self.harmonic_freq * x[i])
            
        # Exponential decay interactions between dimensions
        decay_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = abs(x[i] - x[j])
                decay_term += np.exp(-self.decay_rate * distance) * (x[i]**2 + x[j]**2)
                
        # Multi-modal structure with varying depths
        modal_term = 0.0
        for i in range(self.dim):
            modal_term += (x[i]**4 - 10.0 * x[i]**2 + 5.0) * np.exp(-0.15 * x[i]**2)
            
        # Additional periodic component with varying frequency
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(self.harmonic_freq * x[i] + 0.5 * np.cos(2.0 * self.harmonic_freq * x[i]))
            
        # Combine all components with different weights
        return (1.8 * gaussian_term + 
                0.9 * harmonic_term + 
                0.7 * decay_term + 
                1.4 * modal_term + 
                0.5 * periodic_term)