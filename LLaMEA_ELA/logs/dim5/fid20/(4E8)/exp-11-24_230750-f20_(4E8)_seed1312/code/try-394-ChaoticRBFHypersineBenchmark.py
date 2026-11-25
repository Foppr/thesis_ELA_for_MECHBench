import numpy as np

class ChaoticRBFHypersineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for logistic map
        self.logistic_r = np.random.uniform(3.57, 4.0, dim)
        self.gaussian_centers = np.random.uniform(-3, 3, dim)
        self.gaussian_widths = np.random.uniform(0.5, 2.0, dim)
        # Additional fractal parameters
        self.fractal_exponents = np.random.uniform(0.1, 2.0, dim)
        self.coupling_weights = np.random.uniform(0.5, 2.0, (dim, dim))
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced logistic map chaotic component with dynamic parameter
        chaotic = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Logistic map: f(x) = r * x * (1 - x)
            logistic_val = self.logistic_r[i] * xi * (1 - xi)
            chaotic += np.sin(logistic_val * 3 * np.pi) * np.exp(-0.15 * xi**2)
        
        # Enhanced Radial Basis Functions with adaptive condition numbers
        rbf = 0.0
        for i in range(self.dim):
            center = self.gaussian_centers[i]
            sigma = self.gaussian_widths[i]
            # Adaptive conditioning based on dimension and fractal exponent
            cond_factor = 1.0 + 0.4 * np.log(i + 1) * self.fractal_exponents[i]
            rbf += cond_factor * np.exp(-0.5 * ((x[i] - center) / sigma)**2)
        
        # Enhanced asymmetric polynomial couplings with fractal modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                diff = x[i] - x[j]
                # Asymmetric weights with fractal modulation
                weight_pos = 2.0 + 0.3 * np.sin(0.7 * x[i]) * self.fractal_exponents[i]
                weight_neg = 1.0 + 0.2 * np.cos(0.5 * x[j]) * self.fractal_exponents[j]
                coupling += (weight_pos * diff**3 if diff >= 0 else 
                           weight_neg * diff**3) * np.cos(0.3 * (x[i] + x[j]))
        
        # Enhanced multi-scale fractal modulation with Chebyshev polynomials
        modulated = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.4 * x[i])
            amp = 1.0 + 0.8 * np.cos(0.5 * x[i])
            # Use Chebyshev polynomials for fractal modulation
            T = np.array([1, x[i], 2*x[i]**2 - 1, 4*x[i]**3 - 3*x[i], 8*x[i]**4 - 8*x[i]**2 + 1])
            poly_mod = np.sum(T * np.random.uniform(-1, 1, 5))
            modulated += amp * np.sin(freq * x[i]) * poly_mod
        
        # Enhanced saddle point structure with hyperbolic tangent dynamics
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                tanh_term = np.tanh(0.5 * x[i] + 0.3 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * tanh_term
        
        # Enhanced cross-dimensional polynomial coupling with memory effect
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Memory-dependent coupling
                memory_factor = 1.0 + 0.1 * np.sin(0.2 * (x[i] + x[j]))
                poly_coupling += (x[i]**4 - x[j]**4) * np.cos(0.15 * (x[i] + x[j])) * memory_factor
        
        # Combine all components with dimensionally varying weights
        dim_factor = 1.0 + 0.2 * np.log(self.dim)
        return (0.18 * chaotic + 0.22 * rbf + 0.23 * coupling + 
                0.18 * modulated + 0.12 * saddle + 0.07 * poly_coupling) * dim_factor