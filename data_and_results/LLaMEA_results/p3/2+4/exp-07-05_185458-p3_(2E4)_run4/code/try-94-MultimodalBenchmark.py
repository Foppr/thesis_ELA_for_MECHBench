import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial basis function component with chaotic center placements and dynamic amplitudes
        rb = 0.0
        for i in range(self.dim):
            center = np.sin(i * np.pi / 3.0) * 0.9
            amp = 0.7 + 0.3 * np.cos(i * np.pi / 5.0)
            rb += amp * np.exp(-15 * (x_norm[i] - center)**2) * np.cos(20 * (x_norm[i] - center))
        
        # Improved chaotic cosine modulation with frequency modulation and amplitude variation
        chaos = 0.0
        for i in range(self.dim):
            freq = 3**(i % 4 + 1) * np.pi
            amp = 0.6 + 0.4 * np.sin(i * np.pi / 2.0)
            chaos += amp * np.cos(freq * x_norm[i] + np.sin(freq * x_norm[i]) * np.cos(i * np.pi / 4.0))
        
        # Asymmetric polynomial interactions with dynamic coupling coefficients
        poly = 0.0
        for i in range(self.dim):
            coeff = 0.5 + 0.5 * np.sin(i * np.pi / 4.0)
            poly += coeff * (x_norm[i]**3 + 0.4 * x_norm[i]**5 + 0.2 * x_norm[i]**7) * np.cos(x_norm[(i+1) % self.dim] * x_norm[(i+2) % self.dim])
        
        # Enhanced cross-dimensional coupling with sine-based interaction and dynamic weights
        cross = 0.0
        for i in range(self.dim - 2):
            weight = 0.8 + 0.2 * np.sin(i * np.pi / 3.0)
            cross += weight * np.sin(x_norm[i] * x_norm[i+1]) * (x_norm[i]**2 + x_norm[i+1]**2 + 0.5 * x_norm[i+2]**2)
        
        # Additional chaotic interference with exponential weighting and sinusoidal modulation
        interference = 0.0
        for i in range(self.dim):
            interference += np.exp(-x_norm[i]**2) * np.sin(25 * x_norm[i] + np.cos(15 * x_norm[i]) * np.sin(i * np.pi / 6.0))
        
        # Dynamic weighted combination with modified coefficients
        return 0.9 * rb + 0.7 * chaos + 0.5 * poly + 0.4 * cross + 0.3 * interference + 0.15 * np.sum(x_norm**2)