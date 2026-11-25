import numpy as np

class MultimodalOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sinusoidal oscillation component with varying frequencies and amplitudes
        oscillation = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            amp = 1.0 + 0.5 * np.cos(i * 0.7)
            oscillation += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.5)
        
        # Radial basis function component with multiple centers and varying widths
        rbf = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.3) * 0.8
            width = 0.5 + 0.3 * np.cos(i * 0.4)
            rbf += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Cross-term interactions creating complex landscape structure
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Interaction terms with trigonometric modulation
                interaction = np.sin(x_scaled[i] * x_scaled[j]) * \
                             np.cos(0.5 * (x_scaled[i]**2 + x_scaled[j]**2)) * \
                             np.exp(-0.1 * (x_scaled[i] - x_scaled[j])**2)
                cross_term += interaction
        
        # Polynomial modulation with oscillatory behavior
        poly_mod = 0.0
        for i in range(self.dim):
            poly_mod += (x_scaled[i]**4 - 2*x_scaled[i]**2 + 1) * \
                       np.sin(3 * x_scaled[i]) * np.cos(2 * x_scaled[i])
        
        # Combined function with carefully balanced weights
        return 0.7 * oscillation + 1.2 * rbf + 0.8 * cross_term + 0.6 * poly_mod