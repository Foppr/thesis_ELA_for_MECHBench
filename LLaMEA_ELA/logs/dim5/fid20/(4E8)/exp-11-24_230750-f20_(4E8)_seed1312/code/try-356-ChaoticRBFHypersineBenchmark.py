import numpy as np

class ChaoticRBFHypersineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for tent map
        self.chebyshev_coeffs = np.random.uniform(-1, 1, (dim, 5))
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Tent map chaotic component with dynamic parameter
        chaotic = 0.0
        a = 3.8
        for i in range(self.dim):
            xi = x[i]
            # Tent map: f(x) = a * x if x < 0.5 else a * (1 - x)
            tent_val = a * xi if xi < 0.5 else a * (1 - xi)
            chaotic += np.sin(tent_val * 2 * np.pi) * np.exp(-0.1 * xi**2)
        
        # Radial Basis Functions with adaptive condition numbers
        rbf = 0.0
        for i in range(self.dim):
            center = np.sin(0.5 * x[i]) * 3.0
            sigma = 0.5 + 0.3 * np.cos(0.7 * x[i])
            # Adaptive conditioning based on dimension
            cond_factor = 1.0 + 0.2 * np.log(i + 1) if i > 0 else 1.0
            rbf += cond_factor * np.exp(-0.5 * ((x[i] - center) / sigma)**2)
        
        # Asymmetric hyperbolic sine couplings
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Asymmetric coupling: different weights for positive/negative differences
                diff = x[i] - x[j]
                weight_pos = 1.2 + 0.3 * np.sin(0.5 * x[i])
                weight_neg = 0.8 + 0.4 * np.cos(0.6 * x[j])
                coupling += (weight_pos * np.sinh(diff) if diff >= 0 else 
                           weight_neg * np.sinh(-diff)) * np.cos(0.3 * (x[i] + x[j]))
        
        # Multi-scale periodic modulation with chebyshev polynomials
        modulated = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.4 * x[i])
            amp = 1.0 + 0.5 * np.cos(0.3 * x[i])
            # Use Chebyshev polynomials for modulation
            T = self.chebyshev_coeffs[i]
            poly_mod = T[0] + T[1]*x[i] + T[2]*np.cos(2*x[i]) + T[3]*np.sin(3*x[i]) + T[4]*np.cos(4*x[i])
            modulated += amp * np.sin(freq * x[i]) * poly_mod
        
        # Saddle point structure with hyperbolic tangent dynamics
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                tanh_term = np.tanh(0.5 * x[i] + 0.3 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * tanh_term
        
        # Combine all components with dimensionally varying weights
        dim_factor = 1.0 + 0.1 * np.log(self.dim)
        return (0.25 * chaotic + 0.30 * rbf + 0.20 * coupling + 
                0.15 * modulated + 0.10 * saddle) * dim_factor