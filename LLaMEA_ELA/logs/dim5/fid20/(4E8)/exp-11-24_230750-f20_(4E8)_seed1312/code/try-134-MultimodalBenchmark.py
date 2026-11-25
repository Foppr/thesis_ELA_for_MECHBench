import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like self-similarity with chaotic sine maps and multi-resolution scaling
        fractal = 0.0
        for i in range(1, min(7, self.dim + 1)):
            scale = 2.0 ** (-i)
            fractal += scale * np.sum(np.sin(scale * x) * np.cos(scale * x**3))
        
        # Modified quantum-inspired interference with enhanced phase coupling and adaptive amplitudes
        quantum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(self.dim, i+4)):  # Limited coupling for complexity control
                dist = np.abs(x[i] - x[j])
                phase = dist * np.pi / 2.0 + 0.5 * np.sin(dist)
                quantum += np.sin(phase) * np.cos(phase) * np.exp(-dist**2 / 8.0)
        
        # Adaptive elliptic landscape with dynamic eccentricity and orientation
        elliptic = 0.0
        for i in range(self.dim):
            eccentricity = 1.0 + 0.7 * np.sin(i * np.pi / self.dim) * np.cos(i * np.pi / (self.dim + 1))
            elliptic += (x[i]**2) / (eccentricity**2) + eccentricity**3 * (x[i]**4)
        
        # Augmented Gaussian mixture with chaotic center placement and dynamic weights
        gaussian_mixture = 0.0
        for i in range(min(10, self.dim)):
            center = 4.0 * np.sin(i * np.pi / 5.0) * np.cos(i * np.pi / 7.0)
            width = 1.2 + 0.4 * np.sin(i * np.pi / 4.0)
            weight = 0.6 + 0.4 * np.sin(i * np.pi / 6.0)
            gaussian_mixture += weight * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Novel hyperbolic tangent coupling with exponential decay and multi-scale interaction
        tanh_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = np.tanh(x[i] - x[j]) * np.exp(-np.abs(x[i] - x[j]) / 3.0)
                tanh_coupling += diff**2
        
        # Dynamic conditioning with non-linear transformation and time-varying exponents
        condition = 1.0
        for i in range(self.dim):
            exponent = 1.5 + 0.5 * np.sin(x[i] * np.pi / 4.0)
            condition *= (1.0 + 0.4 * np.sin(x[i] * np.pi / 3.0) * np.cos(x[i] * np.pi / 5.0)) ** exponent
        
        # Combined function value with normalization and fitness landscape enhancement
        result = condition * (fractal + quantum + elliptic + gaussian_mixture + tanh_coupling)
        
        # Add small random noise to break symmetry and increase robustness
        noise = 0.005 * np.random.rand()
        
        return result + noise