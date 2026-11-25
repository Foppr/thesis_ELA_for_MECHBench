import numpy as np

class ChaoticSineBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with adaptive scaling
        quad_term = 0.5 * np.sum(x**2)
        
        # Chaotic sine-wave interactions with varying frequencies
        sine_interaction = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * np.pi / (self.dim + 1))
            sine_interaction += np.sin(x[i] * freq) * np.cos(x[i] * freq * 0.5)
        
        # Adaptive basin depths with chaotic perturbations
        basin_term = 0.0
        for i in range(self.dim):
            # Chaotic depth modulation
            depth_mod = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 2))
            # Basin center with chaotic shift
            center_shift = 2.0 * np.cos(i * np.pi / (self.dim + 3))
            basin_term += depth_mod * (x[i] - center_shift)**2 * np.exp(-0.1 * (x[i] - center_shift)**2)
        
        # Saddle-point perturbations with multi-scale coupling
        saddle_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                dist = np.abs(x[i] - x[j])
                coupling_strength = 0.3 * np.sin(dist) * np.cos(dist)
                saddle_term += coupling_strength * (x[i]**2 + x[j]**2)
        
        # Multi-scale chaotic modulation
        chaotic_mod = 0.0
        scales = [0.5, 1.0, 2.0, 3.0]
        for scale in scales:
            chaotic_mod += np.sin(x[0] / scale) * np.cos(x[1] / (scale + 1)) * np.tan(x[2] / (scale + 2))
        
        # Dimensionality-dependent complexity factor
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / 6)
        
        return dim_factor * (0.3 * quad_term + 0.3 * sine_interaction + 
                            0.2 * basin_term + 0.15 * saddle_term + 
                            0.05 * chaotic_mod)