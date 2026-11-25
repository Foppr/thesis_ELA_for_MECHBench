import numpy as np

class WaveInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial wave interference component with periodic modulation
        radial_wave = 0.0
        r = np.sqrt(np.sum(x_scaled**2))
        if r > 0:
            # Multiple radial wave components with different frequencies and amplitudes
            for i in range(1, min(6, self.dim + 1)):
                freq = 2.0 * i + 0.5 * np.sin(i * 0.7)
                amp = 1.5 + 0.5 * np.cos(i * 0.3)
                phase = i * 0.8 + 0.3 * np.sin(i * 0.5)
                radial_wave += amp * np.sin(freq * r + phase) / (1.0 + 0.1 * r**2)
        
        # Periodic grid interference pattern
        grid_pattern = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Cross-term interference with periodic modulation
                freq_i = 3.0 + 1.2 * np.sin(i * 0.6)
                freq_j = 2.5 + 0.8 * np.cos(j * 0.4)
                grid_pattern += np.sin(freq_i * x_scaled[i]) * np.cos(freq_j * x_scaled[j]) * \
                               np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Radial penalty with exponential decay and multiple local minima
        penalty = 0.0
        for i in range(self.dim):
            # Multiple penalty centers with varying strengths
            center1 = 0.5 * np.sin(i * 0.9)
            center2 = 0.3 * np.cos(i * 0.7)
            strength1 = 2.0 + 0.8 * np.sin(i * 0.5)
            strength2 = 1.5 + 0.6 * np.cos(i * 0.4)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            penalty += strength1 * np.exp(-dist1 * 2.0) + strength2 * np.exp(-dist2 * 3.0)
        
        # Exponential valley structure with multiple competing terms
        valley = 0.0
        for i in range(self.dim):
            # Create exponential valleys with different steepness
            steepness = 1.5 + 0.5 * np.sin(i * 0.8)
            valley += np.exp(-steepness * np.abs(x_scaled[i]))
        
        # Add complex interaction terms with chaotic phase shifts
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                # Chaotic phase modulation and exponential weighting
                phase_shift = np.sin(i * 0.3 + j * 0.4) * np.cos(i * 0.2 + j * 0.5)
                weight = 1.0 / (1.0 + np.abs(x_scaled[i] - x_scaled[j])**2)
                interaction += weight * np.sin(x_scaled[i] + x_scaled[j] + phase_shift) * \
                              np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Combined function with carefully balanced components
        return 1.5 * radial_wave + 2.0 * grid_pattern + 1.2 * penalty + 0.8 * valley + 1.0 * interaction