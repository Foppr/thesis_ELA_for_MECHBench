import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients for different degrees
        self.poly_coeffs = np.random.randn(5, dim)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component
        poly_term = 0.0
        for i in range(5):
            poly_val = np.prod([np.cos((i+1) * np.pi * x_norm[j] / 2) 
                              for j in range(self.dim)])
            poly_term += self.poly_coeffs[i, 0] * poly_val
            
        # Radial basis function component
        rbf_term = 0.0
        for i in range(10):
            dist = np.sum((x_norm - self.rbf_centers[i])**2)
            rbf_term += self.rbf_widths[i] * np.exp(-dist / (2 * 0.5**2))
            
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            freq = 10 + 30 * np.random.rand()
            amp = 1.0 + 2.0 * np.random.rand()
            sin_term += amp * np.sin(freq * x_norm[i])
            
        # Coupling between dimensions with chaotic modulation
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += np.sin(x_norm[i] * x_norm[j]) * \
                               np.cos(2 * (x_norm[i] + x_norm[j]))
                
        # Fractional power and logarithmic scaling for multi-scale behavior
        scale_term = 0.0
        for i in range(self.dim):
            scale_term += (np.abs(x_norm[i])**1.5) * np.log(1 + np.abs(x_norm[i]))
            
        # Add noise term to increase ruggedness
        noise = 0.1 * np.random.rand()
        
        return poly_term + rbf_term + sin_term + coupling_term + scale_term + noise