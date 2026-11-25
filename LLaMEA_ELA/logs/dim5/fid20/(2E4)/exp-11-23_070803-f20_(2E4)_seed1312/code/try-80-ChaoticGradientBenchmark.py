import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Enhanced chaotic tent map with multiple sine modulations and higher chaos parameter
        chaotic_term = 0
        a = 2.1  # Increased chaos parameter for more complex dynamics
        for i in range(self.dim):
            xi = x_norm[i]
            if xi < 0.5:
                tent_val = a * xi
            else:
                tent_val = a * (1 - xi)
            chaotic_term += tent_val * np.sin(2 * np.pi * xi) * np.cos(3 * np.pi * xi) * \
                           np.sin(7 * xi) * np.exp(-0.3 * xi**2) * (1 + 0.5 * np.sin(11 * xi))
        
        # Extended spherical harmonic expansion with higher frequency components and more terms
        sph_harm_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Increased coupling range
                r = np.sqrt(x_norm[i]**2 + x_norm[j]**2)
                theta = np.arctan2(x_norm[j], x_norm[i])
                sph_harm_term += (r**4) * np.sin(6 * theta) * np.cos(7 * theta) * \
                                (1 + 0.5 * np.sin(9 * r) * np.cos(8 * r)) * \
                                (1 + 0.3 * np.cos(12 * r)) * 0.8  # Increased weight
        
        # Stronger asymmetric gradient flow with exponential bias and additional nonlinearities
        grad_term = 0
        for i in range(self.dim):
            # Exponential directional bias with increased strength
            bias = 1.0 + 1.2 * np.exp(-i * 0.3) * np.sin(i * np.pi / self.dim)
            grad_term += (x_norm[i]**4) * (1 + 0.7 * np.cos(4 * x_norm[i])) * \
                        np.sin(5 * x_norm[i]) * bias
            
        # Enhanced cross-dimensional coupling with multiple decay rates and oscillatory components
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling = np.exp(-3*dist) * (1 + 0.6 * np.sin(5 * dist)) * \
                          (1 + 0.4 * np.cos(7 * dist))  # Multiple oscillatory components
                cross_term += coupling * x_norm[i]**2 * x_norm[j]**3
                
        # Higher-order polynomial transformation with mixed odd/even powers and additional trigonometric terms
        poly_term = 0
        for i in range(self.dim):
            if x_norm[i] >= 0:
                poly_val = x_norm[i]**7 + 0.8 * x_norm[i]**6 - 0.5 * x_norm[i]**5 + \
                          0.3 * x_norm[i]**4  # Higher degree terms
            else:
                poly_val = x_norm[i]**8 - 0.6 * x_norm[i]**7 + 0.4 * x_norm[i]**6 - \
                          0.2 * x_norm[i]**5
            poly_term += poly_val * (1 + 0.4 * np.sin(9 * x_norm[i])) * \
                        np.cos(4 * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2)
        
        # Additional high-frequency oscillatory component for increased complexity
        freq_term = 0
        for i in range(self.dim):
            freq_term += (x_norm[i] * np.sin(15 * x_norm[i]) * np.cos(13 * x_norm[i])) * \
                        (1 + 0.3 * np.sin(23 * x_norm[i]))
        
        # Combine all components with adjusted weights
        result = 2.5 * chaotic_term + 1.8 * sph_harm_term + 1.7 * grad_term + \
                1.2 * cross_term + 1.4 * poly_term + 0.8 * freq_term
        
        # Add significant random noise for non-determinism
        noise = np.random.normal(0, 0.01)
        
        return result + noise