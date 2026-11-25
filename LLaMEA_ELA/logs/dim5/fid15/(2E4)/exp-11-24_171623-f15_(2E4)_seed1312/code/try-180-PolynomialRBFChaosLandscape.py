import numpy as np

class PolynomialRBFChaosLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced polynomial chaos coefficients with higher order terms and cross-terms
        self.poly_coeffs = np.random.randn(dim, 15)
        # More diverse RBF centers with fractal-like distribution
        self.rbf_centers = np.random.uniform(-1, 1, (dim, 25))
        self.rbf_widths = 0.05 + np.random.rand(25) * 5.0
        # Stronger spectral conditioning with fractal eigenvalue distribution
        self.eigenvals = np.sort(np.random.rand(dim) * 25 + 1)[::-1] ** 1.7
        self.eigenvecs = np.random.randn(dim, dim)
        self.eigenvecs, _ = np.linalg.qr(self.eigenvecs)
        # Harmonic coupling with quaternion-based phase modulation
        self.harmonic_freqs = np.random.randint(3, 20, dim)
        self.quaternion_phases = np.random.rand(dim, 4)
        # Add fractal self-similarity through recursive scaling
        self.fractal_scale = 0.3 + np.random.rand() * 0.7
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial chaos expansion with cross-dimension terms
        poly_sum = 0.0
        for i in range(self.dim):
            for j in range(15):
                poly_sum += self.poly_coeffs[i, j] * np.polynomial.hermite.hermval(x_norm[i], [0]*j + [1])
        
        # Enhanced RBF component with fractal-like spacing and multi-scale influence
        rbf_sum = 0.0
        for i in range(self.dim):
            for j in range(25):
                dist = np.linalg.norm(x_norm[i] - self.rbf_centers[i, j])
                rbf_sum += np.exp(-self.rbf_widths[j] * dist**2) * (1.0 + 0.15 * np.sin(dist * 15))
        
        # Spectral decomposition with fractal eigenvalue scaling
        spectral_sum = 0.0
        for i in range(self.dim):
            spectral_sum += self.eigenvals[i] * (x_norm[i] ** 2)
        
        # Cross-dimension coupling with quaternion phase modulation
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_i = np.dot(self.quaternion_phases[i], [1, x_norm[i], x_norm[j], 0])
                phase_j = np.dot(self.quaternion_phases[j], [1, x_norm[i], 0, x_norm[j]])
                interaction = np.sin(self.harmonic_freqs[i] * phase_i + self.harmonic_freqs[j] * phase_j)
                cross_sum += interaction * (x_norm[i]**2 + x_norm[j]**2)
        
        # Add higher-order polynomial terms for enhanced non-convexity
        quartic_sum = 0.0
        for i in range(self.dim):
            quartic_sum += x_norm[i] ** 4
        
        quintic_sum = 0.0
        for i in range(self.dim):
            quintic_sum += x_norm[i] ** 5
            
        # Add sextic and octic terms for maximum complexity
        sextic_sum = 0.0
        for i in range(self.dim):
            sextic_sum += x_norm[i] ** 6
            
        octic_sum = 0.0
        for i in range(self.dim):
            octic_sum += x_norm[i] ** 8
            
        # Add non-standard higher-order terms for increased complexity
        decic_sum = 0.0
        for i in range(self.dim):
            decic_sum += x_norm[i] ** 10
            
        dodecic_sum = 0.0
        for i in range(self.dim):
            dodecic_sum += x_norm[i] ** 12
        
        # Combine components with dynamic weighting and fractal scaling
        result = (0.12 * poly_sum + 0.22 * rbf_sum + 0.18 * spectral_sum + 
                 0.12 * cross_sum + 0.09 * quartic_sum + 0.07 * quintic_sum + 
                 0.05 * sextic_sum + 0.03 * octic_sum + 0.04 * decic_sum + 
                 0.02 * dodecic_sum) * self.fractal_scale
        
        # Add chaotic modulation with fractal dimensionality
        chaos_factor = 1.0 + 0.5 * np.sin(np.sum(x_norm) * np.pi * 4)
        
        # Apply transformation to increase non-convexity and create plateaus
        result = np.tanh(result) * (1.0 + 0.6 * np.abs(result))
        
        return result * chaos_factor