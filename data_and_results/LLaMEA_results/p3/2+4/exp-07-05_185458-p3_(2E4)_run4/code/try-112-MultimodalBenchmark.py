import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Modified radial basis function component with shifted centers and altered weights
        rb = 0.0
        for i in range(self.dim):
            center = np.cos(i * np.pi / 4.0) * 0.8
            weight = 1.2 + 0.3 * np.cos(i * np.pi / 3.0)
            rb += weight * np.exp(-20 * (x_norm[i] - center)**2) * np.sin(25 * (x_norm[i] - center))
        
        # Altered chaotic cosine modulation with modified frequencies and amplitudes
        chaos = 0.0
        for i in range(self.dim):
            freq = 4**(i % 5 + 1) * np.pi
            amp = 0.8 + 0.2 * np.cos(i * np.pi / 6.0)
            phase = 0.3 * np.sin(i * np.pi / 7.0)
            chaos += amp * np.sin(freq * x_norm[i] + phase + np.cos(freq * x_norm[i]))
        
        # Modified asymmetric polynomial interactions with different exponents and coupling
        poly = 0.0
        for i in range(self.dim):
            poly += (x_norm[i]**5 + 0.3 * x_norm[i]**7 + 0.2 * x_norm[i]**9) * np.sin(x_norm[(i+1) % self.dim]) * np.cos(x_norm[(i+2) % self.dim])
        
        # Modified cross-dimensional coupling with enhanced sine-based interaction
        cross = 0.0
        for i in range(self.dim - 1):
            cross += np.cos(x_norm[i] * x_norm[i+1]) * (x_norm[i]**4 + x_norm[i+1]**4) + 0.4 * np.sin(x_norm[i] + x_norm[i+1])
        
        # Altered chaotic interference with modified exponential weighting and sine modulation
        interference = 0.0
        for i in range(self.dim):
            interference += np.exp(-0.5 * x_norm[i]**2) * np.cos(30 * x_norm[i] + np.sin(20 * x_norm[i])) + 0.2 * np.sin(35 * x_norm[i])
        
        # Additional modified high-frequency oscillation component
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.cos(60 * x_norm[i]) * np.sin(50 * x_norm[i])
        
        # Final combined function with adjusted component weights
        return 0.8 * rb + 0.6 * chaos + 0.4 * poly + 0.3 * cross + 0.2 * interference + 0.15 * high_freq + 0.05 * np.sum(x_norm**2)