import numpy as np

class PolynomialRBFHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute harmonic coefficients for stability
        self.harmonic_coeffs = np.array([np.sin(i * 0.7) * np.cos(i * 0.5) for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component
        poly_term = np.sum((x_norm ** 3 + 0.3 * x_norm ** 2 - 0.5 * x_norm) * self.harmonic_coeffs)
        
        # Radial basis function ensemble with dynamic centers
        rbf_sum = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.8 + 1.0) * 0.5
            width = 0.3 + 0.2 * np.cos(i * 0.6)
            rbf_sum += np.exp(-((x_norm[i] - center) ** 2) / (2 * width ** 2))
        
        # Dynamic harmonic coupling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (np.sin(x_norm[i] + x_norm[j]) * 
                           np.cos(0.5 * (x_norm[i] - x_norm[j])) * 
                           np.sin(0.3 * (i - j)))
        
        # Multi-scale oscillatory component
        oscillation = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(i * 0.4)
            amp = 1.0 + 0.5 * np.cos(i * 0.3)
            oscillation += amp * np.sin(freq * x_norm[i]) * np.cos(0.7 * x_norm[i])
        
        # Dimensional scaling with fractal-like behavior
        scale_factor = 1.0
        for i in range(self.dim):
            scale_factor *= (1.0 + 0.2 * np.sin(i * 3.14 / self.dim))
        
        # Combine all components
        result = (poly_term ** 2 + 
                 rbf_sum * 0.5 + 
                 coupling * 0.3 + 
                 oscillation * 0.4) * scale_factor
        
        return result