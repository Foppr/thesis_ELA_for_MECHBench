import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Quadratic basin term - pulls towards origin
        basin = 0.05 * np.sum(x**2)
        
        # Sinusoidal multimodal terms - create oscillations in all dimensions
        sinusoidal = 0
        for i in range(self.dim):
            sinusoidal += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
        
        # Additional high-frequency oscillations to increase complexity
        high_freq = 0
        for i in range(self.dim):
            high_freq += np.sin(10.0 * x[i]) * np.exp(-0.5 * x[i]**2)
        
        # Combine all terms
        return basin + 2.0 * sinusoidal + 0.5 * high_freq