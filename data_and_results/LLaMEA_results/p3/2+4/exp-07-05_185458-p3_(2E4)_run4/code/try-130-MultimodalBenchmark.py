import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.tent_map = np.zeros(dim)
        self.tent_map[0] = 0.3
        for i in range(1, dim):
            self.tent_map[i] = 1.5 * self.tent_map[i-1] * (1 - self.tent_map[i-1])
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Spherical harmonic component with varying degrees
        sph_harm = 0.0
        for i in range(self.dim):
            degree = i % 5 + 1
            sph_harm += (x_norm[i]**2 + 0.5 * x_norm[(i+1) % self.dim]**2) * np.sin(degree * np.arctan2(x_norm[(i+1) % self.dim], x_norm[i]))
        
        # Adaptive Gaussian peaks with dynamic centers and widths
        gaussian = 0.0
        for i in range(self.dim):
            center = np.sin(self.tent_map[i] * np.pi) * 0.8
            width = 0.2 + 0.3 * np.cos(i * np.pi / 4.0)
            gaussian += np.exp(-0.5 * ((x_norm[i] - center) / width)**2) * np.cos(10 * (x_norm[i] - center))
        
        # Chaotic sine coupling with tent map modulation
        chaos_coupling = 0.0
        for i in range(self.dim):
            coupling_strength = 0.5 + 0.5 * self.tent_map[i]
            chaos_coupling += coupling_strength * np.sin(15 * x_norm[i]) * np.cos(12 * x_norm[(i+1) % self.dim])
        
        # Dynamic polynomial interactions with dimensionality scaling
        poly = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(i * np.pi / 3.0)
            poly += scale_factor * (x_norm[i]**3 + 0.4 * x_norm[i]**5 + 0.1 * x_norm[i]**7) * np.sin(x_norm[(i+2) % self.dim])
        
        # Cross-dimensional cosine interactions with phase modulation
        cross_cos = 0.0
        for i in range(self.dim - 1):
            phase = 0.3 * np.sin(i * np.pi / 5.0)
            cross_cos += np.cos(8 * x_norm[i] + phase) * np.cos(6 * x_norm[i+1] + phase) * (x_norm[i]**2 + x_norm[i+1]**2)
        
        # Final combined function
        return 0.8 * sph_harm + 0.6 * gaussian + 0.5 * chaos_coupling + 0.4 * poly + 0.3 * cross_cos + 0.2 * np.sum(x_norm**2)