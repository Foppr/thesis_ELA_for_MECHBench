import numpy as np

class PolynomialRBFChaosLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced polynomial chaos coefficients with structured higher-order terms
        self.poly_coeffs = np.random.randn(dim, 10)
        # RBF centers with improved distribution and adaptive widths
        self.rbf_centers = np.random.uniform(-1, 1, (dim, 15))
        self.rbf_widths = 0.2 + np.random.rand(15) * 3.0
        # Structured spectral decomposition with clustered eigenvalues for better conditioning
        self.eigenvals = np.sort(np.random.rand(dim) * 15 + 2)[::-1] ** 1.3
        self.eigenvecs = np.random.randn(dim, dim)
        self.eigenvecs, _ = np.linalg.qr(self.eigenvecs)
        # Harmonic coupling with adaptive phase modulation and frequency scaling
        self.harmonic_freqs = np.random.randint(1, 12, dim)
        self.phase_modulators = np.random.rand(dim, 3)
        # Add structured fractal scaling through geometric progression
        self.fractal_scale = 0.6 + np.random.rand() * 0.4
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial chaos expansion with structured cross-terms
        poly_sum = 0.0
        for i in range(self.dim):
            for j in range(10):
                poly_sum += self.poly_coeffs[i, j] * np.polynomial.hermite.hermval(x_norm[i], [0]*j + [1])
        
        # Enhanced RBF component with adaptive influence and multi-scale modulation
        rbf_sum = 0.0
        for i in range(self.dim):
            for j in range(15):
                dist = np.linalg.norm(x_norm[i] - self.rbf_centers[i, j])
                rbf_sum += np.exp(-self.rbf_widths[j] * dist**2) * (1.0 + 0.2 * np.sin(dist * 8))
        
        # Spectral decomposition with structured eigenvalue clustering
        spectral_sum = 0.0
        for i in range(self.dim):
            spectral_sum += self.eigenvals[i] * (x_norm[i] ** 2)
        
        # Cross-dimension coupling with adaptive phase modulation
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_i = np.dot(self.phase_modulators[i], [1, x_norm[i], x_norm[j]])
                phase_j = np.dot(self.phase_modulators[j], [1, x_norm[i], x_norm[j]])
                interaction = np.sin(self.harmonic_freqs[i] * phase_i + self.harmonic_freqs[j] * phase_j)
                cross_sum += interaction * (x_norm[i]**2 + x_norm[j]**2)
        
        # Add higher-order polynomial terms with structured non-linearity
        quartic_sum = 0.0
        for i in range(self.dim):
            quartic_sum += x_norm[i] ** 4
        
        quintic_sum = 0.0
        for i in range(self.dim):
            quintic_sum += x_norm[i] ** 5
            
        # Add sextic and octic terms with structured scaling
        sextic_sum = 0.0
        for i in range(self.dim):
            sextic_sum += x_norm[i] ** 6
            
        octic_sum = 0.0
        for i in range(self.dim):
            octic_sum += x_norm[i] ** 8
        
        # Combine components with dynamic weighting and fractal scaling
        result = (0.2 * poly_sum + 0.25 * rbf_sum + 0.2 * spectral_sum + 
                 0.15 * cross_sum + 0.1 * quartic_sum + 0.08 * quintic_sum + 
                 0.06 * sextic_sum + 0.03 * octic_sum) * self.fractal_scale
        
        # Add chaotic modulation with structured dimensionality
        chaos_factor = 1.0 + 0.3 * np.sin(np.sum(x_norm) * np.pi * 2)
        
        # Apply transformation to increase gradient complexity and create sharper minima
        result = np.tanh(result) * (1.0 + 0.4 * np.abs(result))
        
        return result * chaos_factor