import numpy as np

class PolynomialRBFChaosLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute harmonic coefficients for stability
        self.harmonic_coeffs = np.array([np.sin(i * np.pi / (dim + 1)) * np.cos(i * np.pi / (dim + 2)) 
                                        for i in range(dim)])
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion with adaptive weights
        poly_sum = 0.0
        for i in range(self.dim):
            # Use Chebyshev polynomials for better conditioning
            T_n = np.cos(i * np.arccos(np.clip(x_norm[i], -1, 1)))
            weight = 1.0 / (1.0 + 0.1 * i**1.5)
            poly_sum += weight * T_n * np.exp(-0.5 * x_norm[i]**2)
        
        # Radial basis function with multi-scale kernel widths
        rbf_sum = 0.0
        for i in range(self.dim):
            # Use Gaussian RBFs with dimensionally adaptive widths
            width = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            rbf_sum += np.exp(-0.5 * (x_norm[i] / width)**2) * np.cos(2 * np.pi * x_norm[i])
        
        # Spectral decomposition with frequency coupling
        spec_sum = 0.0
        for i in range(self.dim):
            freq = 1.0 + 3.0 * np.abs(np.sin(i * np.pi / (self.dim + 3)))
            spec_sum += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Novel harmonic coupling with quaternion-inspired phase modulation
        quat_sum = 0.0
        for i in range(self.dim):
            # Quaternion-like coupling using imaginary unit components
            phase1 = np.sin(x_norm[i] + i * 0.3)
            phase2 = np.cos(x_norm[i] + i * 0.4)
            quat_sum += (phase1**2 + phase2**2) * np.exp(-0.3 * x_norm[i]**2)
        
        # Fractal-like self-similarity with recursive scaling
        fractal_sum = 0.0
        for i in range(self.dim):
            scale = 2.0**(i % 4)
            fractal_sum += np.sin(scale * x_norm[i]) * np.cos(scale * x_norm[i] / 2) * np.exp(-0.1 * x_norm[i]**2)
        
        # Enhanced cross-dimensional coupling with non-linear interaction
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Non-linear coupling with exponential decay and enhanced interaction
                coupling = np.exp(-0.3 * (x_norm[i] - x_norm[j])**2) * np.sin(2 * (x_norm[i] + x_norm[j]))
                cross_sum += coupling * (1.0 + 0.2 * np.abs(x_norm[i]) * np.abs(x_norm[j]) + 0.05 * x_norm[i]**2 * x_norm[j]**2)
        
        # Modified basin structures with asymmetric polynomial potentials
        basin_sum = 0.0
        for i in range(self.dim):
            if x_norm[i] < 0:
                basin_sum += (x_norm[i]**3 + 0.5 * x_norm[i]**2 + 0.1 * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2)
            else:
                basin_sum += (x_norm[i]**4 - 0.4 * x_norm[i]**2 + 0.08 * x_norm[i]) * np.exp(-0.25 * x_norm[i]**2)
        
        # Combine all components with adaptive weighting
        result = 0.25 * poly_sum + 0.2 * rbf_sum + 0.15 * spec_sum + 0.15 * quat_sum + 0.1 * fractal_sum + 0.1 * cross_sum + 0.05 * basin_sum
        
        # Adaptive conditioning with dimension-dependent factors
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 2)
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.2 * np.abs(x_norm[i]) + 0.05 * x_norm[i]**2 + 0.03 * np.sin(x_norm[i]))
        
        # Final transformation with fractal scaling
        return result * condition_factor * (1.0 + 0.2 * np.sum(np.abs(x_norm)**3) + 0.05 * np.sum(x_norm**4))