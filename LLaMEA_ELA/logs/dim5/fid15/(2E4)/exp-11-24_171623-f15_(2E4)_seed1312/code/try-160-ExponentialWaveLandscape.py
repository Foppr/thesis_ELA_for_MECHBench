import numpy as np

class ExponentialWaveLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay components with varying rates
        exp_sum = 0.0
        for i in range(self.dim):
            rate = 0.5 + 1.5 * np.abs(np.sin(i * np.pi / (self.dim + 1)))
            exp_sum += np.exp(-rate * np.abs(x_norm[i])) * np.cos(rate * x_norm[i])
        
        # Trigonometric wave interference patterns
        wave_sum = 0.0
        for i in range(self.dim):
            freq1 = 2.0 + 3.0 * np.sin(i * np.pi / (self.dim + 2))
            freq2 = 1.0 + 2.0 * np.cos(i * np.pi / (self.dim + 3))
            wave_sum += np.sin(freq1 * x_norm[i]) * np.cos(freq2 * x_norm[i])
        
        # Adaptive conditioning based on dimension and position
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.1 * np.abs(x_norm[i]))
        
        # Multi-scale harmonic modulation with exponential weights
        mod_sum = 0.0
        for i in range(self.dim):
            scale = 2.0**(i % 3)
            weight = 1.0 / (1.0 + np.exp(-scale))
            mod_sum += weight * np.sin(scale * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Cross-dimensional interaction terms with exponential coupling
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * np.sin(x_norm[i] + x_norm[j])
                cross_sum += coupling
        
        # Asymmetric basin structure with exponential basins
        basin_sum = 0.0
        for i in range(self.dim):
            if x_norm[i] < 0:
                basin_sum += np.exp(-x_norm[i]**2) * (x_norm[i]**3 + 0.5 * x_norm[i])
            else:
                basin_sum += np.exp(-x_norm[i]**2) * (x_norm[i]**4 - 0.3 * x_norm[i]**2)
        
        # Combine all components with dynamic weights
        result = 0.2 * exp_sum + 0.3 * wave_sum + 0.25 * mod_sum + 0.15 * cross_sum + 0.1 * basin_sum
        
        return result * condition_factor * (1.0 + 0.2 * np.sum(x_norm**2))