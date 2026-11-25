import numpy as np

class MultimodalRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function components with varying widths
        rb_sum = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = centers[i] if self.dim > 1 else 0.0
            width = 0.5 + 0.5 * np.sin(i * np.pi / max(1, self.dim - 1))
            rb_sum += np.exp(-0.5 * np.sum((x_norm - center)**2) / (width**2))
        
        # Sinusoidal oscillations with adaptive frequency and amplitude
        sin_sum = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * np.pi / max(1, self.dim - 1))
            amp = 1.0 + 0.5 * np.cos(i * np.pi / max(1, self.dim - 1))
            sin_sum += amp * np.sin(freq * x_norm[i])
        
        # Cross-dimensional coupling with polynomial interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term = (x_norm[i]**2 + x_norm[j]**2) * np.sin(x_norm[i] * x_norm[j])
                cross_coupling += poly_term
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Valley structure with hyperbolic tangent smoothing
        valley_sum = 0.0
        for i in range(self.dim):
            valley_sum += np.tanh(x_norm[i] * 2.0) * (x_norm[i]**4 - 2*x_norm[i]**2 + 1)
        
        # Combine all components with dynamic weights
        result = 0.3 * rb_sum + 0.25 * sin_sum + 0.2 * cross_coupling + 0.25 * valley_sum
        
        return result * condition_factor * (1 + 0.2 * np.sum(x_norm**2))