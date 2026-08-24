import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.scale_factor = 10.0
        self.decay_rate = 0.5
        self.modulation_freq = 2.0 * np.pi
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component based on radial distance
        r = np.sqrt(np.sum(x**2))
        exp_decay = np.exp(-self.decay_rate * r)
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_modulation = 0
        for i in range(self.dim):
            freq = (i + 1) * self.modulation_freq
            sin_modulation += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional polynomial interactions with varying degrees
        poly_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i]**3 * x[j]**2 + x[i]**2 * x[j]**3) * np.cos(0.5 * (x[i] + x[j]))
        
        # Gaussian-like peaks with random positioning and varying heights
        gaussian_peaks = 0
        peak_positions = np.random.rand(self.dim) * 10 - 5  # Random positions in [-5, 5]
        for i in range(self.dim):
            gaussian_peaks += np.exp(-0.5 * ((x[i] - peak_positions[i]) / 1.5)**2) * (1.0 + 0.5 * np.sin(3 * x[i]))
        
        # Additional chaotic component using a modified sine map
        chaotic_component = 0
        for i in range(self.dim):
            chaotic_component += np.sin(10 * np.sin(x[i])) * np.cos(5 * np.sin(x[i]))
        
        # Combine all components with appropriate scaling
        return (self.scale_factor * exp_decay + 
                2.0 * sin_modulation + 
                0.8 * poly_interaction + 
                1.5 * gaussian_peaks + 
                0.3 * chaotic_component)