import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute harmonic coefficients for different dimensions
        self.harmonic_coeffs = np.array([1.0 / (i + 1)**1.5 for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map component with chaotic dynamics
        logistic = 0.0
        r = 3.95
        for i in range(self.dim):
            if i == 0:
                x_prev = 0.5
            else:
                x_prev = x[i-1]
            logistic += (r * x_prev * (1 - x_prev))**2
        
        # Spherical harmonics component with angular dependencies
        spherical = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x[(i+1) % self.dim], x[i])
            spherical += np.sin(angle * (i + 1)) * np.cos(angle * (i + 2))
        
        # Multilevel sinusoidal modulations with varying frequencies and amplitudes
        modulation = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            amp = 1.0 + 0.5 * np.cos(i * 0.7)
            modulation += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Adaptive conditioning with dimension-dependent scaling
        condition = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(i * 0.3)
            condition += (x[i]**2) / (scale + 0.1 * i)
        
        # Cross-dimensional coupling with interaction terms
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                cross += (dist**2) / (1.0 + dist**3)
        
        # Asymmetric penalty with exponential scaling
        penalty = np.sum(0.5 * np.exp(np.abs(x) - 4.8) * (x > 4.8) + 
                        0.5 * np.exp(-np.abs(x) + 4.8) * (x < -4.8))
        
        # Combine all components with dynamic weights
        total = 0.3 * logistic + 0.25 * spherical + 0.2 * modulation + 0.15 * condition + 0.1 * cross + penalty
        
        return total