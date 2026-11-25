import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial term with mixed degrees and interaction
        poly_term = np.sum(0.5 * x_scaled**6 + 0.3 * x_scaled**4 + 0.2 * x_scaled**2)
        
        # Radial basis function component with multiple centers
        rbfs = []
        centers = np.linspace(-1, 1, min(5, self.dim))
        for c in centers:
            rbfs.append(np.exp(-5 * np.sum((x_scaled - c)**2)))
        rbf_term = np.sum(rbfs)
        
        # Trigonometric component with varying frequencies and phases
        trig_term = np.sum(np.sin(3 * x_scaled) + 0.5 * np.cos(7 * x_scaled) + 0.3 * np.sin(11 * x_scaled))
        
        # Coupled sine waves creating interference patterns
        coupling_term = np.sum(np.sin(x_scaled[:-1] + x_scaled[1:]) * np.cos(x_scaled[:-1] - x_scaled[1:]))
        
        # Add noise-like chaotic modulation
        chaotic_mod = np.sum(np.sin(2 * np.pi * (x_scaled**3 + 0.1 * x_scaled)) * np.cos(1.5 * np.pi * x_scaled))
        
        # Combine all terms with adaptive weights based on dimensionality
        weight_poly = 0.4 + 0.1 * np.log(self.dim)
        weight_rbf = 0.3 + 0.05 * np.log(self.dim)
        weight_trig = 0.2 + 0.02 * np.log(self.dim)
        weight_coupling = 0.05 + 0.01 * np.log(self.dim)
        weight_chaotic = 0.05
        
        result = (weight_poly * poly_term + 
                 weight_rbf * rbf_term + 
                 weight_trig * trig_term + 
                 weight_coupling * coupling_term + 
                 weight_chaotic * chaotic_mod)
        
        # Add global offset to ensure function value is not too close to zero
        return result + 2.0