import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like sequences for scale and attraction dynamics
        self.fractal_scale = np.logspace(-1, 1, dim, base=2.0)
        self.attraction_strength = np.sin(np.arange(dim) * np.pi / 3.0) * 0.5 + 0.5
        self.periodic_freq = np.cos(np.arange(dim) * np.pi / 2.0) * 0.8 + 1.2
        self.basin_shift = np.tan(np.arange(dim) * np.pi / 4.0) * 0.3 + 0.7
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with fractal scaling
        result = 0.0
        for i in range(self.dim):
            result += 0.5 * self.fractal_scale[i] * (x[i] - 1.0)**2
        
        # Add gradient-based attraction fields with dynamic strength
        for i in range(self.dim):
            attraction = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = (x[i] - x[j])**2
                    attraction += self.attraction_strength[i] * np.exp(-dist / (2.0 * self.fractal_scale[j]))
            result += 0.3 * attraction
        
        # Add periodic forcing with fractal frequency modulation
        for i in range(self.dim):
            result += 0.2 * np.sin(self.periodic_freq[i] * x[i] + self.basin_shift[i]) * \
                      np.cos(self.periodic_freq[i] * x[i] + self.basin_shift[i]**2)
        
        # Add self-similar fractal components at multiple scales
        for scale in [0.5, 1.0, 2.0, 4.0]:
            fractal_term = 0.0
            for i in range(self.dim):
                fractal_term += np.sin(scale * x[i] + self.basin_shift[i]) * \
                               np.cos(scale * x[i] + self.basin_shift[i]**2)
            result += 0.05 * fractal_term / scale
        
        # Add multi-scale harmonic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = 0.1 * np.sin(self.fractal_scale[i] * x[i] + self.fractal_scale[j] * x[j]) * \
                              np.cos(self.fractal_scale[i] * x[i] + self.fractal_scale[j] * x[j])
                result += interaction
        
        # Add basin boundary complexity with chaotic shift
        for i in range(self.dim):
            boundary = 0.1 * np.sin(10.0 * x[i] + self.basin_shift[i] * np.pi) * \
                       np.cos(8.0 * x[i] + self.basin_shift[i]**2 * np.pi)
            result += boundary
        
        # Add chaotic noise with scale-dependent amplitude
        noise = 0.0
        for i in range(self.dim):
            noise += 0.02 * np.sin(30.0 * x[i] + self.fractal_scale[i] * np.pi) * \
                     np.cos(25.0 * x[i] + self.fractal_scale[i]**2 * np.pi)
        result += noise
        
        # Add polynomial coupling with fractal coefficients
        result += 0.001 * np.sum(x**3) + 0.0005 * np.sum(x**5) + 0.0001 * np.sum(x**7)
        
        return result