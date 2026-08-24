import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial basis function component with non-uniform center placements
        rb = 0.0
        for i in range(self.dim):
            center = np.sin(i * np.pi / 2.5) * 0.85
            rb += np.exp(-10 * (x_norm[i] - center)**2) * np.sin(15 * (x_norm[i] - center))
        
        # Modified chaotic cosine modulation with dynamic frequencies
        chaos = 0.0
        for i in range(self.dim):
            freq = 3**(i % 5 + 1) * np.pi
            amp = 0.5 + 0.5 * np.cos(i * np.pi / 3.0)
            chaos += amp * np.sin(freq * x_norm[i] + np.cos(freq * x_norm[i] + 0.3))
        
        # Asymmetric polynomial interactions with stronger coupling
        poly = 0.0
        for i in range(self.dim):
            poly += (x_norm[i]**4 + 0.5 * x_norm[i]**6 + 0.2 * x_norm[i]**8) * np.sin(x_norm[(i+1) % self.dim])
        
        # Enhanced cross-dimensional coupling with cosine interaction
        cross = 0.0
        for i in range(self.dim - 1):
            cross += np.cos(x_norm[i] * x_norm[i+1]) * (x_norm[i]**3 + x_norm[i+1]**3 + 0.15)
        
        # Increased chaotic interference with logarithmic weighting
        interference = 0.0
        for i in range(self.dim):
            interference += np.log(1 + 0.5 * x_norm[i]**2) * np.cos(30 * x_norm[i] + np.sin(15 * x_norm[i]))
        
        # Final combined function with adjusted weights for better conditioning
        return 0.8 * rb + 0.6 * chaos + 0.4 * poly + 0.3 * cross + 0.2 * interference + 0.03 * np.sum(x_norm**2)