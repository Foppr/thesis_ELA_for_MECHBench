import numpy as np

class ChaoticRBFHypersineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for tent map
        self.chebyshev_coeffs = np.random.uniform(-1, 1, (dim, 5))
        self.gaussian_centers = np.random.uniform(-3, 3, dim)
        self.gaussian_widths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced tent map chaotic component with dynamic parameter
        chaotic = 0.0
        a = 3.85
        for i in range(self.dim):
            xi = x[i]
            # Tent map: f(x) = a * x if x < 0.5 else a * (1 - x)
            tent_val = a * xi if xi < 0.5 else a * (1 - xi)
            chaotic += np.sin(tent_val * 2 * np.pi) * np.exp(-0.12 * xi**2)
        
        # Enhanced Radial Basis Functions with adaptive condition numbers
        rbf = 0.0
        for i in range(self.dim):
            center = self.gaussian_centers[i]
            sigma = self.gaussian_widths[i]
            # Adaptive conditioning based on dimension
            cond_factor = 1.0 + 0.35 * np.log(i + 1) if i > 0 else 1.0
            rbf += cond_factor * np.exp(-0.5 * ((x[i] - center) / sigma)**2)
        
        # Enhanced asymmetric hyperbolic sine couplings
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Asymmetric coupling: different weights for positive/negative differences
                diff = x[i] - x[j]
                weight_pos = 1.6 + 0.15 * np.sin(0.7 * x[i])
                weight_neg = 0.75 + 0.25 * np.cos(0.6 * x[j])
                coupling += (weight_pos * np.sinh(diff) if diff >= 0 else 
                           weight_neg * np.sinh(-diff)) * np.cos(0.35 * (x[i] + x[j]))
        
        # Enhanced multi-scale periodic modulation with chebyshev polynomials
        modulated = 0.0
        for i in range(self.dim):
            freq = 1.4 + 1.8 * np.sin(0.35 * x[i])
            amp = 0.75 + 0.75 * np.cos(0.45 * x[i])
            # Use Chebyshev polynomials for modulation
            T = self.chebyshev_coeffs[i]
            poly_mod = T[0] + T[1]*x[i] + T[2]*np.cos(2*x[i]) + T[3]*np.sin(3*x[i]) + T[4]*np.cos(4*x[i])
            modulated += amp * np.sin(freq * x[i]) * poly_mod
        
        # Enhanced saddle point structure with hyperbolic tangent dynamics
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                tanh_term = np.tanh(0.35 * x[i] + 0.45 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * tanh_term
        
        # Add a new component: cross-dimensional polynomial coupling with modified exponents
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**4 - x[j]**2) * np.cos(0.25 * (x[i] + x[j]))
        
        # Combine all components with dimensionally varying weights
        dim_factor = 1.0 + 0.18 * np.log(self.dim)
        return (0.22 * chaotic + 0.23 * rbf + 0.27 * coupling + 
                0.14 * modulated + 0.09 * saddle + 0.05 * poly_coupling) * dim_factor