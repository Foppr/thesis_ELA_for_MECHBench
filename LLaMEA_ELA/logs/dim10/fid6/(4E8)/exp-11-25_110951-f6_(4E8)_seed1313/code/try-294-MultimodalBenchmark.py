import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base chaotic quadratic potential with adaptive scaling and logarithmic barriers
        result = 0.0
        for i in range(self.dim):
            # Enhanced chaotic modulation with logarithmic barrier
            barrier = np.log(1.0 + 0.5 * np.abs(x_norm[i]))
            chaotic_factor = 1.0 + 0.6 * np.sin(9 * x_norm[i]) * np.cos(7 * x_norm[i])
            result += chaotic_factor * (x_norm[i]**2) * (1.0 + 0.5 * barrier)
        
        # Enhanced saddle points with spectral harmonic interference
        saddle_term = 0.0
        for i in range(self.dim):
            # Spectral harmonic interference in saddle regions
            harmonic = np.sin(5.0 * x_norm[i]) * np.cos(6.0 * x_norm[i])
            curvature = 1.0 + 0.8 * np.sin(4.0 * x_norm[i]) * np.cos(5.0 * x_norm[i])
            saddle_term += curvature * (x_norm[i]**4) - 2.0 * (x_norm[i]**2) + 0.3 * harmonic
        
        # Modified dimensionality coupling with spectral harmonic interactions
        coupling = 0.0
        for i in range(self.dim):
            dim_weight = 1.0 + 0.6 * np.sin(5 * x_norm[i])
            for j in range(i+1, self.dim):
                # Spectral harmonic interaction between dimensions
                spectral_interaction = np.sin(9 * (x_norm[i] - x_norm[j])) * np.cos(7 * (x_norm[i] + x_norm[j]))
                coupling += dim_weight * np.exp(-0.3 * (x_norm[i] - x_norm[j])**2) * spectral_interaction
        
        # High-frequency oscillatory component with fractal-like self-similarity
        oscillatory = 0.0
        for i in range(self.dim):
            # Fractal-like frequency modulation
            freq = 20 + 10 * np.sin(4.0 * x_norm[i]) * np.cos(3.0 * x_norm[i])
            oscillatory += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.5) * np.sin(2 * x_norm[i])
        
        # Global scaling with dynamic weighting and logarithmic proximity sensitivity
        proximity = np.sum(x_norm**2)
        global_scale = 1.0 + 0.5 * np.exp(-0.4 * proximity) + 0.3 * np.log(1.0 + 0.2 * proximity)
        
        # Add fractal-like self-similarity through multi-scale harmonic terms
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += (np.sin(11 * x_norm[i]) * np.cos(9 * x_norm[i])) * \
                           (np.sin(7 * x_norm[i]) * np.cos(5 * x_norm[i]))
        
        return global_scale * (result + 0.8 * saddle_term + 0.6 * coupling + 0.5 * oscillatory + 0.3 * fractal_term)