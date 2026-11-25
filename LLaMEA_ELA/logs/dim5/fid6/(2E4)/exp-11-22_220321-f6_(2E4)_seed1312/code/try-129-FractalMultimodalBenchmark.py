import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_depth = 4
        self.wave_freq_base = 2.0
        self.gradient_adaptation = 0.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal component using recursive self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            coord = x[i]
            for depth in range(self.fractal_depth):
                coord = np.sin(coord * (2 ** depth)) * 0.5
            fractal_term += coord ** 2
        
        # Wave interference from multiple frequencies
        wave_term = 0.0
        for i in range(self.dim):
            freq = self.wave_freq_base + 0.1 * np.sin(i * 0.3)
            phase = np.cos(i * 0.7)
            wave_term += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
        
        # Adaptive gradient field with position-dependent modulation
        grad_term = 0.0
        for i in range(self.dim):
            mod = 1.0 + self.gradient_adaptation * np.sin(x[i] * 0.5)
            grad_term += mod * (x[i] ** 3) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional interaction with fractal scaling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + (x[i] + x[j])**2)
                scale = 1.0 / (1.0 + dist**2)
                cross_term += scale * np.sin(x[i] * x[j])
        
        # Position-dependent exponential decay with sinusoidal modulation
        exp_term = 0.0
        for i in range(self.dim):
            decay = np.exp(-0.2 * np.abs(x[i]))
            mod = np.cos(i * 0.4 + np.sin(x[i] * 0.3))
            exp_term += decay * mod
        
        # Global scaling based on dimensionality and coordinate sum
        global_scale = 1.0 + 0.2 * np.sin(self.dim * 0.1) * np.cos(np.sum(x) * 0.05)
        
        return global_scale * (0.25 * fractal_term + 0.2 * wave_term + 0.25 * grad_term + 0.2 * cross_term + 0.1 * exp_term)