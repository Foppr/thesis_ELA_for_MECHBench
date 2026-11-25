import numpy as np

class FractalOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal component using self-similar patterns
        fractal = 0
        for i in range(self.dim):
            # Create fractal-like behavior with recursive-like terms
            term = np.sin(2**i * np.pi * x_norm[i]) * np.cos(3**i * np.pi * x_norm[i])
            fractal += term / (1.0 + i * 0.1)
        
        # Harmonic oscillator component with varying frequencies and damping
        harmonic = 0
        for i in range(self.dim):
            freq = 2**(i % 3)  # Frequencies 1, 2, 4, 1, 2, 4, ...
            damp = 1.0 / (1.0 + 0.1 * i)
            harmonic += damp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Multi-scale interaction terms with geometric progression
        interaction = 0
        scales = [1, 2, 4, 8]
        for scale in scales:
            if scale <= self.dim:
                # Grouped interactions with scaling
                group_sum = np.sum(x_norm[:scale]**2)
                interaction += np.sin(np.pi * group_sum) * np.cos(2 * np.pi * group_sum)
        
        # Asymmetric conditioning terms with exponential weights
        conditioning = 0
        for i in range(self.dim):
            if x_norm[i] >= 0:
                conditioning += (x_norm[i]**3) * np.exp(-0.5 * x_norm[i]**2)
            else:
                conditioning += (x_norm[i]**5) * np.exp(-0.3 * x_norm[i]**2)
        
        # Boundary attraction terms to encourage exploration near bounds
        boundary = 0
        for i in range(self.dim):
            boundary += 10 * (np.abs(x_norm[i]) - 1)**4
        
        # Combined result with adaptive scaling
        result = 1.5 * fractal + 1.2 * harmonic + 0.8 * interaction + 0.6 * conditioning + 0.4 * boundary
        
        return result