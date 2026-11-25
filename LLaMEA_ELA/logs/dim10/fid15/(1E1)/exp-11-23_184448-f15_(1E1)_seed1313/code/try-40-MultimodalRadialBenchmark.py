import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Radial basis function component with varying widths and centers
        radial_term = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(i * np.pi / (self.dim + 1))
            width = 0.5 + 0.5 * np.cos(i * np.pi / (self.dim + 2))
            radial_term += np.exp(-width * (x[i] - center)**2)
        
        # Sinusoidal oscillation component with varying frequencies and amplitudes
        sine_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 3))
            amp = 1.0 + 0.3 * np.cos(i * np.pi / (self.dim + 4))
            sine_term += amp * np.sin(freq * x[i])
        
        # Cross-dimensional coupling with polynomial interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += (x[i] * x[j])**2 * np.cos(x[i] + x[j])
        
        # Chaotic perturbation using logistic map
        chaotic_term = 0.0
        r = 3.95
        for i in range(self.dim):
            if i == 0:
                x_prev = x[-1]
            else:
                x_prev = x[i-1]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev)) * np.cos(x[i])
        
        # Hybrid scaling based on dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return scale_factor * (radial_term + 0.5 * sine_term + 0.3 * coupling_term + 0.2 * chaotic_term)