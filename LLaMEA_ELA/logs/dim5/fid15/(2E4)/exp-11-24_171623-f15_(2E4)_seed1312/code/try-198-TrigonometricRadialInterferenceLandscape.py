import numpy as np

class TrigonometricRadialInterferenceLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute harmonic coefficients for stability
        self.harmonic_coeffs = np.array([np.sin(i * np.pi / (dim + 1)) * np.cos(i * np.pi / (dim + 2)) 
                                        for i in range(dim)])
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced trigonometric oscillations with adaptive frequencies
        trig_sum = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * np.pi / (self.dim + 1))
            trig_sum += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2)
        
        # Radial symmetry with modified Bessel functions
        radial_sum = 0.0
        r = np.sqrt(np.sum(x_norm**2))
        for i in range(self.dim):
            # Use modified Bessel function-like terms for radial structure
            radial_sum += np.exp(-0.5 * (x_norm[i] / (1.0 + 0.1 * r))**2) * np.cos(3 * x_norm[i])
        
        # Cross-dimensional interference with phase coupling
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Enhanced interference with cosine coupling and exponential decay
                coupling = np.exp(-0.2 * (x_norm[i] - x_norm[j])**2) * np.cos(4 * (x_norm[i] + x_norm[j]))
                cross_sum += coupling * (1.0 + 0.3 * np.abs(x_norm[i]) * np.abs(x_norm[j]))
        
        # Modified basin structures with asymmetric polynomial potentials
        basin_sum = 0.0
        for i in range(self.dim):
            if x_norm[i] < 0:
                basin_sum += (x_norm[i]**3 + 0.4 * x_norm[i]**2 + 0.15 * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2)
            else:
                basin_sum += (x_norm[i]**4 - 0.3 * x_norm[i]**2 + 0.05 * x_norm[i]) * np.exp(-0.25 * x_norm[i]**2)
        
        # Fractal-like self-similarity with recursive scaling
        fractal_sum = 0.0
        for i in range(self.dim):
            scale = 1.5**(i % 3)
            fractal_sum += np.sin(scale * x_norm[i]) * np.cos(scale * x_norm[i] / 2) * np.exp(-0.1 * x_norm[i]**2)
        
        # Spectral decomposition with frequency coupling
        spec_sum = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.abs(np.sin(i * np.pi / (self.dim + 2)))
            spec_sum += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Novel harmonic coupling with quaternion-inspired phase modulation
        quat_sum = 0.0
        for i in range(self.dim):
            # Quaternion-like coupling using imaginary unit components
            phase1 = np.sin(x_norm[i] + i * 0.25)
            phase2 = np.cos(x_norm[i] + i * 0.35)
            quat_sum += (phase1**2 + phase2**2) * np.exp(-0.25 * x_norm[i]**2)
        
        # Enhanced cross-dimensional coupling with non-linear interaction
        enhanced_cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Non-linear coupling with exponential decay and enhanced interaction
                coupling = np.exp(-0.25 * (x_norm[i] - x_norm[j])**2) * np.sin(3 * (x_norm[i] + x_norm[j]))
                enhanced_cross_sum += coupling * (1.0 + 0.25 * np.abs(x_norm[i]) * np.abs(x_norm[j]) + 0.08 * x_norm[i]**2 * x_norm[j]**2)
        
        # Combine all components with adaptive weighting
        result = 0.2 * trig_sum + 0.15 * radial_sum + 0.2 * cross_sum + 0.15 * basin_sum + 0.1 * fractal_sum + 0.1 * spec_sum + 0.05 * quat_sum + 0.05 * enhanced_cross_sum
        
        # Adaptive conditioning with dimension-dependent factors
        condition_factor = 1.0 + 0.25 * np.log(self.dim + 1)
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.15 * np.abs(x_norm[i]) + 0.03 * x_norm[i]**2 + 0.02 * np.sin(x_norm[i]))
        
        # Final transformation with fractal scaling
        return result * condition_factor * (1.0 + 0.15 * np.sum(np.abs(x_norm)**3) + 0.03 * np.sum(x_norm**4))