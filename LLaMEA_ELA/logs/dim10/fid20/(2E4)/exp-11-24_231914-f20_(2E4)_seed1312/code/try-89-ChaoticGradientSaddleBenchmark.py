import numpy as np

class ChaoticGradientSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for scalability
        self.chaotic_params = [3.8, 4.0, 3.6, 3.9, 3.7][:min(dim, 5)]
        self.saddle_points = np.random.uniform(-2.0, 2.0, (3, dim))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        base = np.sum(x**2) / self.dim
        
        # Chaotic gradient component with logistic map behavior
        chaotic = 0.0
        for i in range(self.dim):
            # Use logistic map for chaotic dynamics
            r = self.chaotic_params[i % len(self.chaotic_params)]
            x_scaled = (x[i] + 5.0) / 10.0  # Normalize to [0, 1]
            chaotic += r * x_scaled * (1 - x_scaled) * np.sin(2 * np.pi * x[i])
        
        # Saddle point interactions with multi-scale harmonic modulations
        saddle = 0.0
        for i in range(self.dim):
            for j in range(len(self.saddle_points)):
                dist = np.sqrt(np.sum((x - self.saddle_points[j])**2))
                saddle += self.saddle_points[j][i] * np.sin(dist) * np.exp(-0.1 * dist**2)
        
        # Multi-scale harmonic modulation with varying frequencies
        harmonics = 0.0
        for i in range(self.dim):
            freqs = [1.0, 2.5, 4.0, 6.5, 8.0][:min(i+1, 5)]
            for k, freq in enumerate(freqs):
                harmonics += np.sin(freq * x[i]) * np.cos(freq * x[i]**2) * \
                            np.exp(-0.05 * np.abs(x[i] - k))
        
        # Discontinuous regions with piecewise non-smooth behavior
        discontinuous = 0.0
        for i in range(self.dim):
            if x[i] < -1:
                discontinuous += np.sin(10 * x[i]) * np.exp(-0.5 * x[i]**2)
            elif x[i] > 1:
                discontinuous += np.cos(8 * x[i]) * np.exp(-0.3 * x[i]**2)
            else:
                discontinuous += np.sin(4 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Asymmetric coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += 0.5 * np.sin(2 * x[i]) * np.cos(3 * x[i+1]) * \
                       np.exp(-0.1 * (x[i] - x[i+1])**2)
        
        # Fractal-like self-similarity with recursive modulation
        fractal = 0.0
        for i in range(self.dim):
            # Recursive scaling factor
            scale_factor = 1.0
            for j in range(3):
                scale_factor *= np.sin(2**j * x[i])
            fractal += scale_factor * np.exp(-0.15 * np.abs(x[i]))
        
        # Combine all components with different weights to create complex landscape
        return base + 1.8 * chaotic + 1.2 * saddle + 0.9 * harmonics + 0.7 * discontinuous + \
               0.6 * coupling + 0.5 * fractal