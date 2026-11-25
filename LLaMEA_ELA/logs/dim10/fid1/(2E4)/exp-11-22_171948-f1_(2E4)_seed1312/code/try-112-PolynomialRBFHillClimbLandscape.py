import numpy as np

class PolynomialRBFHillClimbLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients for different orders
        self.poly_coeffs = np.random.randn(5, dim) * 0.5
        # Precompute radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (8, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 8)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component
        poly_result = 0.0
        for i in range(5):
            for j in range(self.dim):
                poly_result += self.poly_coeffs[i, j] * (x[j] ** (i + 1))
        
        # Radial basis function component with asymmetric weighting
        rbf_result = 0.0
        for i in range(8):
            distance = np.sum((x - self.rbf_centers[i]) ** 2)
            rbf_value = np.exp(-self.rbf_widths[i] * distance)
            # Asymmetric weighting based on position relative to center
            asym_weight = 1.0 + 0.3 * np.tanh(x[np.argmax(np.abs(x))] - self.rbf_centers[i, np.argmax(np.abs(x))])
            rbf_result += rbf_value * asym_weight
        
        # Hill-climbing structure with varying ascent rates
        hill_result = 0.0
        for i in range(self.dim):
            # Asymmetric hill structure with different growth rates
            if x[i] >= 0:
                hill_result += 0.4 * (x[i] ** 3) * np.exp(-0.1 * x[i])
            else:
                hill_result += 0.6 * (x[i] ** 2) * np.exp(-0.05 * np.abs(x[i]))
        
        # Cross-term interactions with noise sensitivity
        cross_result = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric coupling with different weights based on variable values
                weight_i = 1.0 + 0.2 * np.sin(x[i])
                weight_j = 1.0 + 0.2 * np.cos(x[j])
                cross_result += weight_i * weight_j * (x[i] - x[j]) ** 4
        
        # Global conditioning based on dimensionality and position
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1) + 0.1 * np.sum(np.abs(x))
        
        # Noise sensitivity component
        noise = np.random.normal(0, 0.02, self.dim)
        noise_result = 0.05 * np.sum(noise ** 2)
        
        # Combine all components with different weights
        result = 0.3 * poly_result**2 + 0.4 * rbf_result + 0.2 * hill_result + 0.1 * cross_result + noise_result
        
        # Normalize and apply final conditioning
        result *= condition_factor / self.dim
        
        return result