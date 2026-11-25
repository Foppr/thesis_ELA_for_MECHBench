import numpy as np

class ChaoticPolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters
        self.chebyshev_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        # Polynomial chaos expansion coefficients
        self.poly_chaos_coeffs = np.random.normal(0.0, 1.0, (dim, 8))
        # Spherical harmonic components
        self.sph_harm_l = np.random.randint(1, 6, dim)
        self.sph_harm_m = np.random.randint(-5, 6, dim)
        # Interaction weights between dimensions
        self.interaction_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        np.fill_diagonal(self.interaction_weights, 0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chebyshev polynomial chaos component
        chebyshev_sum = 0
        for i in range(self.dim):
            xi = x[i] / 5.0  # Normalize to [-1, 1]
            T = np.ones_like(xi)
            U = 2 * xi
            poly_val = self.chebyshev_coeffs[i, 0] + self.chebyshev_coeffs[i, 1] * U
            for j in range(2, 5):
                T_new = 2 * xi * U - T
                poly_val += self.chebyshev_coeffs[i, j] * T_new
                T, U = U, T_new
            chebyshev_sum += poly_val
            
        # Logistic map chaotic component
        logistic_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Logistic map: x_{n+1} = r * x_n * (1 - x_n)
            logistic_val = self.logistic_r[i] * xi * (1 - xi)
            logistic_sum += logistic_val * np.sin(xi * np.pi / 2) * np.cos(xi * np.pi / 4)
            
        # Polynomial chaos expansion with higher order terms
        poly_chaos_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = (self.poly_chaos_coeffs[i, 0] + 
                        self.poly_chaos_coeffs[i, 1] * xi + 
                        self.poly_chaos_coeffs[i, 2] * xi**2 + 
                        self.poly_chaos_coeffs[i, 3] * xi**3 +
                        self.poly_chaos_coeffs[i, 4] * xi**4 +
                        self.poly_chaos_coeffs[i, 5] * xi**5 +
                        self.poly_chaos_coeffs[i, 6] * xi**6 +
                        self.poly_chaos_coeffs[i, 7] * xi**7)
            poly_chaos_sum += poly_term
            
        # Spherical harmonic component
        sph_harm_sum = 0
        for i in range(self.dim):
            r = np.sqrt(x[i]**2 + 1e-8)  # Add small epsilon to avoid zero
            theta = np.arctan2(x[i], 1.0)
            phi = np.arctan2(1.0, x[i])
            
            # Spherical harmonic Y_l^m(θ, φ)
            Y_lm = (np.sqrt((2 * self.sph_harm_l[i] + 1) * np.math.factorial(self.sph_harm_l[i] - abs(self.sph_harm_m[i])) / 
                           (4 * np.pi * np.math.factorial(self.sph_harm_l[i] + abs(self.sph_harm_m[i])))) *
                   np.cos(self.sph_harm_m[i] * phi) * np.sin(theta)**abs(self.sph_harm_m[i]))
            
            sph_harm_sum += Y_lm * r**(self.sph_harm_l[i])
            
        # Cross-dimension interaction with chaotic coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction += (self.interaction_weights[i, j] * 
                                  np.sin(x[i]) * np.cos(x[j]) * 
                                  (np.exp(-x[i]**2) + np.exp(-x[j]**2)))
        
        # Combine all components with adjusted weights
        result = (1.5 * chebyshev_sum + 
                 1.3 * logistic_sum + 
                 1.4 * poly_chaos_sum + 
                 0.8 * sph_harm_sum + 
                 0.6 * interaction)
        
        return result