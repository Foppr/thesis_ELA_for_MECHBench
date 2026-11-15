import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.alpha = 2.0
        self.beta = 1.5
        self.gamma = 0.5
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_decay = np.exp(-self.alpha * r / self.dim)
        
        # Sine wave interference pattern
        sine_sum = 0.0
        for i in range(self.dim):
            sine_sum += np.sin(self.beta * x[i]) * np.cos(self.gamma * x[i])
        
        # Polynomial radial term with adaptive scaling
        poly_radial = 0.0
        for i in range(self.dim):
            poly_radial += (x[i]**4) * (1.0 + 0.1 * np.sin(self.dim * x[i]))
        
        # Adaptive dimensionality scaling factor
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combined multimodal function
        return (0.5 * r**2 * radial_decay + 
                3.0 * sine_sum * dim_factor + 
                0.8 * poly_radial + 
                0.2 * np.sin(10 * r) * np.cos(5 * r))