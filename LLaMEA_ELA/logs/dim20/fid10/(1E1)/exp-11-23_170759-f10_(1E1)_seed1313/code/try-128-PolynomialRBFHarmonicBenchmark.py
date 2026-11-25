import numpy as np

class PolynomialRBFHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute coefficients for polynomial chaos expansion
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, size=(dim, 5))
        # Precompute RBF centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, size=(10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, size=10)
        
    def f(self, x):
        x = np.array(x)
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial chaos expansion component
        for i in range(self.dim):
            poly_val = 0.0
            for j in range(5):
                poly_val += self.poly_coeffs[i, j] * (x[i] ** j)
            result += 0.3 * poly_val * np.exp(-0.1 * x[i]**2)
        
        # Radial basis function component with asymmetric widths
        for i in range(10):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            diff = x - center
            rbf_val = np.exp(-0.5 * np.sum((diff / width)**2))
            # Add asymmetry: different weights for positive and negative directions
            asym_weight = 1.0 + 0.3 * np.sign(x[0]) if self.dim > 0 else 1.0
            result += 0.4 * rbf_val * asym_weight
        
        # Asymmetric harmonic oscillator component
        for i in range(self.dim):
            freq = 2.0 * (i + 1)
            phase = 0.5 * i
            # Different amplitudes based on sign of coordinate
            amp = 0.5 + 0.3 * np.sign(x[i]) if x[i] != 0 else 0.5
            result += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] - phase)
        
        # Cross-dimensional coupling with polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add complex coupling term with exponential decay
                coupling = (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                result += 0.2 * coupling * (1.0 + 0.1 * (i + j))
        
        # Add a global modulation term based on distance from origin
        r = np.sqrt(np.sum(x**2))
        result += 0.3 * np.sin(5.0 * r) * np.exp(-0.2 * r)
        
        # Add boundary attraction with varying strength
        for i in range(self.dim):
            boundary_term = (5.0 - abs(x[i]))**4
            if boundary_term > 0:
                result += 0.15 * boundary_term
        
        # Add noise-like component with chaotic behavior
        chaos_factor = 0.0
        for i in range(min(3, self.dim)):
            chaos_factor += np.sin(10.0 * x[i] + np.cos(7.0 * x[i]))
        result += 0.25 * chaos_factor
        
        # Add higher-order polynomial interaction
        if self.dim >= 4:
            for i in range(4):
                result += 0.1 * (x[i]**3) * np.sin(x[i]) * (1.0 + 0.05 * i)
        
        return result