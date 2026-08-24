import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.freq_base = 2.0 * np.pi
        self.amplitude = 3.0
        self.decay_rate = 0.5
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial polynomial component with multiple terms
        r = np.sqrt(np.sum(x**2))
        radial_poly = 0.1 * r**6 + 0.3 * r**4 + 0.5 * r**2
        
        # Sinusoidal waves with varying frequencies and amplitudes
        wave_sum = 0
        for i in range(self.dim):
            wave_sum += np.sin(self.freq_base * x[i] * (1 + 0.1 * i)) * np.cos(self.freq_base * x[i] * 0.5 * (1 + 0.05 * i))
        
        # Exponential decay modulation based on distance from origin
        decay_mod = np.exp(-self.decay_rate * r)
        
        # Chaotic interaction terms between dimensions
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        
        # Additional multimodal component with multiple peaks
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(5 * x[i]) * np.cos(3 * x[i]) + 0.5 * np.sin(7 * x[i])**2
        
        # Combine all components with appropriate scaling
        result = (0.8 * radial_poly + 
                  1.5 * wave_sum + 
                  0.6 * chaotic_interaction + 
                  0.9 * multimodal) * decay_mod
        
        return result