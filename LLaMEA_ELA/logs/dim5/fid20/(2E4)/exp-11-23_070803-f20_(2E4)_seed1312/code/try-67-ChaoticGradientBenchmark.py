import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Chaotic tent map component with modified parameter and added sine modulation
        chaotic_term = 0
        a = 1.7  # Slightly increased chaos parameter
        for i in range(self.dim):
            xi = x_norm[i]
            if xi < 0.5:
                tent_val = a * xi
            else:
                tent_val = a * (1 - xi)
            chaotic_term += tent_val * np.sin(2 * np.pi * xi) * (1 + 0.4 * np.cos(5 * xi)) * np.exp(-0.5 * xi**2)
        
        # Spherical harmonic expansion with modified frequencies and weights
        sph_harm_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended coupling
                r = np.sqrt(x_norm[i]**2 + x_norm[j]**2)
                theta = np.arctan2(x_norm[j], x_norm[i])
                sph_harm_term += (r**3) * np.sin(4 * theta) * np.cos(5 * theta) * \
                                (1 + 0.3 * np.sin(8 * r) * np.cos(6 * r)) * 0.7  # Reduced weight
        
        # Asymmetric gradient flow with stronger directional bias
        grad_term = 0
        for i in range(self.dim):
            # Stronger directional bias based on dimension index
            bias = 1.0 + 0.8 * np.sin(i * np.pi / self.dim)  # Increased bias strength
            grad_term += (x_norm[i]**3) * (1 + 0.5 * np.cos(3 * x_norm[i])) * bias
            
        # Cross-dimensional coupling with different decay rate
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling = np.exp(-2*dist) * (1 + 0.4 * np.sin(3 * dist))  # Faster decay
                cross_term += coupling * x_norm[i]**2 * x_norm[j]**2
                
        # Non-linear transformation with different polynomial degrees
        poly_term = 0
        for i in range(self.dim):
            if x_norm[i] >= 0:
                poly_val = x_norm[i]**5 + 0.6 * x_norm[i]**4 - 0.4 * x_norm[i]**3  # Higher degree terms
            else:
                poly_val = x_norm[i]**6 - 0.5 * x_norm[i]**5 + 0.3 * x_norm[i]**4
            poly_term += poly_val * (1 + 0.3 * np.sin(7 * x_norm[i]))
        
        # Combine all components with slightly adjusted weights
        result = 2.0 * chaotic_term + 1.3 * sph_harm_term + 1.4 * grad_term + \
                0.9 * cross_term + 1.1 * poly_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise