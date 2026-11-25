import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial polynomial conditioning with dynamic exponents
        r_squared = np.sum(x**2)
        radial_condition = 1.0 + 0.3 * np.sin(r_squared / 10.0) * np.cos(r_squared / 5.0)
        
        # Composite sinusoidal waves with varying frequencies and amplitudes
        wave = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i * np.pi / self.dim)
            amp = 1.0 + 0.2 * np.cos(i * np.pi / (self.dim + 1))
            wave += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Rotationally symmetric chaotic structure with multi-scale interference
        rotation = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = np.arctan2(x[j], x[i])
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                rotation += np.sin(dist * (i + j) / 2.0) * np.cos(angle * (i + j))
        
        # Adaptive noise modulation based on position
        noise_amp = 0.05 * (1.0 + 0.5 * np.sin(r_squared / 5.0))
        noise = noise_amp * np.random.randn()
        
        # Combined function value with normalization
        result = radial_condition * (wave + rotation) + noise
        
        return result