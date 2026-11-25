import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Periodic trigonometric wave components with varying frequencies and amplitudes
        wave_term = 0.0
        for i in range(self.dim):
            wave_term += np.sin(2 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i]) + \
                         0.5 * np.sin(5 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i])
        
        # Radial symmetry with logarithmic barrier near boundaries
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = 1.0 / (1.0 + np.exp(-r)) - 0.5 + \
                      0.3 * np.sin(10 * r) * np.cos(8 * r) + \
                      0.2 * np.log(1.0 + r**2)
        
        # Non-linear cross-dimensional coupling with exponential interactions
        coupling_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            coupling_term += np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * \
                            np.sin(4 * x_norm[i] * x_norm[k]) * \
                            np.cos(3 * x_norm[j] * x_norm[k])
        
        # Multi-scale fractal-like structure with chaotic perturbations
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(12 * x_norm[i]) * np.cos(9 * x_norm[i]) + \
                           0.7 * np.sin(18 * x_norm[i]) * np.cos(15 * x_norm[i]) + \
                           0.3 * np.sin(24 * x_norm[i]) * np.cos(21 * x_norm[i])
        
        # Asymmetric saddle points with varying curvature
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x_norm[i]**4 - 2 * x_norm[i]**2 + 0.5) * \
                          np.sin(6 * x_norm[i]) + \
                          0.8 * np.exp(-0.5 * (x_norm[i] - 1)**2) * \
                          np.cos(5 * x_norm[i])
        
        # Final combined function with weighted contributions
        return 0.3 * wave_term + 0.25 * radial_term + 0.2 * coupling_term + \
               0.15 * fractal_term + 0.1 * saddle_term