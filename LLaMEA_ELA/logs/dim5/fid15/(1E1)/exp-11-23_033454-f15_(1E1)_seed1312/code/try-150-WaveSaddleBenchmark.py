import numpy as np

class WaveSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Initialize wave parameters with chaotic variation
        np.random.seed(42)
        self.wave_freq = 1.0 + 3.0 * np.random.rand(dim)
        self.wave_amp = 0.5 + 2.0 * np.random.rand(dim)
        # Saddle point configuration
        self.saddle_positions = 3.0 * np.random.rand(dim) - 1.5
        self.saddle_strength = 2.0 + np.random.rand(dim)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Wave component
        wave_term = np.sum(self.wave_amp * np.sin(self.wave_freq * x) * np.exp(-0.1 * x**2))
        
        # Saddle point component with chaotic positioning
        saddle_term = 0.0
        for i in range(self.dim):
            dist = (x[i] - self.saddle_positions[i])**2
            saddle_term += self.saddle_strength[i] * np.exp(-dist / 0.5)
        
        # Add chaotic modulation to the wave frequencies and amplitudes
        chaotic_mod = np.sin(x * 0.7) + 0.5 * np.cos(x * 1.3)
        wave_mod = np.sum(self.wave_amp * (1.0 + 0.3 * chaotic_mod) * 
                         np.sin((self.wave_freq + 0.2 * chaotic_mod) * x))
        
        # Combine terms with different weights
        return 0.7 * wave_term + 0.3 * saddle_term + 0.5 * wave_mod