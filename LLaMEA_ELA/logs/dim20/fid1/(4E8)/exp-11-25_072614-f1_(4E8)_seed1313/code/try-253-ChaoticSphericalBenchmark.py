import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic tent map parameters
        self.tent_params = np.array([0.5 + 0.5 * np.sin(0.3 * np.pi * i) for i in range(dim)])
        # Precompute spherical harmonic degrees
        self.harmonic_degrees = np.array([2 + 2 * np.cos(0.4 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map dynamics term
        tent_term = 0.0
        for i in range(self.dim):
            param = self.tent_params[i]
            tent_val = 1.0 - 2.0 * abs(0.5 - (x[i] + 2.5) / 5.0)
            tent_term += param * tent_val * np.exp(-0.1 * x[i]**2)
        tent_term /= self.dim
        
        # Spherical harmonic decomposition term
        harmonic_term = 0.0
        for i in range(self.dim):
            degree = int(max(1, self.harmonic_degrees[i]))
            # Spherical harmonic Y_l^m with l=degree, m=0 (zonal harmonics)
            theta = np.arccos(x[i] / (1e-8 + np.sqrt(np.sum(x**2))))
            harmonic_val = np.cos(degree * theta)
            harmonic_term += harmonic_val * np.exp(-0.05 * x[i]**2)
        harmonic_term /= self.dim
        
        # Adaptive penalty term with chaotic modulation
        penalty_term = 0.0
        for i in range(self.dim):
            # Chaotic modulation of penalty strength
            modulator = 1.0 + 0.3 * np.sin(0.7 * np.pi * i + 0.2 * np.sum(x))
            penalty_term += modulator * (x[i]**2 - 25.0)**2 * np.exp(-0.02 * x[i]**2)
        penalty_term /= self.dim
        
        # Cross-dimensional coupling with chaotic interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction strength
                interaction = 0.8 + 0.2 * np.sin(0.5 * np.pi * (i + j) + 0.3 * np.sum(x))
                cross_term += interaction * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale chaotic oscillation
        oscillation_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.6 * np.pi * i)
            oscillation_term += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.08 * x[i]**2)
        oscillation_term /= self.dim
        
        # Fractal-like basin structure with chaotic scaling
        basin_term = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.cos(0.5 * np.pi * i)
            basin_term += (scale_factor * x[i]**3 - 3.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        basin_term /= self.dim
        
        # Combined weighted sum
        weights = np.abs(np.array([0.2, 0.15, 0.25, 0.15, 0.15, 0.1])) / np.sum(np.abs(np.array([0.2, 0.15, 0.25, 0.15, 0.15, 0.1])))
        
        total = (weights[0] * tent_term + 
                 weights[1] * harmonic_term + 
                 weights[2] * penalty_term + 
                 weights[3] * cross_term + 
                 weights[4] * oscillation_term + 
                 weights[5] * basin_term)
        
        return total