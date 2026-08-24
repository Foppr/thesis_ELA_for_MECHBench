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
        sine_interference = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sine_interference += np.sin(self.beta * x[i]) * np.cos(self.gamma * x[j])
        
        # Polynomial radial terms with adaptive scaling
        poly_radial = 0
        for i in range(self.dim):
            poly_radial += (x[i]**4 + x[i]**3 + x[i]**2) * (1.0 + 0.1 * i / self.dim)
        
        # Adaptive dimensionality-dependent scaling
        dim_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Exponential interaction terms
        exp_interaction = 0
        for i in range(self.dim):
            exp_interaction += np.exp(-0.5 * (x[i] - 1.0)**2) * np.sin(2 * np.pi * x[i])
        
        # Combine all components
        return (dim_factor * radial_decay * 
                (sine_interference + 0.5 * poly_radial + 0.3 * exp_interaction))