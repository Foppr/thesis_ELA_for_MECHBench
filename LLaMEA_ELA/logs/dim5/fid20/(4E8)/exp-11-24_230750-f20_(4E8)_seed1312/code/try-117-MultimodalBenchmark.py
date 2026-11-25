import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similarity pattern with recursive scaling and multi-resolution components
        fractal = 0.0
        for i in range(1, min(6, self.dim + 1)):
            scale = 2.0 ** (-i)
            fractal += scale * np.sum(np.sin(scale * x) * np.cos(scale * x**2))
        
        # Quantum-inspired interference terms with phase modulation and complex amplitude coupling
        quantum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                quantum += np.sin(dist * np.pi) * np.cos(dist * np.pi / 2.0) * np.exp(-dist**2 / 10.0)
        
        # Adaptive elliptic landscape with dynamic eccentricity and orientation
        elliptic = 0.0
        for i in range(self.dim):
            eccentricity = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            elliptic += (x[i]**2) / (eccentricity**2) + eccentricity**2 * (x[i]**4)
        
        # Multi-scale Gaussian mixture with varying centers, widths, and weights
        gaussian_mixture = 0.0
        for i in range(min(8, self.dim)):
            center = 3.0 * np.sin(i * np.pi / 4.0)
            width = 1.0 + 0.3 * np.cos(i * np.pi / 3.0)
            weight = 0.5 + 0.5 * np.sin(i * np.pi / 5.0)
            gaussian_mixture += weight * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Dynamic conditioning with time-varying exponents and non-linear transformation
        condition = 1.0
        for i in range(self.dim):
            condition *= (1.0 + 0.3 * np.sin(x[i] * np.pi / 5.0) * np.cos(x[i] * np.pi / 3.0))
        
        # Combined function value with normalization and fitness landscape enhancement
        result = condition * (fractal + quantum + elliptic + gaussian_mixture)
        
        # Add small random noise to break symmetry and increase robustness
        noise = 0.01 * np.random.rand()
        
        return result + noise