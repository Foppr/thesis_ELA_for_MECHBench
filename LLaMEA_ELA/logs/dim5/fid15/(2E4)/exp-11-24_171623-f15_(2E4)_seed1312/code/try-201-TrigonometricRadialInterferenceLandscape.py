import numpy as np

class TrigonometricRadialInterferenceLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute angular frequencies and radial basis parameters with slight modifications
        self.angles = np.array([i * np.pi / (dim + 1) for i in range(dim)])
        self.radial_params = np.array([1.2 + 0.3 * np.sin(i * np.pi / dim) for i in range(dim)])
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Trigonometric oscillation component with varying frequencies
        trig_sum = 0.0
        for i in range(self.dim):
            freq = 1.5 + 4.0 * np.sin(i * np.pi / (self.dim + 2))
            trig_sum += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Radial symmetry component with multi-scale influence
        radial_sum = 0.0
        for i in range(self.dim):
            radius = np.sqrt(np.sum(x_norm[:i+1]**2)) if i > 0 else np.abs(x_norm[0])
            width = self.radial_params[i]
            radial_sum += np.exp(-0.5 * (radius / width)**2) * np.sin(4 * radius)
        
        # Cross-dimensional interference patterns with enhanced coupling
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling = np.exp(-dist**2) * np.sin(7 * (x_norm[i] + x_norm[j]))
                cross_sum += coupling
        
        # Multi-scale harmonic modulation with altered exponents
        harm_sum = 0.0
        for i in range(self.dim):
            scale = 1.5 + 0.2 * np.sin(i * np.pi / self.dim)
            harm_sum += np.sin(scale * x_norm[i])**4 + np.cos(scale * x_norm[i])**4
        
        # Asymmetric basin regions with modified polynomial potentials
        basin_sum = 0.0
        for i in range(self.dim):
            if x_norm[i] < 0:
                basin_sum += (x_norm[i]**6 - 0.4 * x_norm[i]**3 + 0.15 * x_norm[i]) * np.exp(-0.25 * x_norm[i]**2)
            else:
                basin_sum += (x_norm[i]**5 - 0.5 * x_norm[i]**2 + 0.08 * x_norm[i]) * np.exp(-0.15 * x_norm[i]**2)
        
        # Combined landscape with adjusted weights
        result = 0.25 * trig_sum + 0.3 * radial_sum + 0.25 * cross_sum + 0.15 * harm_sum + 0.05 * basin_sum
        
        # Conditioning factor based on input magnitude and dimensionality
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.25 * np.abs(x_norm[i]) + 0.15 * x_norm[i]**2 + 0.1 * np.sin(3 * x_norm[i]))
        
        # Final transformation with global scaling
        return result * condition_factor * (1.0 + 0.4 * np.sum(np.abs(x_norm)**4) + 0.15 * np.sum(x_norm**6))