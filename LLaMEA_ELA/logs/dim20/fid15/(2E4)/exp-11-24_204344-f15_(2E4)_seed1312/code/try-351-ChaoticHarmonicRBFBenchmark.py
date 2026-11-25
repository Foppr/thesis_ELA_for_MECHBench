import numpy as np

class ChaoticHarmonicRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters with higher complexity
        self.chebyshev_coeffs = np.random.randn(dim, 7)
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (dim, 5))
        self.rbf_widths = np.random.uniform(0.3, 2.5, (dim, 5))
        self.harmonic_freqs = np.random.uniform(0.5, 8.0, dim)
        self.harmonic_amplitudes = np.random.uniform(0.3, 4.0, dim)
        # Additional fractal-like recursive parameters
        self.fractal_depth = np.random.randint(2, 6, dim)
        self.fractal_weights = np.random.uniform(0.1, 1.0, (dim, 3))
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic component using Chebyshev polynomials with higher degree
        chaotic_term = 0.0
        for i in range(self.dim):
            coeffs = self.chebyshev_coeffs[i]
            T_x = np.cos(coeffs[0] * np.arccos(np.clip(x[i], -1, 1)))
            chaotic_term += coeffs[1] * T_x + coeffs[2] * T_x**2 + coeffs[3] * T_x**3 + \
                           coeffs[4] * T_x**4 + coeffs[5] * T_x**5 + coeffs[6] * T_x**6
        
        # Radial basis function component with more centers and fractal-like scaling
        rbf_term = 0.0
        for i in range(self.dim):
            for j in range(5):
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[i, j]
                # Fractal-like recursive scaling
                scale_factor = np.sum([self.fractal_weights[i, k] * np.sin((j+1) * x[i] * (k+1)) 
                                     for k in range(3)])
                rbf_term += np.exp(-0.5 * ((x[i] - center) / width)**2) * scale_factor
        
        # Harmonic oscillation component with multiple frequencies and fractal coupling
        harmonic_term = 0.0
        for i in range(self.dim):
            freq1 = self.harmonic_freqs[i]
            amp1 = self.harmonic_amplitudes[i]
            freq2 = freq1 * np.sin(x[i] * 0.3) + 1.0
            amp2 = amp1 * np.cos(x[i] * 0.7) + 1.0
            harmonic_term += amp1 * np.sin(freq1 * x[i]) + amp2 * np.cos(freq2 * x[i] * 0.7)
        
        # Coupling between dimensions using fractal-like recursive terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Recursive fractal coupling with depth-dependent interaction
                recursive_factor = 1.0
                for k in range(min(self.fractal_depth[i], self.fractal_depth[j])):
                    recursive_factor *= np.sin(x[i] * x[j] * (k+1)) * np.cos(x[i] + x[j] * (k+1))
                coupling_term += recursive_factor * (i + j) * 0.1
        
        # Gradient-enhanced component with non-uniform scaling and chaotic modulation
        grad_term = 0.0
        for i in range(self.dim):
            # Chaotic modulation of gradient term
            modulator = np.sin(x[i] * 3.0) * np.cos(x[i] * 1.5) + 1.5
            grad_term += (x[i]**2) * np.exp(-0.1 * x[i]**2) * np.sin(x[i] * 2) * modulator
        
        # Fractal-like recursive structure in final combination
        total = 0.25 * chaotic_term + 0.20 * rbf_term + 0.25 * harmonic_term + \
                0.15 * coupling_term + 0.15 * grad_term
        
        # Global modulation using a nonlinear transformation with fractal characteristics
        global_mod = 1.0 + 0.4 * np.sin(np.sum(x) * 0.5) * np.cos(np.sum(x) * 0.2) * \
                     np.sin(np.sum(x**2) * 0.1)
        
        return total * global_mod