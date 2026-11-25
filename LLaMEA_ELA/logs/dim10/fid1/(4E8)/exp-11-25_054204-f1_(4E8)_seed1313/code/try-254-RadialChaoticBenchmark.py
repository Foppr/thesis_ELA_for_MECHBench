import numpy as np

class RadialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial and angular components for structured complexity
        self.radii = np.linspace(0.1, 5.0, dim)
        self.angles = np.linspace(0.0, 2 * np.pi, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial quadratic component
        r = np.sqrt(np.sum(x**2))
        f1 = 0.5 * r**2
        
        # Sinusoidal radial modulation with chaotic frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            f2 -= 0.3 * np.sin(freq * r) * np.cos(freq * x[i])
        
        # Polynomial chaos with radial coupling
        f3 = 0.2 * np.sum(x**4 - 2 * x**2 + 1)
        
        # Adaptive cross-dimensional interaction
        f4 = 0.15 * np.sum(np.sin(x) * np.cos(1.5 * x)) + 0.1 * np.sum(np.sin(2 * x) * np.cos(x))
        
        # Radial harmonic with exponential decay
        f5 = 0.25 * np.sum(np.exp(-x**2 / 10.0) * np.sin(3 * r))
        
        # Fractal-like angular coupling
        angular_coupling = 0.0
        for i in range(self.dim - 1):
            angular_coupling += np.sin(x[i] + x[i+1]) * np.cos(x[i] - x[i+1])
        f6 = 0.18 * angular_coupling
        
        # Spherical harmonic with dynamic scaling
        f7 = 0.2 * np.sum(np.sin(r) * np.cos(2 * r)) * (1 + 0.2 * np.sin(np.sum(x**2)))
        
        # Multi-scale oscillation with chaotic modulation
        f8 = 0.12 * np.sum(np.sin(5 * x) * np.cos(7 * x) * np.exp(-r / 3.0))
        
        # Radial polynomial chaos with sinusoidal weighting
        f9 = 0.1 * np.sum((x**6) * np.sin(r / 2.0))
        
        # Adaptive radial coupling with cubic interaction
        f10 = 0.15 * np.sum(x**3 * np.cos(1.2 * r))
        
        # Combined scaling factor based on dimensionality
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Final function value with refined weights
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)