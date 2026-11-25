import numpy as np

class PolynomialStochasticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial chaos coefficients
        self.poly_coeffs = np.random.randn(dim, 6) * 0.5
        # Stochastic differential equation parameters
        self.diffeq_params = np.random.rand(dim) * 2.0 + 1.0
        # Dynamic coupling weights between dimensions
        self.coupling_weights = np.random.rand(dim, dim) * 0.3 + 0.1
        # Frequency modulation factors
        self.freq_mods = np.random.rand(dim) * 3.0 + 1.0
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Polynomial chaos expansion terms
        poly_terms = []
        for i in range(self.dim):
            coeffs = self.poly_coeffs[i]
            x_i = x_norm[i]
            # 6th order polynomial with mixed monomials
            poly_val = (coeffs[0] + 
                       coeffs[1] * x_i + 
                       coeffs[2] * x_i**2 + 
                       coeffs[3] * x_i**3 + 
                       coeffs[4] * x_i**4 + 
                       coeffs[5] * x_i**5)
            poly_terms.append(poly_val)
        
        # Stochastic differential equation components
        diff_terms = []
        for i in range(self.dim):
            x_i = x_norm[i]
            # SDE-driven term with frequency modulation
            sde_term = np.sin(self.freq_mods[i] * x_i) * np.exp(-0.5 * x_i**2)
            # Add noise component
            noise = np.random.normal(0, 0.1) * (1.0 + 0.2 * np.sin(5.0 * x_i))
            diff_terms.append(sde_term + noise)
        
        # Cross-dimension coupling with dynamic weights
        coupling_terms = []
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_weights[i][j] * np.sin(x_norm[i] - x_norm[j])
            coupling_terms.append(coupling_sum)
        
        # Dynamic curvature modulation
        curvature_mod = []
        for i in range(self.dim):
            x_i = x_norm[i]
            # Time-varying curvature factor based on input position
            curv_factor = 1.0 + 0.5 * np.sin(2.0 * x_i) * np.cos(3.0 * x_i)
            curvature_mod.append(curv_factor)
        
        # Combine all terms with adaptive weighting
        result = (np.sum(np.array(poly_terms) * np.array(curvature_mod)) + 
                 0.7 * np.sum(np.array(diff_terms)) + 
                 0.3 * np.sum(np.array(coupling_terms)))
        
        # Add global scaling and noise
        global_scale = 1.0 + 0.1 * np.sin(0.5 * np.sum(x_norm**2))
        noise = np.random.normal(0, 0.01) * (1.0 + 0.05 * np.cos(np.sum(x_norm)))
        
        return result * global_scale + noise