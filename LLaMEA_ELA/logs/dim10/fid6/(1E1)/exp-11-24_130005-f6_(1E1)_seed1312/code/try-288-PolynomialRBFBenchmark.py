import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random coefficients for polynomial chaos expansion
        self.poly_coeffs = np.random.randn(dim, 5)
        # Generate random centers and widths for RBF network
        self.rbf_centers = np.random.uniform(-1.0, 1.0, (dim, 3))
        self.rbf_widths = np.random.uniform(0.1, 0.5, (dim, 3))
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial chaos expansion component
        poly_component = 0.0
        for i in range(self.dim):
            for j in range(5):
                # Use Hermite polynomials (first 5 orders)
                hermite_poly = self._hermite_polynomial(x_scaled[i], j)
                poly_component += self.poly_coeffs[i, j] * hermite_poly
        
        # Radial basis function network component
        rbf_component = 0.0
        for i in range(self.dim):
            for j in range(3):
                dist = np.linalg.norm(x_scaled[i] - self.rbf_centers[i, j])
                rbf_value = np.exp(-0.5 * (dist / self.rbf_widths[i, j])**2)
                rbf_component += rbf_value
        
        # Mixed smooth-discontinuous regions with sine modulation
        mixed_component = 0.0
        for i in range(self.dim):
            # Create discontinuous regions with smooth transitions
            discontinuity = np.sin(10 * x_scaled[i]) * np.cos(5 * x_scaled[i])
            smooth_term = np.sin(x_scaled[i]**2) + np.cos(x_scaled[i])
            mixed_component += (discontinuity + smooth_term) * np.exp(-abs(x_scaled[i]))
        
        # Multi-scale interaction terms with varying coupling strengths
        interaction_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Varying coupling strength based on dimension index
                coupling_strength = 1.0 / (1.0 + 0.1 * (i + j))
                interaction_term = np.sin(x_scaled[i] * x_scaled[j]) * \
                                  np.cos(x_scaled[i] / (1.0 + abs(x_scaled[j])))
                interaction_component += coupling_strength * interaction_term
        
        # Combine all components with adaptive weights
        total = 0.8 * poly_component + 1.2 * rbf_component + 0.6 * mixed_component + 0.4 * interaction_component
        
        # Add a global scaling factor and offset to ensure good conditioning
        return total + 0.1 * np.sum(x_scaled**4)
    
    def _hermite_polynomial(self, x, n):
        """Compute nth order Hermite polynomial"""
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        else:
            Hn_minus_1 = x
            Hn_minus_2 = 1.0
            for i in range(2, n + 1):
                Hn = x * Hn_minus_1 - (i - 1) * Hn_minus_2
                Hn_minus_2 = Hn_minus_1
                Hn_minus_1 = Hn
            return Hn_minus_1