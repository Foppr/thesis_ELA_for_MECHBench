import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced periodic trigonometric wave components with higher frequencies
        wave_term = 0.0
        for i in range(self.dim):
            wave_term += (np.sin(3 * np.pi * x_norm[i]) * np.cos(4 * np.pi * x_norm[i]) + 
                         0.6 * np.sin(7 * np.pi * x_norm[i]) * np.cos(9 * np.pi * x_norm[i]) +
                         0.3 * np.sin(11 * np.pi * x_norm[i]) * np.cos(13 * np.pi * x_norm[i]))
        
        # Modified radial symmetry with logarithmic barrier and fractal-like perturbations
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = 1.0 / (1.0 + np.exp(-2*r)) - 0.5 + \
                      0.4 * np.sin(15 * r) * np.cos(12 * r) + \
                      0.3 * np.log(1.0 + r**3) + \
                      0.1 * np.sin(25 * r)
        
        # Non-linear cross-dimensional coupling with chaotic interactions
        coupling_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 3) % self.dim
            coupling_term += np.exp(-0.3 * (x_norm[i] - x_norm[j])**2) * \
                            np.sin(5 * x_norm[i] * x_norm[k]) * \
                            np.cos(4 * x_norm[j] * x_norm[k]) + \
                            0.5 * np.sin(8 * x_norm[i]) * np.cos(6 * x_norm[j])
        
        # Multi-scale fractal-like structure with increased complexity
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += (np.sin(15 * x_norm[i]) * np.cos(13 * x_norm[i]) + 
                           0.8 * np.sin(22 * x_norm[i]) * np.cos(19 * x_norm[i]) + 
                           0.5 * np.sin(30 * x_norm[i]) * np.cos(27 * x_norm[i]) +
                           0.2 * np.sin(35 * x_norm[i]) * np.cos(32 * x_norm[i]))
        
        # Asymmetric saddle points with varying curvature and chaotic perturbations
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x_norm[i]**4 - 2 * x_norm[i]**2 + 0.7) * \
                          np.sin(8 * x_norm[i]) + \
                          0.9 * np.exp(-0.4 * (x_norm[i] - 1)**2) * \
                          np.cos(7 * x_norm[i]) + \
                          0.3 * np.sin(15 * x_norm[i]) * np.cos(10 * x_norm[i])
        
        # Additional chaotic modulation and spectral complexity
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += 0.2 * np.sin(20 * x_norm[i] + 0.5 * np.sin(30 * x_norm[i])) + \
                         0.1 * np.cos(25 * x_norm[i] + 0.3 * np.cos(35 * x_norm[i]))
        
        # Final combined function with weighted contributions
        return 0.25 * wave_term + 0.2 * radial_term + 0.25 * coupling_term + \
               0.15 * fractal_term + 0.1 * saddle_term + 0.05 * chaos_term