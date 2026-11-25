import numpy as np

class RadialSkewSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Radial basis function centers scattered in the domain
        self.centers = -5.0 + 10.0 * np.random.rand(dim, dim)
        # Radial basis function widths
        self.widths = 0.5 + 2.0 * np.random.rand(dim)
        # Skewness parameters for asymmetric basins
        self.skew_params = -1.0 + 2.0 * np.random.rand(dim)
        # Saddle point locations and strengths
        self.saddle_centers = -5.0 + 10.0 * np.random.rand(dim, dim)
        self.saddle_strengths = 0.5 + 3.0 * np.random.rand(dim)
        # Asymmetry coefficients for each dimension
        self.asymmetry_coeffs = 0.5 + 2.0 * np.random.rand(dim)
        # Polynomial modulation terms
        self.poly_exponents = 1.0 + 3.0 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.centers[i])**2)
            rbf_sum += np.exp(-self.widths[i] * dist)
        
        # Skewed basin component
        skew_sum = 0.0
        for i in range(self.dim):
            skewed_x = x_norm[i] + self.skew_params[i] * (x_norm[i]**3)
            skew_sum += np.abs(skewed_x)**(self.poly_exponents[i])
        
        # Saddle point interactions
        saddle_sum = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.saddle_centers[i])**2)
            saddle_sum -= self.saddle_strengths[i] * np.exp(-dist / (2.0 * (1.0 + x_norm[i]**2)))
        
        # Asymmetric modulation
        asym_sum = 0.0
        for i in range(self.dim):
            asym_sum += self.asymmetry_coeffs[i] * np.sin(x_norm[i]) * np.cos(2 * x_norm[i])
        
        # Combine components with varying weights
        result = 0.3 * rbf_sum + 0.25 * skew_sum + 0.25 * saddle_sum + 0.2 * asym_sum
        
        # Add a global conditioning term
        condition_term = np.sum((x_norm**2) * (1.0 + 0.1 * np.abs(x_norm)))
        
        # Add penalty for large values
        penalty = 0.1 * np.sum(np.abs(x_norm)**4)
        
        return result + condition_term + penalty