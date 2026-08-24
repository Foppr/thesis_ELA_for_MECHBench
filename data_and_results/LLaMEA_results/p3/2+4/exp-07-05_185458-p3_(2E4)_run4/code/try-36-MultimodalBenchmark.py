import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute harmonic coefficients for spherical harmonics
        self.harmonic_coeffs = np.random.uniform(-1, 1, (dim, dim))
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial chaos component with mixed degrees
        poly_chaos = np.sum((x_norm**2 + 0.5 * x_norm**4 + 0.1 * x_norm**6) * np.random.uniform(0.5, 1.5, self.dim))
        
        # Radial basis function component with varying widths
        rbf = 0.0
        for i in range(self.dim):
            rbf += np.exp(-np.sum((x_norm - np.random.uniform(-1, 1, self.dim))**2) / (2 * (0.5 + 0.5 * np.sin(i))))
        
        # Spherical harmonic interaction terms
        sph_harm = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sph_harm += np.sin(self.harmonic_coeffs[i, j] * (x_norm[i] + x_norm[j])) * np.cos(self.harmonic_coeffs[i, j] * (x_norm[i] - x_norm[j]))
        
        # Cross-dimensional coupling with trigonometric functions
        cross_coupling = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm))
        
        # Nonlinear transformation with exponential decay
        nonlinear = np.sum(np.exp(-np.abs(x_norm)) * np.sin(10 * x_norm) * np.cos(7 * x_norm))
        
        # Add noise component to increase robustness
        noise = np.sum(np.random.normal(0, 0.01, self.dim) * x_norm)
        
        # Combine all components with adaptive weights
        return 0.5 * poly_chaos + 0.3 * rbf + 0.2 * sph_harm + 0.1 * cross_coupling + 0.15 * nonlinear + 0.05 * noise