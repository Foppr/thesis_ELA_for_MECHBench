import numpy as np

class PolynomialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Precompute orthogonal polynomial coefficients for chaos expansion
        self.poly_coeffs = np.random.randn(dim, 7) * 0.6
        self.coupling_matrix = np.random.randn(dim, dim) * 0.4
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base polynomial chaos expansion with varying degrees
        f_val = 0.0
        for i in range(self.dim):
            # Adaptive polynomial terms with dynamic weights
            poly_term = 0.0
            for deg in range(1, 8):
                poly_term += self.poly_coeffs[i, deg-1] * (x_norm[i] ** deg)
            
            # Dynamic weighting based on position and dimension
            weight = 1.0 + 0.6 * np.sin(4 * np.pi * x_norm[i]) + 0.4 * np.cos(3 * np.pi * x_norm[i])
            f_val += weight * poly_term
            
        # Spectral filtering with dynamic frequency modulation
        for i in range(self.dim):
            # Multi-frequency sine-cosine combinations with amplitude modulation
            freq_mod = 1.0 + 0.5 * np.sin(3 * np.pi * x_norm[i])
            f_val += 0.4 * np.sin(freq_mod * 9 * np.pi * x_norm[i]) * np.cos(freq_mod * 6 * np.pi * x_norm[i])
            
        # Dynamic coupling terms with time-varying interaction strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling strength based on distance and angle
                dist = np.abs(x_norm[i] - x_norm[j])
                angle = np.arctan2(x_norm[j], x_norm[i])
                coupling_strength = 0.6 * (1 + np.cos(5 * np.pi * dist)) * (1 + np.sin(4 * angle))
                f_val += coupling_strength * np.sin(7 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(5 * np.pi * (x_norm[i] - x_norm[j]))
                
        # Chaotic modulation with logistic map-like behavior
        chaos_factor = 1.0
        for i in range(self.dim):
            chaos_factor *= (1.7 * np.abs(x_norm[i]) * (1 - np.abs(x_norm[i])))
        f_val += 0.3 * chaos_factor * np.sin(9 * np.pi * x_norm[0]) * np.cos(7 * np.pi * x_norm[-1])
        
        # Multi-scale harmonic components with varying amplitudes
        for scale in [0.3, 0.7, 1.2, 1.8]:
            harmonic_sum = 0.0
            for i in range(self.dim):
                harmonic_sum += np.sin(scale * 4 * np.pi * x_norm[i]) * np.cos(scale * 3 * np.pi * x_norm[i])
            f_val += 0.2 * harmonic_sum ** 2
            
        # Non-separable high-order interaction with variable conditioning
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Variable conditioning based on dimension indices
                cond_factor = (i + 2) / (j + 2)
                f_val += 0.3 * cond_factor * (x_norm[i]**4 + x_norm[j]**4) * np.sin(6 * np.pi * (x_norm[i] + x_norm[j]))
                
        # Improved adaptive conditioning with piecewise linear transformation
        for i in range(self.dim):
            if x_norm[i] < -0.6:
                f_val += 0.15 * (x_norm[i] + 0.6)**2
            elif x_norm[i] > 0.6:
                f_val += 0.15 * (x_norm[i] - 0.6)**2
            else:
                f_val += 0.08 * x_norm[i]**4
                
        # Add separable quadratic components to improve algorithm discrimination
        sep_term = 0.0
        for i in range(self.dim):
            sep_term += 0.15 * (x_norm[i] - 0.4)**2 + 0.1 * (x_norm[i] + 0.3)**4
            
        # Add correlation structure to reduce algorithm bias
        corr_term = 0.0
        for i in range(self.dim-1):
            corr_term += 0.1 * np.sin(4 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i+1])
            
        f_val += sep_term + corr_term
        
        return f_val