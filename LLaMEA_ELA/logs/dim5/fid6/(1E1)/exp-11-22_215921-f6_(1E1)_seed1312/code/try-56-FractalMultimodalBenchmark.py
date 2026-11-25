import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        quadratic = np.sum(x_norm ** 2)
        
        # Multi-scale sinusoidal oscillations with varying frequencies and amplitudes
        sinusoidal = 2.0 * np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm) + 
                                 np.sin(30 * x_norm) * np.cos(25 * x_norm))
        
        # Radial basis functions with fractal-like positioning
        rbf = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.1)
                rbf += np.exp(-5 * distance**2) * np.sin(10 * distance)
        
        # Fractal-like structure with recursive scaling
        fractal = 0.0
        for k in range(1, 6):
            scale = 2 ** k
            fractal += (1.0 / scale) * np.sum(np.sin(scale * x_norm) * np.cos(scale * x_norm))
        
        # Cross-term coupling with exponential decay
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x_norm[i] * x_norm[i+1]) * np.exp(-0.5 * (x_norm[i]**2 + x_norm[i+1]**2))
        
        # Modified Gaussian peaks with fractal positioning
        gaussian = 0.0
        for i in range(self.dim):
            pos = np.sin(i * np.pi / self.dim) * np.cos(i * np.pi / (self.dim + 1))
            gaussian += 2.0 * np.exp(-5 * (x_norm[i] - pos)**2)
        
        # Saddle point structure with hyperbolic tangent components
        saddle = 0.0
        for i in range(self.dim):
            saddle += np.tanh(3 * x_norm[i]) * np.sin(5 * x_norm[i])
        
        # Dimension-dependent conditioning factor
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Combine all components
        return condition_factor * (quadratic + sinusoidal + rbf + fractal + cross_term + gaussian + saddle)