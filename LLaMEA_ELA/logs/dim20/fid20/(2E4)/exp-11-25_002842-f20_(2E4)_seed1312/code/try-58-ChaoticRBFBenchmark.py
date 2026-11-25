import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic tent map parameters
        self.chebyshev_coeffs = np.random.uniform(-1, 1, dim)
        
    def f(self, x):
        # Scale input to [-1, 1] range
        scaled_x = x / 5.0
        
        # Chaotic tent map component with varying parameter
        chaotic = 0.0
        a = 1.8
        for i in range(self.dim):
            if i == 0:
                xi = scaled_x[i]
            else:
                xi = scaled_x[i] * (a * scaled_x[i-1] if scaled_x[i-1] < 0.5 else a * (1 - scaled_x[i-1]))
            chaotic += np.sin(xi * np.pi) * np.cos(xi * np.pi / 2)
        
        # Radial basis function component with Gaussian kernels
        rbf = 0.0
        centers = np.random.uniform(-1, 1, (10, self.dim))
        widths = np.random.uniform(0.1, 0.5, 10)
        
        for i in range(10):
            diff = scaled_x - centers[i]
            rbf += widths[i] * np.exp(-np.sum(diff**2) / (2 * widths[i]**2))
        
        # Polynomial interaction terms
        poly = 0.0
        for i in range(self.dim):
            poly += (scaled_x[i]**3) * np.sin(scaled_x[i]) + (scaled_x[i]**4) * np.cos(scaled_x[i])
        
        # Cross-dimensional coupling with Chebyshev polynomials
        chebyshev = 0.0
        for i in range(self.dim):
            chebyshev += self.chebyshev_coeffs[i] * np.cos((i+1) * np.arccos(scaled_x[i]))
        
        # Sinusoidal modulation with varying frequencies
        modulated = 0.0
        for i in range(self.dim):
            modulated += np.sin(2**(i+1) * scaled_x[i]) * np.cos(3**(i+1) * scaled_x[i])
        
        # Add a noise term with chaotic amplitude modulation
        noise = 0.05 * np.sum(np.sin(13 * scaled_x) + np.cos(17 * scaled_x))
        
        # Combine all components with adaptive weights
        return 0.8 * (chaotic + rbf + poly + chebyshev + modulated + noise)