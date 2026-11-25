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
                         0.7 * np.sin(7 * np.pi * x_norm[i]) * np.cos(9 * np.pi * x_norm[i]) +
                         0.3 * np.sin(11 * np.pi * x_norm[i]) * np.cos(13 * np.pi * x_norm[i]))
        
        # Modified radial symmetry with stronger logarithmic barrier and fractal components
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = (1.0 / (1.0 + np.exp(-2*r)) - 0.5) + \
                      0.5 * np.sin(15 * r) * np.cos(12 * r) + \
                      0.4 * np.log(1.0 + r**3) + \
                      0.2 * np.sin(25 * r)
        
        # Stronger non-linear cross-dimensional coupling with chaotic interactions
        coupling_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 3) % self.dim
            coupling_term += np.exp(-0.3 * (x_norm[i] - x_norm[j])**2) * \
                            np.sin(6 * x_norm[i] * x_norm[k]) * \
                            np.cos(5 * x_norm[j] * x_norm[k]) * \
                            (1 + 0.3 * np.sin(10 * x_norm[i]))
        
        # Enhanced fractal-like structure with multiple scales and chaotic perturbations
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(20 * x_norm[i]) * np.cos(18 * x_norm[i]) + \
                           0.6 * np.sin(25 * x_norm[i]) * np.cos(23 * x_norm[i]) + \
                           0.4 * np.sin(30 * x_norm[i]) * np.cos(27 * x_norm[i]) + \
                           0.2 * np.sin(35 * x_norm[i]) * np.cos(32 * x_norm[i])
        
        # Asymmetric saddle points with varying curvature and enhanced complexity
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x_norm[i]**4 - 2 * x_norm[i]**2 + 0.3) * \
                          np.sin(8 * x_norm[i]) + \
                          0.9 * np.exp(-0.7 * (x_norm[i] - 1)**2) * \
                          np.cos(7 * x_norm[i]) + \
                          0.5 * np.sin(12 * x_norm[i])
        
        # Additional chaotic modulation and noise component
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += 0.1 * np.sin(50 * x_norm[i]) * np.cos(48 * x_norm[i]) + \
                         0.05 * np.sin(60 * x_norm[i]) * np.cos(58 * x_norm[i])
        
        # Final combined function with adjusted weights for better difficulty
        return 0.25 * wave_term + 0.3 * radial_term + 0.25 * coupling_term + \
               0.15 * fractal_term + 0.05 * saddle_term + 0.05 * chaos_term