import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic base term
        quadratic = np.sum(x_scaled**2)
        
        # Exponentially decaying harmonic terms with varying frequencies
        harmonics = 0.0
        for i in range(1, self.dim + 1):
            freq = i * 2 * np.pi
            decay = np.exp(-0.1 * i)
            harmonics += decay * np.sin(freq * x_scaled[i-1])**2
        
        # Adaptive conditioning: increase difficulty with dimensionality
        conditioning = 0.5 * (self.dim - 1) * np.sum(x_scaled**4)
        
        # Combine all components
        return quadratic + 10 * harmonics + conditioning