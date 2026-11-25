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
            barrier = np.log(1.0 + 0.3 * np.abs(x_norm[i]))
            chaotic_factor = 1.0 + 0.5 * np.sin(7 * x_norm[i]) * np.cos(5 * x_norm[i])
            result += chaotic_factor * (x_norm[i]**2) * (1.0 + 0.3 * barrier)
        
        # Enhanced saddle points with spectral harmonic interference
        saddle_term = 0.0
        for i in range(self.dim):
            # Spectral harmonic interference in saddle regions
            harmonic = np.sin(4.0 * x_norm[i]) * np.cos(5.0 * x_norm[i])
            curvature = 1.0 + 0.6 * np.sin(3.0 * x_norm[i]) * np.cos(4.0 * x_norm[i])
            saddle_term += curvature * (x_norm[i]**4) - 2.0 * (x_norm[i]**2) + 0.2 * harmonic
        
        # Modified dimensionality coupling with spectral harmonic interactions
        coupling = 0.0
        for i in range(self.dim):
            dim_weight = 1.0 + 0.5 * np.sin(4 * x_norm[i])
            for j in range(i+1, self.dim):
                # Spectral harmonic interaction between dimensions
                spectral_interaction = np.sin(7 * (x_norm[i] - x_norm[j])) * np.cos(5 * (x_norm[i] + x_norm[j]))
                coupling += dim_weight * np.exp(-0.2 * (x_norm[i] - x_norm[j])**2) * spectral_interaction
        
        # High-frequency oscillatory component with improved fractal-like self-similarity
        oscillatory = 0.0
        for i in range(self.dim):
            # Fractal-like frequency modulation
            freq = 15 + 8 * np.sin(3.0 * x_norm[i]) * np.cos(2.0 * x_norm[i])
            oscillatory += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.4) * np.sin(1.5 * x_norm[i])
        
        # Global scaling with dynamic weighting and logarithmic proximity sensitivity
        proximity = np.sum(x_norm**2)
        global_scale = 1.0 + 0.4 * np.exp(-0.3 * proximity) + 0.2 * np.log(1.0 + 0.1 * proximity)
        
        # Add improved fractal-like self-similarity through multi-scale harmonic terms
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += (np.sin(9 * x_norm[i]) * np.cos(7 * x_norm[i])) * \
                           (np.sin(5 * x_norm[i]) * np.cos(3 * x_norm[i]))
        
        # Add improved chaotic coupling term
        chaotic_coupling = 0.0
        for i in range(self.dim):
            chaotic_coupling += np.sin(8 * x_norm[i]) * np.cos(6 * x_norm[i]) * \
                               (1.0 + 0.3 * np.sin(2 * x_norm[i]))
        
        return global_scale * (result + 0.7 * saddle_term + 0.5 * coupling + 0.4 * oscillatory + 0.2 * fractal_term + 0.3 * chaotic_coupling)