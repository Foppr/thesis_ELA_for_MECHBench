import numpy as np

class RadialFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for each dimension
        self.fractal_params = np.random.uniform(0.5, 2.0, (dim, 3))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with dynamic centers and widths
        rbf = 0.0
        num_centers = min(20, self.dim * 3)
        centers = np.random.uniform(-4.5, 4.5, (num_centers, self.dim))
        
        for i in range(num_centers):
            center = centers[i]
            # Dynamic width based on dimension
            widths = 0.5 + 0.5 * np.sin(np.arange(self.dim) * 0.7 + i)
            dist_sq = np.sum(((x - center) / widths) ** 2)
            rbf += np.exp(-dist_sq / 2.0)
        
        # Fractal noise component with multi-scale self-similarity
        fractal = 0.0
        for i in range(self.dim):
            # Multi-scale fractal noise using sine and cosine combinations
            scale = self.fractal_params[i, 0]
            amp = self.fractal_params[i, 1]
            freq = self.fractal_params[i, 2]
            
            # Combine multiple frequencies for fractal-like behavior
            noise = (amp * np.sin(freq * x[i]) + 
                    0.5 * amp * np.sin(2 * freq * x[i]) + 
                    0.3 * amp * np.sin(3 * freq * x[i]))
            
            # Add scale-dependent modulation
            fractal += noise * np.exp(-0.1 * (x[i] ** 2)) * scale
        
        # Cross-dimensional coupling with dynamic weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Dynamic coupling weight based on both dimensions
                weight = 0.5 + 0.5 * np.sin(0.3 * (x[i] + x[j]))
                coupling += weight * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Asymmetric saddle points with varying curvature
        saddle = 0.0
        for i in range(self.dim):
            # Create asymmetric saddle with dynamic location and curvature
            loc = 1.5 * np.sin(0.5 * i) * (1.0 + 0.2 * np.cos(i))
            curvature = 1.0 + 0.8 * np.sin(0.3 * i)
            saddle += (x[i] - loc)**2 * (x[i] - loc)**4 * curvature
        
        # Nonlinear transformation with chaotic modulation
        nonlinear = 0.0
        for i in range(self.dim):
            # Apply chaotic modulation to each dimension
            chaos_mod = np.sin(1.7 * x[i]) * np.cos(2.3 * x[i])
            nonlinear += (x[i]**3 + chaos_mod) * np.exp(-0.1 * x[i]**2)
        
        # Add global scaling and combine components
        total = (rbf * 0.4 + 
                fractal * 0.35 +
                coupling * 0.25 +
                saddle * 0.2 +
                nonlinear * 0.3)
        
        return total