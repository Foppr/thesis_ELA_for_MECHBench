import numpy as np

class FractalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal parameters for self-similarity
        self.hurst = 0.3
        self.fractal_dim = 1.5 + 0.2 * np.random.rand()
        # Ridge and basin parameters
        self.ridge_strength = 2.0 + np.random.rand() * 3.0
        self.basin_depth = 1.0 + np.random.rand() * 2.0
        self.adaptivity = 0.5 + np.random.rand() * 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal component using fractional Brownian motion-like scaling
        fractal = 0.0
        for i in range(self.dim):
            # Scale dimension index for fractal behavior
            scaled_i = (i + 1) / self.dim
            # Multi-scale fractal pattern with varying exponents
            fractal_term = 0.0
            scales = [1.0, 0.5, 0.25, 0.125]
            for scale in scales:
                freq = 2.0 * np.pi / scale
                # Fractal-like oscillation with Hurst parameter influence
                fractal_term += np.sin(freq * x[i] * scaled_i**self.hurst) * scale**self.fractal_dim
            fractal += fractal_term**2
            
        # Ridge structure component with adaptive strength
        ridge = 0.0
        for i in range(self.dim):
            # Adaptive ridge based on dimension position and solution proximity
            ridge_pos = (x[i] + 5.0) / 10.0
            # Dynamic ridge orientation and amplitude
            amp = self.ridge_strength * (1.0 + 0.3 * np.sin(i * np.pi / self.dim))
            ridge += amp * np.exp(-0.5 * (x[i] - 2.0 * np.sin(0.5 * i * np.pi))**2)
            
        # Basin structure with dynamic depth
        basin = 0.0
        for i in range(self.dim):
            # Basin boundaries that change based on solution proximity
            dist_from_center = abs(x[i])
            # Dynamic basin depth modulation
            depth = self.basin_depth * (1.0 + 0.5 * np.cos(i * np.pi / self.dim))
            basin += depth * np.exp(-0.3 * dist_from_center**2) * np.sin(0.4 * x[i])**2
            
        # Cross-dimensional interaction with fractal coupling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                # Fractal coupling strength based on dimension indices
                coupling = (i + j)**(-self.fractal_dim) * np.exp(-0.1 * abs(diff))
                cross += coupling * np.sin(3.0 * diff) * np.cos(2.0 * diff)
                
        # Adaptive scaling based on solution quality and dimensionality
        adapt_scale = 1.0 + self.adaptivity * (1.0 - np.linalg.norm(x) / 5.0)
        
        # Combine all components with adaptive weights
        result = adapt_scale * (0.8 * fractal + 1.2 * ridge + 0.9 * basin + 0.7 * cross)
        
        # Add dimensionality-dependent offset
        result += 0.5 * self.dim
        
        return result