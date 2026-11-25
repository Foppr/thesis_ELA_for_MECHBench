import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic base term
        quadratic = np.sum(x_scaled**2)
        
        # Exponentially decaying harmonic terms with varying frequencies and amplitudes
        harmonics = 0.0
        for i in range(1, self.dim + 1):
            freq = i * 2 * np.pi
            decay = np.exp(-0.05 * i)
            amplitude = 1.0 + 0.5 * np.sin(i)
            harmonics += decay * amplitude * np.sin(freq * x_scaled[i-1])**3
        
        # Adaptive conditioning with cubic and quartic terms
        conditioning = 0.3 * (self.dim - 1) * np.sum(x_scaled**4)
        
        # Cross-dimensional interaction terms for increased complexity
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.1 * x_scaled[i] * x_scaled[j] * np.sin(3 * np.pi * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Add a global sinusoidal modulation to increase landscape complexity
        modulation = np.sin(2 * np.pi * np.sum(x_scaled**2)) * 0.5
        
        # Combine all components
        return quadratic + 15 * harmonics + conditioning + cross_terms + modulation