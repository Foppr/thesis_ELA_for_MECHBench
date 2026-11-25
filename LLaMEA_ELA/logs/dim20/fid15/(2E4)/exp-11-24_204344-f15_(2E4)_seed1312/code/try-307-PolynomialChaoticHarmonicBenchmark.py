import numpy as np

class PolynomialChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Polynomial chaos expansion with Legendre polynomials and dynamic weights
        chaos_term = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.sin(i * 0.5 + self.dim * 0.2)
            poly_val = np.polynomial.legendre.legval(x[i], [0, 0, 0, 1])  # P3(x) = x^3
            chaos_term += weight * poly_val ** 2
        
        # Hyperbolic tangent gradient modulation with directional scaling
        tanh_term = 0.0
        for i in range(self.dim):
            scale = 2.0 + 1.5 * np.cos(i * 0.3 + self.dim * 0.4)
            direction = np.tanh(x[i] * scale) * np.sin(i * 0.7)
            tanh_term += direction ** 3
        
        # Spherical harmonic coupling with angular frequency modulation
        sphere_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.0 + 2.0 * np.sin(i * 0.4)
                freq_j = 1.0 + 2.0 * np.cos(j * 0.3)
                angle_ij = np.arctan2(x[j], x[i])
                sphere_term += np.sin(freq_i * angle_ij) * np.cos(freq_j * angle_ij)
        
        # Multi-scale oscillatory component with frequency modulation
        oscillation_term = 0.0
        for i in range(self.dim):
            freq_mod = 3.0 + 2.0 * np.sin(i * 0.6 + self.dim * 0.3)
            amp_mod = 1.0 + 0.8 * np.cos(i * 0.5)
            oscillation_term += amp_mod * np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.3)
        
        # Asymmetric exponential decay with position-dependent parameters
        exp_term = 0.0
        for i in range(self.dim):
            decay_rate = 0.5 + 0.8 * np.sin(i * 0.4 + self.dim * 0.25)
            base = 1.0 + 0.5 * np.cos(i * 0.3)
            exp_term += base * np.exp(-decay_rate * np.abs(x[i]))
        
        # Cross-dimensional interaction with cosine coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = np.cos(x[i] * x[j]) * (1.0 + 0.2 * np.sin(i + j))
                    cross_term += coupling
        
        # Final weighted combination with adaptive scaling
        total = 0.25 * chaos_term + 0.20 * tanh_term + 0.15 * sphere_term + 0.20 * oscillation_term + 0.10 * exp_term + 0.10 * cross_term
        
        # Global conditioning factor with dynamic adjustment
        condition_factor = 1.0 + 0.3 * np.sin(self.dim * 0.5) * np.cos(self.dim * 0.2)
        
        return total * condition_factor