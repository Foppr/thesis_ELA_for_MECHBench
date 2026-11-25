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
        a = 3.9
        for i in range(self.dim):
            xi = x[i]
            # Tent map: f(x) = a * x if x < 0.5 else a * (1 - x)
            tent_val = a * xi if xi < 0.5 else a * (1 - xi)
            chaotic += np.sin(tent_val * 2 * np.pi) * np.exp(-0.1 * xi**2)
        
        # Enhanced Radial Basis Functions with adaptive condition numbers
        rbf = 0.0
        for i in range(self.dim):
            center = self.gaussian_centers[i]
            sigma = self.gaussian_widths[i]
            # Adaptive conditioning based on dimension
            cond_factor = 1.0 + 0.3 * np.log(i + 1) if i > 0 else 1.0
            rbf += cond_factor * np.exp(-0.5 * ((x[i] - center) / sigma)**2)
        
        # Enhanced asymmetric hyperbolic sine couplings
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Asymmetric coupling: different weights for positive/negative differences
                diff = x[i] - x[j]
                weight_pos = 1.5 + 0.2 * np.sin(0.6 * x[i])
                weight_neg = 0.7 + 0.3 * np.cos(0.5 * x[j])
                coupling += (weight_pos * np.sinh(diff) if diff >= 0 else 
                           weight_neg * np.sinh(-diff)) * np.cos(0.4 * (x[i] + x[j]))
        
        # Enhanced multi-scale periodic modulation with chebyshev polynomials
        modulated = 0.0
        for i in range(self.dim):
            freq = 1.5 + 2.0 * np.sin(0.3 * x[i])
            amp = 0.8 + 0.7 * np.cos(0.4 * x[i])
            # Use Chebyshev polynomials for modulation
            T = self.chebyshev_coeffs[i]
            poly_mod = T[0] + T[1]*x[i] + T[2]*np.cos(2*x[i]) + T[3]*np.sin(3*x[i]) + T[4]*np.cos(4*x[i])
            modulated += amp * np.sin(freq * x[i]) * poly_mod
        
        # Enhanced saddle point structure with hyperbolic tangent dynamics
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                tanh_term = np.tanh(0.4 * x[i] + 0.5 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * tanh_term
        
        # Add a new component: cross-dimensional polynomial coupling with enhanced nonlinearity
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced cubic coupling with dynamic weights
                weight = 1.0 + 0.2 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[j])
                poly_coupling += weight * (x[i]**3 - x[j]**3) * np.cos(0.2 * (x[i] + x[j]))
        
        # Add a new component: enhanced chaotic sine-wave modulation with memory effect
        memory_mod = 0.0
        for i in range(self.dim):
            # Memory effect based on previous dimension values
            mem_factor = 1.0
            if i > 0:
                mem_factor = 1.0 + 0.1 * np.sin(0.3 * x[i-1])
            memory_mod += mem_factor * np.sin(2.5 * x[i] + 0.7 * np.cos(0.4 * x[i])) * np.exp(-0.05 * x[i]**2)
        
        # Add a new component: enhanced asymmetric polynomial coupling with dynamic weights
        asym_poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric cubic coupling with dynamic weight modulation
                weight = 1.2 + 0.3 * np.sin(0.4 * x[i]) * np.cos(0.6 * x[j])
                diff = x[i] - x[j]
                asym_poly_coupling += weight * (diff**3) * np.sin(0.3 * (x[i] + x[j]))
        
        # Add a new component: enhanced multi-modal Gaussian with dynamic centers and widths
        multimodal_gauss = 0.0
        for i in range(self.dim):
            center = self.gaussian_centers[i] + 0.5 * np.sin(0.7 * x[i])
            sigma = self.gaussian_widths[i] * (1.0 + 0.2 * np.cos(0.5 * x[i]))
            multimodal_gauss += np.exp(-0.5 * ((x[i] - center) / sigma)**2)
        
        # Combine all components with dimensionally varying weights
        dim_factor = 1.0 + 0.15 * np.log(self.dim)
        return (0.15 * chaotic + 0.20 * rbf + 0.22 * coupling + 
                0.15 * modulated + 0.10 * saddle + 0.07 * poly_coupling + 0.06 * memory_mod +
                0.05 * asym_poly_coupling + 0.05 * multimodal_gauss) * dim_factor