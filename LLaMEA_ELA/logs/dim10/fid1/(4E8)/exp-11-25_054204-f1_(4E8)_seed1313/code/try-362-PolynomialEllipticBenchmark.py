import numpy as np

class PolynomialEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute elliptic parameters for radial scaling
        self.elliptic_params = 1.0 + 0.5 * np.cos(np.arange(dim) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with weighted harmonics
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x[i]**4 + 0.5 * x[i]**3 + 0.2 * x[i]**2) * np.sin(1.5 * x[i])
        
        # Elliptic radial interaction with adaptive scaling
        elliptic_radial = 0.0
        for i in range(self.dim):
            r = np.sqrt(x[i]**2 + self.elliptic_params[i]**2)
            elliptic_radial += np.exp(-0.1 * r) * np.cos(3.0 * x[i] / (1.0 + 0.1 * i))
        
        # Quaternion-inspired coupling with imaginary components
        quat_coupling = 0.0
        for i in range(self.dim - 1):
            # Simulate quaternion-like interaction using cross products of trigonometric terms
            quat_coupling += np.sin(x[i]) * np.cos(x[i+1]) + np.cos(x[i]) * np.sin(x[i+1])
        
        # Cross-dimensional polynomial with exponential weights
        cross_poly = 0.0
        for i in range(self.dim - 2):
            weight = np.exp(-i / (self.dim + 1))
            cross_poly += (x[i] * x[i+1] + x[i+1] * x[i+2]) * weight
        
        # Chaotic modulation with tent map
        chaotic_mod = 0.0
        for i in range(self.dim):
            # Tent map: f(x) = mu * x if x < 0.5 else mu * (1 - x)
            mu = 3.8
            tent_val = mu * np.abs(x[i] - 0.5) if x[i] < 0.5 else mu * (1.0 - np.abs(x[i] - 0.5))
            chaotic_mod += np.sin(tent_val * x[i]) * np.cos(2.0 * x[i])
        
        # Sine-cosine coupled with dynamic phase shifts
        phase_coupling = 0.0
        for i in range(self.dim):
            phase_shift = np.sin(i * np.pi / self.dim)
            phase_coupling += np.sin(x[i] + phase_shift) * np.cos(2.0 * x[i] + phase_shift)
        
        # Fractal-like interaction with recursive polynomial terms
        fractal_interaction = 0.0
        for i in range(self.dim - 3):
            fractal_interaction += (x[i]**2 + x[i+1]**2 + x[i+2]**2) * np.sin(x[i] * x[i+1] * x[i+2])
        
        # Adaptive dimensionality scaling factor
        scale = 1.0 + 0.4 * np.log(self.dim + 1)
        
        # Combined function with refined weights
        return scale * (0.9 * poly_chaos + 0.8 * elliptic_radial + 0.7 * quat_coupling + 
                       0.6 * cross_poly + 0.5 * chaotic_mod + 0.4 * phase_coupling + 
                       0.3 * fractal_interaction)