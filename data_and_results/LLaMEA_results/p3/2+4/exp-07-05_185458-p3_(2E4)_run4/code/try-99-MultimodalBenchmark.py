import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component with varying frequencies and amplitudes
        sin_comp = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(i * np.pi / 4.0)
            amp = 1.0 + 0.5 * np.cos(i * np.pi / 3.0)
            sin_comp += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Polynomial conditioning with asymmetric weights
        poly_comp = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.3 * np.sin(i * np.pi / 2.0)
            poly_comp += weight * (x_norm[i]**4 + 0.5 * x_norm[i]**6 + 0.1 * x_norm[i]**8)
        
        # Radial basis function with asymmetric center placement and varying widths
        rb_comp = 0.0
        for i in range(self.dim):
            center = 0.5 * np.sin(i * np.pi / 3.0)
            width = 0.8 + 0.4 * np.cos(i * np.pi / 4.0)
            rb_comp += np.exp(-width * (x_norm[i] - center)**2) * np.sin(10 * (x_norm[i] - center))
        
        # Cross-dimensional coupling with exponential interaction
        cross_comp = 0.0
        for i in range(self.dim - 1):
            cross_comp += np.exp(-0.5 * (x_norm[i]**2 + x_norm[i+1]**2)) * np.sin(5 * x_norm[i] * x_norm[i+1])
        
        # Asymmetric scaling component
        scale_comp = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.2 * np.sin(i * np.pi / 2.0)
            scale_comp += scale * np.abs(x_norm[i])**1.5
        
        # Final combined function with carefully weighted components
        return 0.6 * sin_comp + 0.4 * poly_comp + 0.3 * rb_comp + 0.25 * cross_comp + 0.15 * scale_comp + 0.02 * np.sum(x_norm**2)