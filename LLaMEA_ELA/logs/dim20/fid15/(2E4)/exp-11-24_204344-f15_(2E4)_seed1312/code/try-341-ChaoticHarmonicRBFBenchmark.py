import numpy as np

class ChaoticHarmonicRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters
        self.chebyshev_coeffs = np.random.randn(dim, 5)
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, 3))
        self.rbf_widths = np.random.uniform(0.5, 2.0, (dim, 3))
        self.harmonic_freqs = np.random.uniform(1.0, 5.0, dim)
        self.harmonic_amplitudes = np.random.uniform(0.5, 3.0, dim)
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic component using Chebyshev polynomials
        chaotic_term = 0.0
        for i in range(self.dim):
            coeffs = self.chebyshev_coeffs[i]
            T_x = np.cos(coeffs[0] * np.arccos(np.clip(x[i], -1, 1)))
            chaotic_term += coeffs[1] * T_x + coeffs[2] * T_x**2 + coeffs[3] * T_x**3 + coeffs[4] * T_x**4
        
        # Radial basis function component with multiple centers
        rbf_term = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[i, j]
                rbf_term += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Harmonic oscillation component with varying frequencies and amplitudes
        harmonic_term = 0.0
        for i in range(self.dim):
            freq = self.harmonic_freqs[i]
            amp = self.harmonic_amplitudes[i]
            harmonic_term += amp * np.sin(freq * x[i]) + amp * np.cos(freq * x[i] * 0.7)
        
        # Coupling between dimensions using chaotic interaction terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_factor = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                coupling_term += coupling_factor * (i + j) * 0.1
        
        # Gradient-enhanced component with non-uniform scaling
        grad_term = 0.0
        for i in range(self.dim):
            grad_term += (x[i]**2) * np.exp(-0.1 * x[i]**2) * np.sin(x[i] * 2)
        
        # Final combination with dynamic weighting based on dimensionality
        total = 0.35 * chaotic_term + 0.25 * rbf_term + 0.2 * harmonic_term + 0.1 * coupling_term + 0.1 * grad_term
        
        # Global modulation using a nonlinear transformation
        global_mod = 1.0 + 0.3 * np.sin(np.sum(x) * 0.5) * np.cos(np.sum(x) * 0.2)
        
        return total * global_mod