import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic map dynamics with time-delayed feedback
        chaotic = 0.0
        r = 3.95  # Chaos-inducing parameter
        for i in range(self.dim):
            if i >= 2:
                # Time-delayed feedback with chaotic logistic map
                chaotic += (r * x[i-2] * (1 - x[i-2]) - 
                           r * x[i-1] * (1 - x[i-1])) ** 2
        
        # Exponential radial basis functions with dynamic centers and widths
        rbfs = 0.0
        for i in range(min(5, self.dim)):
            center = 2.0 * np.sin(i * 0.5)  # Dynamic centers
            width = 0.3 + 0.1 * np.cos(i * 0.7)  # Varying widths
            rbfs += np.exp(-0.5 * ((x[i] - center) / width) ** 2)
        
        # Sinusoidal coupling between dimensions with varying frequencies
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                freq_i = 1.0 + 0.5 * np.sin(i * 0.3)
                freq_j = 1.0 + 0.5 * np.cos(j * 0.4)
                coupling += np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
        
        # Saddle-point dominant term with negative curvature regions
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i] ** 2 - 1.0) ** 2 + 0.1 * np.sin(5.0 * x[i])
        
        # Polynomial terms with mixed convexity and non-separability
        poly = np.sum(x**2) + 0.05 * np.sum(x**3) + 0.01 * np.sum(x**4)
        
        # Dynamic scaling factor based on dimensionality
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * 0.3) + 0.1 * np.cos(self.dim * 0.5)
        
        return scale_factor * (poly + 0.2 * coupling + 0.15 * rbfs + 0.3 * saddle + 0.25 * chaotic)