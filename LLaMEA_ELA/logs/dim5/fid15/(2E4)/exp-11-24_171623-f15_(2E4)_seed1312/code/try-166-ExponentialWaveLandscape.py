import numpy as np

class ExponentialWaveLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay components with variable rates and interaction
        exp_sum = 0.0
        for i in range(self.dim):
            rate = 0.3 + 2.0 * np.abs(np.sin(i * np.pi / (self.dim + 1)))
            exp_sum += np.exp(-rate * np.abs(x_norm[i])) * np.cos(rate * x_norm[i] + i * 0.5)
        
        # Improved trigonometric wave interference with frequency modulation
        wave_sum = 0.0
        for i in range(self.dim):
            freq1 = 1.5 + 4.0 * np.sin(i * np.pi / (self.dim + 2))
            freq2 = 0.5 + 3.0 * np.cos(i * np.pi / (self.dim + 3))
            wave_sum += np.sin(freq1 * x_norm[i]) * np.cos(freq2 * x_norm[i]) * np.exp(-0.1 * i)
        
        # Enhanced adaptive conditioning with dynamic scaling factors
        condition_factor = 1.0 + 0.4 * np.log(self.dim + 1)
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.2 * np.abs(x_norm[i]) + 0.1 * x_norm[i]**2)
        
        # Multi-scale harmonic modulation with improved weights
        mod_sum = 0.0
        for i in range(self.dim):
            scale = 3.0**(i % 4)
            weight = 1.0 / (1.0 + np.exp(-scale * 0.5))
            mod_sum += weight * np.sin(scale * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Stronger cross-dimensional interaction terms with coupling strength
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = np.exp(-0.3 * (x_norm[i] - x_norm[j])**2) * np.sin(2 * (x_norm[i] + x_norm[j]))
                cross_sum += coupling * (1.0 + 0.2 * np.abs(x_norm[i] - x_norm[j]))
        
        # Modified asymmetric basin structure with polynomial and exponential components
        basin_sum = 0.0
        for i in range(self.dim):
            if x_norm[i] < 0:
                basin_sum += np.exp(-x_norm[i]**2) * (x_norm[i]**3 + 0.4 * x_norm[i] - 0.1)
            else:
                basin_sum += np.exp(-x_norm[i]**2) * (x_norm[i]**5 - 0.4 * x_norm[i]**3 + 0.1 * x_norm[i])
        
        # Combine all components with updated weights and add correlation term
        result = 0.25 * exp_sum + 0.35 * wave_sum + 0.2 * mod_sum + 0.15 * cross_sum + 0.05 * basin_sum
        
        # Add correlation and interaction terms to increase complexity
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_term += (x_norm[i] * x_norm[j]) / (1.0 + np.abs(x_norm[i] - x_norm[j]))
        
        return (result * condition_factor + 0.1 * corr_term) * (1.0 + 0.3 * np.sum(x_norm**2))