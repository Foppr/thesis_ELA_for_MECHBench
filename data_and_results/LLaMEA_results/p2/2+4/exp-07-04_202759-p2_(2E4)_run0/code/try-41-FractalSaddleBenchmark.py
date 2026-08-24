import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.scale_factor = 1.0
        self.fractal_depth = 3
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like polynomial component with self-similar structure
        fractal = 0.0
        for i in range(self.fractal_depth):
            scale = 2 ** i
            for j in range(self.dim):
                fractal += scale * np.sin(scale * x[j]) * np.cos(scale * x[j] * 0.5) * (1 + 0.1 * np.sin(scale * x[j]**2))
        
        # Saddle-point interaction terms with dynamic weights
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 + 0.5 * np.sin(0.3 * (x[i] + x[j]))
                saddle += weight * (x[i]**2 - x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Chaotic oscillation component with multi-scale frequency modulation
        chaotic = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.4 * x[i]) + 1.5 * np.cos(0.6 * x[i])
            chaotic += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.exp(-0.05 * x[i]**2)
        
        # Multi-modal sinusoidal landscape with varying amplitudes and frequencies
        modal = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.3 * np.sin(0.5 * x[i])
            freq = 2.0 + 1.5 * np.cos(0.4 * x[i])
            modal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Combined landscape with dynamic scaling and conditioning
        return 0.2 * fractal + 0.3 * saddle + 0.25 * chaotic + 0.25 * modal