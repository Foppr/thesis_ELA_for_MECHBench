import numpy as np

class PolynomialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Precompute orthogonal polynomial coefficients for chaos expansion
        self.poly_coeffs = np.random.randn(dim, 5) * 0.5
        self.coupling_matrix = np.random.randn(dim, dim) * 0.3
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base polynomial chaos expansion with varying degrees
        f_val = 0.0
        for i in range(self.dim):
            # Adaptive polynomial terms with dynamic weights
            poly_term = 0.0
            for deg in range(1, 6):
                poly_term += self.poly_coeffs[i, deg-1] * (x_norm[i] ** deg)
            
            # Dynamic weighting based on position and dimension
            weight = 1.0 + 0.5 * np.sin(3 * np.pi * x_norm[i]) + 0.3 * np.cos(2 * np.pi * x_norm[i])
            f_val += weight * poly_term
            
        # Spectral filtering with dynamic frequency modulation
        for i in range(self.dim):
            # Multi-frequency sine-cosine combinations with amplitude modulation
            freq_mod = 1.0 + 0.4 * np.sin(2 * np.pi * x_norm[i])
            f_val += 0.3 * np.sin(freq_mod * 7 * np.pi * x_norm[i]) * np.cos(freq_mod * 5 * np.pi * x_norm[i])
            
        # Dynamic coupling terms with time-varying interaction strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling strength based on distance and angle
                dist = np.abs(x_norm[i] - x_norm[j])
                angle = np.arctan2(x_norm[j], x_norm[i])
                coupling_strength = 0.5 * (1 + np.cos(4 * np.pi * dist)) * (1 + np.sin(3 * angle))
                f_val += coupling_strength * np.sin(6 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(4 * np.pi * (x_norm[i] - x_norm[j]))
                
        # Chaotic modulation with logistic map-like behavior
        chaos_factor = 1.0
        for i in range(self.dim):
            chaos_factor *= (1.5 * np.abs(x_norm[i]) * (1 - np.abs(x_norm[i])))
        f_val += 0.2 * chaos_factor * np.sin(8 * np.pi * x_norm[0]) * np.cos(6 * np.pi * x_norm[-1])
        
        # Multi-scale harmonic components with varying amplitudes
        for scale in [0.5, 1.0, 2.0]:
            harmonic_sum = 0.0
            for i in range(self.dim):
                harmonic_sum += np.sin(scale * 3 * np.pi * x_norm[i]) * np.cos(scale * 2 * np.pi * x_norm[i])
            f_val += 0.15 * harmonic_sum ** 2
            
        # Non-separable high-order interaction with variable conditioning
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Variable conditioning based on dimension indices
                cond_factor = (i + 1) / (j + 1)
                f_val += 0.2 * cond_factor * (x_norm[i]**3 + x_norm[j]**3) * np.sin(5 * np.pi * (x_norm[i] + x_norm[j]))
                
        # Adaptive conditioning with piecewise linear transformation
        for i in range(self.dim):
            if x_norm[i] < -0.5:
                f_val += 0.1 * (x_norm[i] + 0.5)**2
            elif x_norm[i] > 0.5:
                f_val += 0.1 * (x_norm[i] - 0.5)**2
            else:
                f_val += 0.05 * x_norm[i]**4
                
        return f_val