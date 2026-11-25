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
        
        for i in range(self.dim):
            # Create wave patterns with varying frequencies and amplitudes
            freq = 2.0 + 1.5 * np.sin(i * 0.5)
            amp = 1.0 + 0.5 * np.cos(i * 0.3)
            phase = i * 0.2 + 0.1 * np.sin(x_scaled[i] * 3.0)
            radial_wave += amp * np.sin(freq * x_scaled[i] + phase) * np.exp(-0.5 * r**2)
        
        # Periodic interference pattern with exponential decay
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create interference terms between dimensions
                dist = np.abs(x_scaled[i] - x_scaled[j])
                freq = 3.0 + 2.0 * np.sin(i * 0.4 + j * 0.3)
                interference += np.sin(freq * dist) * np.exp(-0.1 * (i + j))
        
        # Radial symmetry with exponential penalty for large distances
        symmetry = 0.0
        for i in range(self.dim):
            # Add radial symmetry with varying strengths
            strength = 1.5 + 0.5 * np.sin(i * 0.7)
            symmetry += strength * np.cos(x_scaled[i] * 2.0) * np.exp(-0.3 * x_scaled[i]**2)
        
        # Sharp ridge and valley structure with exponential penalties
        ridge_valley = 0.0
        for i in range(self.dim):
            # Create sharp transitions using hyperbolic tangent
            ridge_valley += np.tanh(5.0 * x_scaled[i])**2 + np.tanh(3.0 * x_scaled[i])**4
        
        # Exponential penalty term for distance from origin with periodic modulation
        penalty = 0.0
        for i in range(self.dim):
            # Add exponential penalties that increase rapidly away from center
            penalty += np.exp(2.0 * np.abs(x_scaled[i])) * (1.0 + 0.3 * np.sin(i * 0.5))
        
        # Combine all components with carefully balanced weights
        return 1.5 * radial_wave + 1.2 * interference + 0.8 * symmetry + 1.0 * ridge_valley + 0.6 * penalty