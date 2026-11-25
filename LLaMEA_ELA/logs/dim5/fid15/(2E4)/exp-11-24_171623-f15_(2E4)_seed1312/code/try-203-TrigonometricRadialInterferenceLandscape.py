import numpy as np

class TrigonometricRadialInterferenceLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute angular frequencies and radial basis parameters with enhanced complexity
        self.angles = np.array([i * np.pi / (dim + 1) for i in range(dim)])
        self.radial_params = np.array([1.0 + 0.5 * np.sin(i * np.pi / dim) for i in range(dim)])
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced trigonometric oscillation component with increased frequency variation
        trig_sum = 0.0
        for i in range(self.dim):
            freq = 2.0 + 6.0 * np.sin(i * np.pi / (self.dim + 3))
            trig_sum += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Modified radial symmetry component with multi-scale influence and enhanced nonlinearity
        radial_sum = 0.0
        for i in range(self.dim):
            radius = np.sqrt(np.sum(x_norm[:i+1]**2)) if i > 0 else np.abs(x_norm[0])
            width = self.radial_params[i]
            radial_sum += np.exp(-0.5 * (radius / width)**3) * np.sin(5 * radius)
        
        # Enhanced cross-dimensional interference patterns with stronger coupling
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling = np.exp(-dist**3) * np.sin(8 * (x_norm[i] + x_norm[j]))
                cross_sum += coupling
        
        # Modified harmonic modulation with altered exponents and increased complexity
        harm_sum = 0.0
        for i in range(self.dim):
            scale = 2.0 + 0.3 * np.sin(i * np.pi / self.dim)
            harm_sum += np.sin(scale * x_norm[i])**5 + np.cos(scale * x_norm[i])**5
        
        # Improved basin regions with modified polynomial potentials and enhanced asymmetry
        basin_sum = 0.0
        for i in range(self.dim):
            if x_norm[i] < 0:
                basin_sum += (x_norm[i]**7 - 0.3 * x_norm[i]**4 + 0.2 * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
            else:
                basin_sum += (x_norm[i]**6 - 0.4 * x_norm[i]**3 + 0.12 * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2)
        
        # Combined landscape with adjusted weights and improved conditioning
        result = 0.3 * trig_sum + 0.25 * radial_sum + 0.2 * cross_sum + 0.18 * harm_sum + 0.07 * basin_sum
        
        # Enhanced conditioning factor based on input magnitude and dimensionality
        condition_factor = 1.0 + 0.6 * np.log(self.dim + 1)
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.3 * np.abs(x_norm[i]) + 0.2 * x_norm[i]**2 + 0.15 * np.sin(4 * x_norm[i]))
        
        # Final transformation with global scaling and improved penalty terms
        return result * condition_factor * (1.0 + 0.5 * np.sum(np.abs(x_norm)**5) + 0.2 * np.sum(x_norm**7))