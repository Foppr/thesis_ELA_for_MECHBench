import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis functions with varying widths and centers
        rbfs = 0.0
        centers = np.random.uniform(-4, 4, (10, self.dim))
        widths = np.random.uniform(0.5, 2.0, 10)
        for i in range(10):
            dist = np.sum((x - centers[i]) ** 2)
            rbfs += widths[i] * np.exp(-dist / (2 * widths[i]**2))
        
        # Quaternion-inspired rotational symmetry component
        rot_sym = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                rot_sym += (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        
        # Adaptive noise injection based on position
        noise = 0.0
        for i in range(self.dim):
            noise += np.random.normal(0, 0.1 * (1 + np.abs(x[i]) / 5.0)) * np.sin(x[i])
        
        # Dynamic conditioning with exponential scaling
        cond = 0.0
        for i in range(self.dim):
            cond += (1 + 0.5 * np.sin(x[i])) * x[i]**4
        
        # Multi-scale fractal-like interaction using sine and cosine products
        fractal = 0.0
        scales = [0.1, 0.3, 1.0, 3.0]
        for scale in scales:
            fractal += np.sum(np.sin(scale * x) * np.cos(scale * x))
        
        # Combined fitness function with dynamic weights
        return 0.3 * rbfs + 0.25 * rot_sym + 0.2 * noise + 0.15 * cond + 0.1 * fractal