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
        # Add fractal-like recursive structures
        self.fractal_depth = np.random.randint(2, 6, dim)
        self.fractal_weights = np.random.uniform(0.1, 0.8, (dim, 3))
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic component using Chebyshev polynomials with higher degree
        chaotic_term = 0.0
        for i in range(self.dim):
            coeffs = self.chebyshev_coeffs[i]
            T_x = np.cos(coeffs[0] * np.arccos(np.clip(x[i], -1, 1)))
            chaotic_term += coeffs[1] * T_x + coeffs[2] * T_x**2 + coeffs[3] * T_x**3 + \
                           coeffs[4] * T_x**4 + coeffs[5] * T_x**5 + coeffs[6] * T_x**6
        
        # Radial basis function component with more centers and fractal-like interaction
        rbf_term = 0.0
        for i in range(self.dim):
            for j in range(5):
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[i, j]
                # Add fractal scaling factor
                fractal_scale = np.sum([self.fractal_weights[i, k] * np.sin((j+1) * x[i]) for k in range(3)])
                rbf_term += np.exp(-0.5 * ((x[i] - center) / (width + 0.1 * fractal_scale))**2)
        
        # Harmonic oscillation component with multiple frequencies and amplitudes
        harmonic_term = 0.0
        for i in range(self.dim):
            freq1 = self.harmonic_freqs[i]
            amp1 = self.harmonic_amplitudes[i]
            freq2 = freq1 * np.random.uniform(0.5, 1.5)
            amp2 = amp1 * np.random.uniform(0.5, 1.5)
            harmonic_term += amp1 * np.sin(freq1 * x[i]) + amp2 * np.cos(freq2 * x[i] * 0.7)
        
        # Coupling between dimensions using chaotic interaction terms with recursive structure
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add recursive coupling based on fractal depth
                recursive_factor = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                depth_factor = (i + j) * 0.05 * np.sin(self.fractal_depth[i] * x[i] * x[j])
                coupling_term += recursive_factor * depth_factor
        
        # Gradient-enhanced component with non-uniform scaling and fractal modulation
        grad_term = 0.0
        for i in range(self.dim):
            # Add fractal modulation to gradient term
            fractal_mod = np.sum([self.fractal_weights[i, k] * np.cos((k+1) * x[i]) for k in range(3)])
            grad_term += (x[i]**2) * np.exp(-0.1 * x[i]**2) * np.sin(x[i] * 2) * fractal_mod
        
        # Fractal-like recursive structure component
        fractal_term = 0.0
        for i in range(self.dim):
            # Recursive application of chaotic functions
            val = x[i]
            for depth in range(self.fractal_depth[i]):
                val = np.sin(val * (depth + 1)) + np.cos(val * (depth + 2))
            fractal_term += val**2
        
        # Final combination with dynamic weighting based on dimensionality and fractal complexity
        total = 0.25 * chaotic_term + 0.20 * rbf_term + 0.25 * harmonic_term + \
                0.15 * coupling_term + 0.10 * grad_term + 0.05 * fractal_term
        
        # Global modulation using a nonlinear transformation with fractal characteristics
        global_mod = 1.0 + 0.4 * np.sin(np.sum(x) * 0.3) * np.cos(np.sum(x) * 0.1) * \
                     np.exp(-0.01 * np.sum(np.abs(x)))
        
        return total * global_mod