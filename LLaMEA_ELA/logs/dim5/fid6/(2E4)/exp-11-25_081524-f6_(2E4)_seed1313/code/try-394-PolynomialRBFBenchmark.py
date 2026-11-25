import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients for different orders
        self.poly_coeffs = {}
        for i in range(1, 8):
            self.poly_coeffs[i] = np.random.normal(0, 1, i+1)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial basis function with polynomial chaos expansion
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            # Multi-scale RBF with polynomial weighting
            for i in range(1, min(6, self.dim + 1)):
                for j in range(i, min(i+3, self.dim + 1)):
                    if j < self.dim:
                        # Radial basis function with dynamic bandwidth
                        sigma = 0.5 + 0.5 * np.sin(r / (i + 1))
                        rbf_val = np.exp(-np.sum((x[i:j] - x[i:j])**2) / (2 * sigma**2))
                        
                        # Polynomial chaos weighting
                        poly_weight = 0.0
                        for k in range(len(self.poly_coeffs[i])):
                            poly_weight += self.poly_coeffs[i][k] * (r ** k)
                        
                        result += rbf_val * poly_weight * np.cos(i * r) * np.sin(j * r)
        
        # Dynamic dimensionality scaling with polynomial modulation
        for i in range(self.dim):
            xi = x[i]
            # Adaptive polynomial with dynamic exponent
            exp_factor = 2 + 0.5 * np.sin(xi / 3.0)
            poly_term = xi**exp_factor - 2*xi**(exp_factor-1) + xi**(exp_factor-2) - xi**(exp_factor-3)
            
            # Dynamic scaling based on position
            scale = 1.0 + 0.3 * np.cos(xi / 2.0) * np.sin(xi / 4.0)
            result += scale * poly_term * np.exp(-abs(xi) / 3.0)
        
        # Fractal-like angular coupling with multi-scale interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                
                # Angular distance with fractal modulation
                angle_diff = np.arctan2(xj, xi)
                fractal_mod = 1.0 + 0.4 * np.sin(10 * angle_diff) * np.cos(8 * angle_diff)
                
                # Multi-scale coupling with radial influence
                coupling = np.exp(-((xi - xj)**2 + (xi + xj)**2)/5.0) * fractal_mod
                result += coupling * np.sin(3 * (xi + xj)) * np.cos(4 * (xi - xj))
        
        # Polynomial chaos expansion with radial modulation
        for i in range(1, 7):
            poly_exp = np.sum([self.poly_coeffs[i][j] * (r ** j) for j in range(len(self.poly_coeffs[i]))])
            result += poly_exp * np.sin(i * r) * np.cos(i * r) * np.exp(-r / (i + 1))
        
        # Multi-scale radial polynomial with angular harmonic components
        for i in range(1, min(8, self.dim + 1)):
            freq = i * (1.2 + 0.3 * np.sin(r / 4.0))
            amp = 1.0 + 0.5 * np.cos(i * r / 3.0)
            angular_component = np.sin(freq * r) * np.cos(freq * r)
            
            # Add fractal-like behavior to amplitude
            fractal_amp = 1.0 + 0.2 * np.sin(7 * r) * np.cos(5 * r)
            result += fractal_amp * amp * angular_component * np.exp(-r / (i + 2))
        
        # Cross-dimensional coupling with polynomial chaos weighting
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                if j < self.dim:
                    xi = x[i]
                    xj = x[j]
                    
                    # Polynomial chaos weighted coupling
                    poly_weight = 0.0
                    order = min(5, i + j)
                    for k in range(len(self.poly_coeffs[order])):
                        poly_weight += self.poly_coeffs[order][k] * ((xi + xj) ** k)
                    
                    coupling = np.exp(-abs(xi - xj) / 4.0) * np.sin(xi + xj) * np.cos(xi - xj)
                    result += poly_weight * coupling
        
        # Adaptive radial polynomial with dynamic scaling
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # High-order polynomial with adaptive exponent
            exp_val = 6 + 0.8 * np.sin(xi / 2.0)
            poly_sum += xi**exp_val - 3*xi**(exp_val-1) + 3*xi**(exp_val-2) - xi**(exp_val-3)
        result += 0.7 * poly_sum * np.exp(-r / 5.0)
        
        # Angular harmonic polynomial with fractal modulation
        angular_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal-like angular component
            fractal_angle = 1.0 + 0.3 * np.sin(15 * xi) * np.cos(12 * xi)
            angular_sum += fractal_angle * np.sin(xi / 2.0) * np.cos(xi / 3.0)
        result += 0.6 * angular_sum * np.exp(-r / 4.0)
        
        # Multi-scale polynomial chaos with radial basis influence
        for i in range(1, min(10, self.dim + 1)):
            poly_val = np.sum([self.poly_coeffs[i][j] * (r ** j) for j in range(len(self.poly_coeffs[i]))])
            result += poly_val * np.sin(i * r) * np.cos(i * r) * np.exp(-r / (i + 3))
        
        return result