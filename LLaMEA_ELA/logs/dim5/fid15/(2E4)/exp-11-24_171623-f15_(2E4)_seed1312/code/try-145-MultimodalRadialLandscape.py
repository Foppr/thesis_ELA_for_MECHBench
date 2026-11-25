import numpy as np

class MultimodalRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sinusoidal components with non-linear modulation
        sin_sum = 0.0
        for i in range(self.dim):
            freq = 3 + 2 * np.sin(x_norm[i] * 2.0) + 0.5 * np.sin(x_norm[i] * 7.0)
            amp = 1.0 + 0.3 * np.cos(x_norm[i] * 3.0)
            sin_sum += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.7)
        
        # Dynamic radial basis functions with chaotic widths and positions
        rb_sum = 0.0
        for i in range(min(7, self.dim)):
            center = np.sin(i * 1.3) * 0.8 + 0.2 * np.cos(i * 2.1)
            width = 0.5 + 0.5 * np.sin(i * 0.9) + 0.3 * np.cos(i * 1.7)
            dist = np.sum((x_norm - center)**2)
            rb_sum += np.exp(-dist * width) * (1 + 0.4 * np.sin(i * 2.5))
        
        # Cross-dimensional polynomial couplings with chaotic exponents
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_i = 1.5 + 0.5 * np.sin(i * 1.2)
                exp_j = 1.5 + 0.5 * np.cos(j * 1.8)
                coupling = (x_norm[i]**exp_i + x_norm[j]**exp_j) * np.sin(x_norm[i] * x_norm[j] * 5.0)
                cross_sum += coupling
        
        # Valley structure with chaotic exponential decay
        valley_sum = 0.0
        for i in range(self.dim):
            decay = 0.3 + 0.2 * np.sin(i * 1.1)
            valley_sum += (x_norm[i]**2) * np.exp(-decay * x_norm[i]**2) * (1 + 0.3 * np.sin(x_norm[i] * 9.0))
        
        # Adaptive conditioning with chaotic scaling
        cond_factor = 1.0 + 0.5 * np.sin(self.dim * 0.7 + np.cos(self.dim * 0.3))
        
        # Add chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x_norm[i] * 13.0) * np.cos(x_norm[i] * 8.0) * (0.1 + 0.05 * np.sin(i * 2.3))
        
        # Combine all components with chaotic weights
        result = 0.25 * rb_sum + 0.3 * sin_sum + 0.2 * cross_sum + 0.25 * valley_sum
        
        return result * cond_factor + noise * (1 + 0.1 * np.sum(np.abs(x_norm)))