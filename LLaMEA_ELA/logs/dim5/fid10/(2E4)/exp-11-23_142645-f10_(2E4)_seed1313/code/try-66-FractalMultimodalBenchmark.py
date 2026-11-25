import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic component with varying parameters
        chaotic = 0.0
        r_values = [3.8, 3.9, 4.0] * (self.dim // 3 + 1)
        for i in range(self.dim):
            chaotic += r_values[i % len(r_values)] * x[i] * (1 - x[i])
        
        # Adaptive elliptic terms with dynamic eccentricity
        elliptic = 0.0
        for i in range(self.dim):
            eccentricity = 1.0 + 0.5 * np.sin(0.3 * i)
            elliptic += (x[i]**2) / (eccentricity**2 + 0.1)
        
        # Hybrid gradient-sine interaction terms with phase modulation
        hybrid = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(0.5 * (x[i] + x[j]))
                hybrid += np.sin(3.0 * x[i]) * np.cos(2.0 * x[j]) * phase
        
        # Modified fractal sine-wave with dynamic amplitude scaling
        fractal_sine = 0.0
        for i in range(self.dim):
            amplitude = 1.0 + 0.3 * np.sin(0.7 * i)
            fractal_sine += amplitude * np.sin(4.0 * x[i]) * np.cos(6.0 * x[i])
        
        # Cross-dimensional penalty with exponential scaling
        penalty = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                penalty += 0.5 * np.exp(2.0 * (np.abs(x[i]) - 4.5))
        
        # Global normalization and weighted combination
        return 0.3 * chaotic + 0.25 * elliptic + 0.2 * hybrid + 0.15 * fractal_sine + penalty