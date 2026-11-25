import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for conditioning
        self.rotation_matrix = np.random.rand(dim, dim) * 2 - 1
        self.rotation_matrix = np.linalg.qr(self.rotation_matrix)[0]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Rotate input for conditioning
        x_rot = self.rotation_matrix @ x
        
        # Elliptic component with varying condition numbers
        elliptic = 0
        for i in range(self.dim):
            elliptic += (10 ** (2 * i / (self.dim - 1))) * x_rot[i]**2
            
        # Embedded Gaussian peaks with varying heights and widths
        gaussian = 0
        peak_centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = peak_centers[i] if self.dim > 1 else 0
            gaussian += 2.5 * np.exp(-0.5 * ((x_rot[0] - center) / (1.5 + 0.2 * i))**2)
            
        # Cross-dimensional quadratic interactions
        cross_quad = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_quad += 0.3 * x_rot[i] * x_rot[j] / (1 + abs(x_rot[i]) + abs(x_rot[j]))
                
        # Sinusoidal modulation to increase complexity
        sin_mod = 0
        for i in range(self.dim):
            sin_mod += np.sin(0.7 * np.pi * x_rot[i]) * np.cos(0.3 * np.pi * x_rot[i])
            
        return 0.5 * elliptic + gaussian + 0.8 * cross_quad + 0.2 * sin_mod + 2.0 * self.dim