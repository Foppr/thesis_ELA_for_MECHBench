import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial warping term that distorts the search space
        warped_x = x_norm * (1 + 0.3 * np.sin(3 * x_norm))
        
        # Sum of squares with polynomial distortion
        f1 = np.sum(warped_x**2)
        
        # Logarithmic barrier terms near boundaries to create ruggedness
        barriers = np.sum(np.log(1 + 10 * (5.0 - np.abs(x))**2))
        
        # Gaussian peaks scattered across the domain
        peaks = 0.0
        for i in range(1, 6):
            peak_x = np.random.uniform(-5, 5, self.dim)
            sigma = 0.5 + i * 0.1
            peak_height = 1.0 / (i * 2.0)
            gaussian_term = peak_height * np.exp(-np.sum(((x - peak_x) / sigma)**2))
            peaks += gaussian_term
        
        # Trigonometric mixing term for additional complexity
        trig_term = np.sum(np.sin(5 * x_norm) * np.cos(7 * x_norm))
        
        return f1 + barriers + peaks + 0.5 * trig_term