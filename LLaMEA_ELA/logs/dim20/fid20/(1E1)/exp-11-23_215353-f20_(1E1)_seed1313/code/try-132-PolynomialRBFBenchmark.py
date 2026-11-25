import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with mixed monomials
        poly_chaos = np.sum((x**3 + 0.7 * x**2.7 - 0.4 * x**1.8 + 0.9 * x + 0.6) ** 1.5)
        
        # Radial basis function with varying widths and centers
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, 15)
        for center in centers:
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / 1.0**2)
        
        # Spectral decomposition using sine and cosine components with varying frequencies
        spec_term = np.sum(np.sin(2.0 * x) + 0.6 * np.cos(3.0 * x) + 0.3 * np.sin(5.0 * x) + 0.2 * np.cos(7.0 * x))
        
        # Interaction terms between pairs of dimensions with varying coupling strengths
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += 0.5 * np.sin(x[i] + x[j]) * np.cos(0.5 * (x[i] - x[j]))
        
        # Multi-scale Gaussian modulation with different bandwidths
        gauss_mod = np.sum(np.exp(-0.2 * x**2) + 0.5 * np.exp(-0.8 * (x - 1.0)**2) + 0.3 * np.exp(-1.2 * (x + 1.5)**2))
        
        # High-order polynomial distortion with non-uniform exponents
        high_order = np.sum(0.4 * x**5 + 0.3 * x**4 - 0.2 * x**3 + 0.1 * x**2 - 0.8 * x + 0.9)
        
        # Cross-dimensional coupling with trigonometric interaction
        cross_coupling = np.sum(np.sin(0.5 * np.sum(x)) * np.cos(0.3 * np.sum(x**2)))
        
        # Add a global scaling factor to balance contribution of terms
        return 0.25 * poly_chaos + 0.20 * rbf_term + 0.15 * spec_term + 0.12 * interaction_term + 0.10 * gauss_mod + 0.08 * high_order + 0.05 * cross_coupling + 1.5