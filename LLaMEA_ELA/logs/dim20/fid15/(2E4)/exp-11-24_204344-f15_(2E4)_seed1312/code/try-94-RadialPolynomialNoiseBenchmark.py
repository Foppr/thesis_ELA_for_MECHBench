import numpy as np

class RadialPolynomialNoiseBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis parameters
        self.center = np.random.uniform(-2.0, 2.0, dim)
        self.scale = np.random.uniform(0.5, 2.0, dim)
        self.noise_level = 0.1 + 0.2 * np.random.rand()
        
    def f(self, x):
        x = np.array(x)
        
        # Radial polynomial term with varying exponents
        radial_poly = 0.0
        for i in range(self.dim):
            dist_from_center = (x[i] - self.center[i])**2
            exponent = 2 + 2 * np.sin(i * 0.5)
            radial_poly += self.scale[i] * dist_from_center**(exponent/2)
            
        # Multi-dimensional polynomial interaction
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
                
        # Radial harmonic modulation
        radial_harmonic = 0.0
        total_dist = np.sum((x - self.center)**2)
        if total_dist > 1e-8:
            radial_harmonic = np.sin(np.sqrt(total_dist)) * np.cos(np.sqrt(total_dist))
            
        # Cross-dimensional coupling with exponential weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-abs(x[i] - x[j]) / (self.dim + 1))
                cross_coupling += weight * (x[i]**3 + x[j]**3)
                
        # Dynamic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += self.noise_level * np.sin(x[i] * (i + 1) * 2 * np.pi)
            
        # Global minimum at origin with adaptive scaling
        global_min = np.sum(x**2) * 0.1
        
        return radial_poly + 0.5 * poly_interaction + 0.3 * radial_harmonic + \
               0.4 * cross_coupling + noise + global_min