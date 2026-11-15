import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Tent map chaotic component with varying parameter
        chaotic = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                # Tent map with parameter 2.5
                tent1 = 2.5 * np.abs(x_norm[i] - 0.5)
                tent2 = 2.5 * np.abs(x_norm[i+1] - 0.5)
                chaotic += np.sin(tent1 * tent2) * np.cos(tent1 + tent2)
        
        # Fractional polynomial interactions with varying exponents
        poly_frac = 0.0
        for i in range(self.dim):
            poly_frac += (x_norm[i]**1.5 + 0.5 * x_norm[i]**2.5 + 0.3 * x_norm[i]**3.5)
        
        # Radial basis functions with dynamic centers and widths
        rbf = 0.0
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        widths = np.linspace(1.0, 3.0, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < self.dim:
                rbf += np.exp(-widths[i] * (x_norm[i] - centers[i])**2)
        
        # Multi-scale sine-cosine polynomial interactions
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += (np.sin(10 * x_norm[i]**2) * np.cos(15 * x_norm[i]**3) + 
                           0.7 * np.sin(20 * x_norm[i]) * np.cos(25 * x_norm[i]**2))
        
        # Cross-dimensional coupling with hyperbolic functions
        coupling = 0.0
        if self.dim > 2:
            for i in range(self.dim - 2):
                coupling += np.tanh(x_norm[i] * x_norm[i+1]) * np.cosh(x_norm[i+2])
        
        # Asymmetric exponential with polynomial correction
        asym_exp = np.sum(np.exp(-x_norm**2) * (1 + 0.3 * x_norm**3))
        
        # Novel fractional chaotic interaction term
        frac_chaotic = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                frac_chaotic += (np.sin(12 * x_norm[i]**1.7) * np.cos(18 * x_norm[i+1]**1.3) + 
                               0.4 * np.sin(24 * x_norm[i] * x_norm[i+1]**1.5))
        
        # Combine all components
        result = (0.2 * chaotic + 
                 0.25 * poly_frac + 
                 0.15 * rbf + 
                 0.2 * multi_scale + 
                 0.1 * coupling + 
                 0.1 * asym_exp + 
                 0.1 * frac_chaotic)
        
        # Add small noise for non-triviality
        noise = 0.001 * np.random.random()
        
        return result + noise