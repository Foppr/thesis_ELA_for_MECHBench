import numpy as np

class PolynomialGaussianCoupledLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize landscape parameters
        self.poly_degree = 3 + np.random.randint(0, 3)
        self.gaussian_width = 0.5 + 2.0 * np.random.rand()
        self.coupling_strength = 0.5 + 2.5 * np.random.rand()
        self.conditioning_range = 0.1 + 0.9 * np.random.rand()
        self.valley_depth = 1.0 + 3.0 * np.random.rand()
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial conditioning term
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i] ** self.poly_degree) * (1.0 + self.conditioning_range * np.sin(0.5 * x[i]))
        
        # Gaussian radial basis function component
        gaussian_term = 0.0
        for i in range(self.dim):
            center = -2.0 + 4.0 * np.random.rand()
            gaussian_term += np.exp(-0.5 * ((x[i] - center) / self.gaussian_width)**2)
        
        # Sine-cosine coupling term
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling_term += np.sin(self.coupling_strength * x[i]) * np.cos(self.coupling_strength * x[j])
        
        # Valley interaction term
        valley_term = 0.0
        for i in range(self.dim):
            valley_term += self.valley_depth * np.sin(0.3 * x[i]) * np.cos(0.7 * x[i])
        
        # Combine all components
        result = poly_term + gaussian_term + coupling_term + valley_term
        
        return result