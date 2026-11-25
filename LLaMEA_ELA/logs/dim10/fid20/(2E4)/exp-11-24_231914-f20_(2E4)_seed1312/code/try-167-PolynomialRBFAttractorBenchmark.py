import numpy as np

class PolynomialRBFAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.normal(0, 1, size=(dim, 5))
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, size=(10, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=10)
        # Attractor dynamics parameters
        self.attractor_strength = np.random.uniform(0.5, 2.0, size=dim)
        self.attractor_positions = np.random.uniform(-5.0, 5.0, size=(5, dim))
        # Noise injection parameters
        self.noise_level = 0.1
        self.noise_decay = np.random.uniform(0.8, 0.99, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component
        poly_expansion = 0.0
        for i in range(self.dim):
            for j in range(5):
                poly_expansion += self.poly_coeffs[i, j] * (x[i] ** j)
                
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(10):
            distance = np.sum((x - self.rbf_centers[i]) ** 2)
            rbf_sum += np.exp(-distance / (2 * self.rbf_widths[i] ** 2))
            
        # Attractor dynamics component
        attractor_force = 0.0
        for i in range(5):
            distance = np.sum((x - self.attractor_positions[i]) ** 2)
            force_magnitude = self.attractor_strength[i] / (distance + 1e-8)
            attractor_force += force_magnitude
            
        # Gradient-based landscape with adaptive noise
        gradient_term = 0.0
        for i in range(self.dim):
            # Compute gradient of polynomial part
            grad = 0.0
            for j in range(1, 5):
                grad += j * self.poly_coeffs[i, j] * (x[i] ** (j-1))
            gradient_term += grad ** 2
            
        # Noise injection with decay
        noise = np.sum(np.random.normal(0, self.noise_level, size=self.dim) * 
                      self.noise_decay)
        
        # Combine all components with appropriate weights
        return (0.8 * poly_expansion + 
                1.2 * rbf_sum + 
                0.9 * attractor_force + 
                1.1 * gradient_term + 
                0.5 * noise)