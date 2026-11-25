import numpy as np

class PolynomialChaoticRBF:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial term with mixed degrees
        base_term = np.sum(x**4) + 0.5 * np.sum(x**2)
        
        # Radial basis function component with chaotic center placement
        rbf_sum = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * np.pi / (self.dim + 1)) * np.cos(i * np.pi / (self.dim + 2))
            width = 0.5 + 0.3 * np.sin(i * np.pi / (self.dim + 3))
            rbf_sum += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Cross-dimensional polynomial coupling with chaotic coefficients
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.1 * np.sin(i * j * np.pi / (self.dim + 1))
                coupling_term += coeff * x[i]**3 * x[j]**2
        
        # Chaotic sine modulation with varying phases and amplitudes
        chaotic_mod = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.sin(i * np.pi / (self.dim + 1))
            amp = 0.8 + 0.2 * np.cos(i * np.pi / (self.dim + 2))
            chaotic_mod += amp * np.sin(x[i] + phase) * np.cos(x[i] * 0.5 + phase)
        
        # Exponentially decaying noise component
        noise = 0.0
        for i in range(self.dim):
            noise += np.exp(-0.1 * x[i]**2) * np.sin(3.0 * x[i])
        
        # Dimensionality scaling and chaotic weighting
        dim_scaling = 1.0 + 0.1 * np.sin(self.dim * np.pi / 4.0)
        
        return dim_scaling * (base_term + 0.3 * rbf_sum + 0.2 * coupling_term + 
                             0.25 * chaotic_mod + 0.15 * noise)