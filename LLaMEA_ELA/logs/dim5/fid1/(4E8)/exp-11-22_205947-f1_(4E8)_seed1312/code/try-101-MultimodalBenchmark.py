import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like radial component with multi-scale oscillations
        radial = np.sum(x**2)
        fractal = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(0.5 * i) + 0.3 * np.cos(0.3 * i)
            fractal += scale * np.sin(10.0 * np.sqrt(radial + 1e-8)) * np.cos(7.0 * x[i])
        
        # Rotation-invariant chaotic component with dynamic phase shifts
        chaotic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = np.arctan2(x[j], x[i]) + 0.1 * np.sin(0.3 * (i + j))
                chaotic += np.sin(15.0 * angle) * np.cos(12.0 * angle) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Multi-scale interference pattern with varying frequencies and amplitudes
        interference = 0.0
        for i in range(self.dim):
            freqs = [2.0, 4.0, 6.0, 8.0]
            amps = [1.0, 0.7, 0.5, 0.3]
            for f, a in zip(freqs, amps):
                interference += a * np.sin(f * x[i]) * np.cos(f * x[i] + np.pi/4)
        
        # Dynamic conditioning with dimension-dependent scaling
        condition = 1.0 + 0.2 * np.log(self.dim + 1) + 0.1 * np.sin(0.5 * self.dim)
        
        # Combine all components with adaptive weights
        total = condition * (0.3 * radial + 0.4 * fractal + 0.2 * chaotic + 0.1 * interference)
        
        # Add noise-like perturbations for increased complexity
        noise = 0.01 * np.sum(np.sin(50.0 * x) + np.cos(30.0 * x))
        
        return total + noise