import numpy as np

class PolynomialHarmonicRBF:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency components for harmonic terms
        self.frequencies = np.arange(1, min(6, dim + 1))
        # Precompute radial basis function centers and widths
        self.rbf_centers = np.linspace(-4.0, 4.0, min(8, dim * 2))
        self.rbf_widths = np.logspace(-1, 1, min(8, dim * 2))
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential terms (quartic and sextic)
        poly_potential = np.sum(0.1 * x**4 + 0.02 * x**6)
        
        # Harmonic oscillator components with varying frequencies
        harmonic = 0.0
        for i, freq in enumerate(self.frequencies):
            if i < len(x):
                harmonic += 0.5 * freq**2 * x[i]**2 + 0.1 * np.sin(freq * x[i])
        
        # Radial basis function terms with varying widths and centers
        rbf = 0.0
        for i, center in enumerate(self.rbf_centers):
            if i < len(x):
                width = self.rbf_widths[i % len(self.rbf_widths)]
                rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Cross-term coupling between dimensions
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += 0.3 * (x[i]**2 + x[i+1]**2) * np.sin(0.5 * (x[i] - x[i+1]))
        
        # Global scaling and noise component
        result = poly_potential + harmonic + rbf + cross_term
        
        # Add a global conditioning factor that increases with dimensionality
        conditioning = 1.0 + 0.2 * np.log(self.dim + 1)
        result *= conditioning
        
        # Add small random noise to increase robustness
        noise = 0.001 * np.sum(np.random.randn(self.dim) * x)
        
        return result + noise