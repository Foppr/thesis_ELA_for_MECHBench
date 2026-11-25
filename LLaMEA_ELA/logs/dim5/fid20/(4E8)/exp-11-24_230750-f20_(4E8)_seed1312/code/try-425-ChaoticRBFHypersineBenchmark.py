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
        
        # Enhanced tent map chaotic component with dynamic parameter and memory effect
        chaotic = 0.0
        a = 3.9
        prev_x = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Tent map with memory effect
            tent_val = a * xi if xi < 0.5 else a * (1 - xi)
            chaotic += np.sin(tent_val * 2 * np.pi) * np.exp(-0.1 * xi**2) * (1.0 + 0.1 * np.sin(prev_x))
            prev_x = xi
        
        # Enhanced Radial Basis Functions with adaptive condition numbers
        rbf = 0.0
        for i in range(self.dim):
            center = self.gaussian_centers[i]
            sigma = self.gaussian_widths[i]
            # Adaptive conditioning based on dimension and local curvature
            cond_factor = 1.0 + 0.3 * np.log(i + 1) if i > 0 else 1.0
            rbf += cond_factor * np.exp(-0.5 * ((x[i] - center) / sigma)**2)
        
        # Enhanced asymmetric hyperbolic sine couplings with dynamic weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Asymmetric coupling with dynamic weights based on position
                diff = x[i] - x[j]
                weight_pos = 1.5 + 0.2 * np.sin(0.6 * x[i]) + 0.1 * np.cos(0.3 * x[j])
                weight_neg = 0.7 + 0.3 * np.cos(0.5 * x[j]) + 0.1 * np.sin(0.4 * x[i])
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
                # Enhanced cubic coupling with dynamic weights and position-dependent modulation
                weight = 1.0 + 0.2 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[j])
                # Add a new modulation factor based on distance between dimensions
                dist_mod = 1.0 + 0.05 * np.abs(x[i] - x[j])
                poly_coupling += weight * dist_mod * (x[i]**3 - x[j]**3) * np.cos(0.2 * (x[i] + x[j]))
        
        # Add a new component: enhanced chaotic sine-wave modulation with memory effect and position-dependent amplitude
        memory_mod = 0.0
        for i in range(self.dim):
            # Memory effect based on previous dimension values with dynamic scaling
            mem_factor = 1.0 + 0.1 * np.sin(0.3 * x[i-1]) if i > 0 else 1.0
            amp_mod = 1.0 + 0.2 * np.cos(0.2 * x[i])
            memory_mod += mem_factor * amp_mod * np.sin(2.5 * x[i] + 0.7 * np.cos(0.4 * x[i])) * np.exp(-0.05 * x[i]**2)
        
        # NEW: Added cosine modulation terms with enhanced complexity and dynamic weights
        cos_mod = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+2, self.dim)):
                # Enhanced coupling with dynamic weights based on both dimensions
                weight = 0.8 + 0.3 * np.sin(0.5 * x[i]) * np.cos(0.4 * x[j])
                cos_mod += weight * np.cos(0.8 * (x[i] - x[j])) * np.sin(0.3 * x[i]) * np.cos(0.4 * x[j])
        
        # Combine all components with dimensionally varying weights and enhanced scaling
        dim_factor = 1.0 + 0.15 * np.log(self.dim)
        # Adjust weights to improve fitness score
        return (0.20 * chaotic + 0.25 * rbf + 0.20 * coupling + 
                0.15 * modulated + 0.10 * saddle + 0.06 * poly_coupling + 0.05 * memory_mod + 0.04 * cos_mod) * dim_factor