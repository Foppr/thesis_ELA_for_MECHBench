import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like self-similarity with chaotic sine maps and multi-resolution components
        fractal = 0.0
        for i in range(1, min(8, self.dim + 1)):
            scale = 3.0 ** (-i)
            fractal += scale * np.sum(np.sin(scale * x) * np.cos(scale * x**3) * np.tanh(scale * x**2))
        
        # Quantum-inspired interference with complex phase coupling and dynamic amplitude modulation
        quantum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Limited interaction range
                dist = np.abs(x[i] - x[j])
                phase = np.sin(dist * np.pi / 2.0) * np.cos(dist * np.pi / 4.0)
                amplitude = 1.0 + 0.5 * np.sin(i * np.pi / self.dim) * np.cos(j * np.pi / self.dim)
                quantum += amplitude * phase * np.exp(-dist**2 / 8.0)
        
        # Adaptive elliptic landscape with dynamic eccentricity and orientation, plus quartic terms
        elliptic = 0.0
        for i in range(self.dim):
            eccentricity = 1.5 + 0.8 * np.sin(i * np.pi / self.dim) * np.cos(i * np.pi / (self.dim + 1))
            elliptic += (x[i]**2) / (eccentricity**2) + eccentricity**2 * (x[i]**4) + 0.3 * x[i]**6
        
        # Augmented Gaussian mixture with chaotic centers, varying widths, and dynamic weights
        gaussian_mixture = 0.0
        for i in range(min(10, self.dim)):
            center = 4.0 * np.sin(i * np.pi / 5.0) * np.cos(i * np.pi / 7.0)
            width = 1.2 + 0.4 * np.sin(i * np.pi / 6.0)
            weight = 0.6 + 0.4 * np.sin(i * np.pi / 8.0) * np.cos(i * np.pi / 9.0)
            gaussian_mixture += weight * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Novel hyperbolic tangent coupling with multi-scale interaction and dynamic conditioning
        ht_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                ht_coupling += np.tanh(dist) * np.sin(dist * np.pi / 3.0) * np.exp(-dist**2 / 12.0)
        
        # Dynamic conditioning with time-varying exponents and non-linear transformation
        condition = 1.0
        for i in range(self.dim):
            exponents = [1.0, 1.5, 2.0, 2.5, 3.0]
            exp_idx = i % len(exponents)
            condition *= (1.0 + 0.4 * np.sin(x[i] * np.pi / 5.0) * np.cos(x[i] * np.pi / 3.0) * exponents[exp_idx])
        
        # Combined function value with normalization and fitness landscape enhancement
        result = condition * (fractal + quantum + elliptic + gaussian_mixture + ht_coupling)
        
        # Add small random noise to break symmetry and increase robustness
        noise = 0.015 * np.random.rand()
        
        return result + noise