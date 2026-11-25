import numpy as np

class OscillatoryCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Polynomial base with global scaling
        poly_term = np.sum(x**4) + 0.5 * np.sum(x**2)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            amp = 1.0 + 0.3 * np.cos(i * np.pi / (self.dim + 2))
            sin_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Correlation-based interactions with exponential decay
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x[i] - x[j])
                weight = np.exp(-dist / (self.dim + 1))
                corr_term += weight * (x[i]**2 + x[j]**2)
        
        # Multi-scale harmonic components
        harmonic_term = 0.0
        scales = [0.5, 1.0, 2.0, 3.0]
        for scale in scales:
            harmonic_term += np.sin(scale * np.sum(x)) * np.cos(scale * np.sum(x**2))
        
        # Exponentially decaying local minima
        local_term = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(i * np.pi / (self.dim + 1))
            depth = 1.0 + 0.5 * np.cos(i * np.pi / (self.dim + 3))
            local_term += depth * np.exp(-0.5 * (x[i] - center)**2) * (x[i]**4 - 2*x[i]**2)
        
        # Dimensionality scaling factor
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return dim_factor * (0.3 * poly_term + 0.25 * sin_term + 
                            0.2 * corr_term + 0.15 * harmonic_term + 
                            0.1 * local_term)