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
            fractal += term / (1.0 + i * 0.15)
        
        # Harmonic oscillator component with varying frequencies and damping
        harmonic = 0
        for i in range(self.dim):
            freq = 2**(i % 4)  # Frequencies 1, 2, 4, 8, 1, 2, 4, 8, ...
            damp = 1.0 / (1.0 + 0.15 * i)
            harmonic += damp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Multi-scale interaction terms with geometric progression
        interaction = 0
        scales = [1, 3, 6, 12]  # Changed scale values for more complex interactions
        for scale in scales:
            if scale <= self.dim:
                # Grouped interactions with scaling
                group_sum = np.sum(x_norm[:scale]**2)
                interaction += np.sin(np.pi * group_sum) * np.cos(3 * np.pi * group_sum)  # Changed frequency
        
        # Asymmetric conditioning terms with exponential weights
        conditioning = 0
        for i in range(self.dim):
            if x_norm[i] >= 0:
                conditioning += (x_norm[i]**3) * np.exp(-0.7 * x_norm[i]**2)  # Changed exponent and coefficient
            else:
                conditioning += (x_norm[i]**5) * np.exp(-0.4 * x_norm[i]**2)  # Changed exponent and coefficient
        
        # Boundary attraction terms to encourage exploration near bounds
        boundary = 0
        for i in range(self.dim):
            boundary += 15 * (np.abs(x_norm[i]) - 1)**4  # Increased boundary influence
        
        # Combined result with adaptive scaling
        result = 1.8 * fractal + 1.5 * harmonic + 1.0 * interaction + 0.7 * conditioning + 0.5 * boundary
        
        return result