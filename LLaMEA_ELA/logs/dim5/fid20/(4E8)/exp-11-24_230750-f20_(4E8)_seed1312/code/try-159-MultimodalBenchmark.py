import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial polynomial conditioning with enhanced dynamic exponents
        r_squared = np.sum(x**2)
        radial_condition = 1.0 + 0.5 * np.sin(r_squared / 8.0) * np.cos(r_squared / 4.0)
        
        # Composite sinusoidal waves with modified frequencies and amplitudes
        wave = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.3 * np.sin(i * np.pi / (self.dim + 2))
            amp = 1.2 + 0.1 * np.cos(i * np.pi / (self.dim + 3))
            wave += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Rotationally symmetric chaotic structure with modified interference
        rotation = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = np.arctan2(x[j], x[i])
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                rotation += np.sin(dist * (i + j) / 3.0) * np.cos(angle * (i + j) * 0.5)
        
        # Adaptive noise modulation with modified amplitude
        noise_amp = 0.03 * (1.0 + 0.4 * np.sin(r_squared / 6.0))
        noise = noise_amp * np.random.randn()
        
        # Combined function value with normalization
        result = radial_condition * (wave + rotation) + noise
        
        return result