import numpy as np

class MultimodalOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Primary trigonometric oscillation component
        oscillation = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(x_scaled[i] * 2.0)
            amp = 1.0 + 0.4 * np.cos(x_scaled[i] * 3.0)
            oscillation += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Radial basis function landscape with multiple centers
        rbf = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                center = centers[i]
                sigma = 0.3 + 0.2 * np.sin(i * 0.5)
                rbf += np.exp(-0.5 * ((x_scaled[i] - center) / sigma)**2)
        
        # Asymmetric penalty terms creating non-smooth regions
        penalty = 0.0
        for i in range(self.dim):
            if x_scaled[i] > 0:
                penalty += 2.0 * np.exp(-x_scaled[i]**2) + 0.5 * x_scaled[i]**4
            else:
                penalty += 1.5 * np.exp(x_scaled[i]**2) + 0.3 * x_scaled[i]**3
        
        # Cross-term interactions creating complex coupling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = 1.0 / (1.0 + np.abs(i - j))
                cross += weight * np.sin(x_scaled[i] * x_scaled[j]) * \
                        np.cos(x_scaled[i] + x_scaled[j])
        
        # Fractional dimensionality scaling with periodic modulation
        frac_dim = 0.0
        for i in range(self.dim):
            mod = 1.0 + 0.3 * np.sin(i * 0.8)
            frac_dim += (x_scaled[i]**2)**mod
        
        # Combined function with dynamic weighting
        return 0.8 * oscillation + 1.2 * rbf + 0.6 * penalty + 0.4 * cross + 0.3 * frac_dim