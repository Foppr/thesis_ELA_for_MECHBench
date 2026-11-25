import numpy as np

class ExponentialWaveLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay with multi-scale modulation
        exp_sum = 0.0
        for i in range(self.dim):
            rate = 0.5 + 3.0 * np.abs(np.sin(i * np.pi / (self.dim + 1)))
            exp_sum += np.exp(-rate * np.abs(x_norm[i])) * np.cos(rate * x_norm[i] + i * 0.5)
        
        # Modified wave interference with frequency coupling
        wave_sum = 0.0
        for i in range(self.dim):
            freq1 = 2.0 + 5.0 * np.sin(i * np.pi / (self.dim + 2))
            freq2 = 1.0 + 4.0 * np.cos(i * np.pi / (self.dim + 3))
            wave_sum += np.sin(freq1 * x_norm[i] + 0.3 * np.sin(freq2 * x_norm[i]))
        
        # Enhanced adaptive conditioning with dimension-dependent factors
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.2 * np.abs(x_norm[i]) + 0.05 * x_norm[i]**2)
        
        # Multi-scale harmonic modulation with exponential weights and phase shifts
        mod_sum = 0.0
        for i in range(self.dim):
            scale = 4.0**(i % 5)
            weight = 1.0 / (1.0 + np.exp(-scale))
            phase_shift = 0.2 * np.sin(i * np.pi / self.dim)
            mod_sum += weight * np.sin(scale * x_norm[i] + phase_shift) * np.exp(-0.4 * x_norm[i]**2)
        
        # Enhanced cross-dimensional interaction with non-linear coupling
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling = np.exp(-0.2 * (x_norm[i] - x_norm[j])**2) * np.sin(3 * (x_norm[i] + x_norm[j]))
                cross_sum += coupling * (1.0 + 0.1 * np.abs(x_norm[i] * x_norm[j]))
        
        # Modified asymmetric basin structure with enhanced polynomial basins
        basin_sum = 0.0
        for i in range(self.dim):
            if x_norm[i] < 0:
                basin_sum += np.exp(-x_norm[i]**2) * (x_norm[i]**4 + 0.4 * x_norm[i]**2 + 0.1)
            else:
                basin_sum += np.exp(-x_norm[i]**2) * (x_norm[i]**5 - 0.3 * x_norm[i]**3 + 0.05 * x_norm[i])
        
        # Additional harmonic coupling and interaction terms
        interaction_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if j < i + 3:
                    interaction_sum += np.sin(2 * (x_norm[i] - x_norm[j])) * np.cos(1.5 * (x_norm[i] + x_norm[j]))
        
        # Combine all components with adjusted weights
        result = 0.3 * exp_sum + 0.3 * wave_sum + 0.15 * mod_sum + 0.15 * cross_sum + 0.1 * basin_sum + 0.05 * interaction_sum
        
        return result * condition_factor * (1.0 + 0.2 * np.sum(x_norm**2))