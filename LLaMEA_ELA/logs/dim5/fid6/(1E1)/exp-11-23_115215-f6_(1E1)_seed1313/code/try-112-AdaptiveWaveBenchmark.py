import numpy as np

class AdaptiveWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute wave parameters
        self.wave_frequencies = np.random.uniform(0.5, 3.0, dim)
        self.wave_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.noise_levels = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term
        f_val = np.sum(x**4) * 0.1
        
        # Trigonometric wave components with adaptive frequencies and amplitudes
        for i in range(self.dim):
            wave = self.wave_amplitudes[i] * (
                np.sin(self.wave_frequencies[i] * x[i]) + 
                0.5 * np.cos(2 * self.wave_frequencies[i] * x[i])
            )
            f_val += wave
        
        # Polynomial coupling terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f_val += 0.3 * (x[i]**2) * (x[j]**3) * np.sin(x[i] + x[j])
        
        # Adaptive noise modulation based on position
        for i in range(self.dim):
            noise = self.noise_levels[i] * np.sin(x[i] * 5.0) * np.cos(x[i] * 2.0)
            f_val += noise
        
        # Cross-dimensional interaction with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                f_val += 0.2 * np.exp(-dist) * np.sin(x[i] * x[j])
        
        # Asymmetric polynomial terms with dynamic exponents
        for i in range(self.dim):
            exp_factor = 1.0 + 0.3 * np.sin(i * 0.7)
            f_val += 0.25 * (x[i]**(2 + exp_factor)) * np.cos(x[i])
        
        # Global trigonometric modulation
        f_val += 0.4 * np.sin(np.sum(x) * 0.3) * np.cos(np.sum(x) * 0.7)
        
        return f_val