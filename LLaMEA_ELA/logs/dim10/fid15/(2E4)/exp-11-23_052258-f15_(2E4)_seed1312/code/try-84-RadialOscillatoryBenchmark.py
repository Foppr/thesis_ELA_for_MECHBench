import numpy as np

class RadialOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with oscillatory modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = r * np.sin(3.0 * r) * np.exp(-0.1 * r**2)
        
        # Periodic oscillation in each dimension
        periodic_term = np.sum(np.sin(2.0 * x + 0.5 * np.cos(x)) * 
                              np.cos(1.5 * x - 0.3 * np.sin(x)))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Cross-dimensional interaction with radial influence
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                cross_term += (x[i] * x[j]) / (1.0 + 0.1 * dist**2) * np.sin(0.5 * r)
        
        # Multi-scale harmonic component with varying amplitudes
        harmonic_term = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.3 * np.sin(0.2 * i)
            freq = 2.0 + 0.5 * np.cos(0.1 * i)
            harmonic_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Symmetric multimodal structure with Gaussian peaks
        modal_term = 0.0
        for i in range(self.dim):
            peak_pos = 2.0 * np.sin(0.3 * i)
            modal_term += np.exp(-0.5 * ((x[i] - peak_pos) / 0.5)**2) * np.sin(3.0 * x[i])
        
        # Combined function with scaling and normalization
        total = condition_factor * (radial_term + periodic_term + cross_term + 
                                   harmonic_term + modal_term)
        
        return total