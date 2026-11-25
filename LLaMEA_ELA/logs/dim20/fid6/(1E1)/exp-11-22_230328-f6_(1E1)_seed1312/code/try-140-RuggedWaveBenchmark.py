import numpy as np

class RuggedWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize dimension-specific parameters for wave interactions
        self.wave_frequencies = np.random.uniform(1.0, 4.0, dim)
        self.basin_depths = np.random.uniform(1.0, 3.0, dim)
        self.interaction_strengths = np.random.uniform(0.5, 2.0, dim)
        # Add periodic modulation for adaptive difficulty
        self.modulation_periods = np.random.uniform(2.0, 6.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base rugged wave term with varying frequencies and depths
        wave_term = 0.0
        for i in range(self.dim):
            wave_component = (np.sin(self.wave_frequencies[i] * x_norm[i]) * 
                             np.cos(self.wave_frequencies[i] * x_norm[i]))
            depth_factor = self.basin_depths[i] * (1.0 + 0.3 * np.sin(x_norm[i] * self.modulation_periods[i]))
            wave_term += depth_factor * wave_component
        
        # Multi-dimensional interaction with adaptive coupling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling based on basin depths and interaction strengths
                coupling_strength = (self.interaction_strengths[i] * self.interaction_strengths[j] * 
                                   np.exp(-0.2 * (x_norm[i] - x_norm[j])**2))
                interaction_term += coupling_strength * np.sin(3 * (x_norm[i] + x_norm[j]))
        
        # Periodic basin modulation across dimensions
        modulation_term = 0.0
        for i in range(self.dim):
            modulation_term += np.cos(self.modulation_periods[i] * x_norm[i]) * \
                              np.exp(-0.1 * np.abs(x_norm[i]))
        
        # Combined fitness with dynamic scaling
        combined = wave_term + interaction_term + modulation_term
        
        # Add dimensionality-dependent noise and bias
        noise_factor = 0.05 * np.random.uniform(-1, 1)
        bias_factor = 0.2 * self.dim * np.sum(np.sin(x_norm) * np.cos(x_norm))
        
        return combined + noise_factor + bias_factor