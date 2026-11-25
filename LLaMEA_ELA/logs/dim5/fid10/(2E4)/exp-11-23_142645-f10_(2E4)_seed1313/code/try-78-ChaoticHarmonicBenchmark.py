import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute harmonic coefficients for different dimensions
        self.harmonic_coeffs = np.array([1.0 / (i + 1)**1.5 for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map component with altered chaotic dynamics
        logistic = 0.0
        r = 3.85  # Slightly reduced chaos parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = 0.5
            else:
                x_prev = x[i-1]
            logistic += (r * x_prev * (1 - x_prev))**1.8  # Nonlinear exponent change
        
        # Spherical harmonics component with modified weights
        spherical = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x[(i+1) % self.dim], x[i])
            # Modified angular dependencies with different harmonic weights
            spherical += (i + 1) * np.sin(angle * (i + 1)) * np.cos(angle * (i + 3))
        
        # Multilevel sinusoidal modulations with altered frequencies
        modulation = 0.0
        for i in range(self.dim):
            freq = 1.5 + 2.5 * np.sin(i * 0.4)  # Different frequency base
            amp = 1.2 + 0.3 * np.cos(i * 0.6)   # Modified amplitude
            modulation += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Adaptive conditioning with modified scaling
        condition = 0.0
        for i in range(self.dim):
            scale = 1.2 + 0.2 * np.sin(i * 0.4)  # Different scaling factor
            condition += (x[i]**2) / (scale + 0.05 * i**1.5)  # Modified denominator
        
        # Cross-dimensional coupling with new interaction terms
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                cross += (dist**1.8) / (1.0 + dist**2.5)  # Different power laws
        
        # Asymmetric penalty with modified exponential scaling
        penalty = np.sum(0.4 * np.exp(np.abs(x) - 4.9) * (x > 4.8) + 
                        0.6 * np.exp(-np.abs(x) + 4.9) * (x < -4.8))
        
        # Combine all components with new dynamic weights
        total = 0.25 * logistic + 0.3 * spherical + 0.25 * modulation + 0.1 * condition + 0.1 * cross + penalty
        
        return total