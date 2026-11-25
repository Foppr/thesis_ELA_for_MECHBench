import numpy as np

class FractalMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Recursive sine-wave harmonic parameters
        self.harmonic_freq = 1.0 + np.random.rand(dim) * 4.0
        self.harmonic_amp = 0.5 + np.random.rand(dim) * 2.0
        # Adaptive Gaussian mixture components
        self.gauss_centers = np.random.uniform(-4.0, 4.0, (dim, 3))
        self.gauss_heights = 1.0 + np.random.rand(dim, 3) * 3.0
        self.gauss_widths = 0.3 + np.random.rand(dim, 3) * 1.2
        # Directional conditioning factors
        self.conditioning_dirs = np.random.randn(dim, dim)
        self.conditioning_strength = 0.5 + np.random.rand(dim) * 2.0
        # Fractal recursion depth
        self.recursion_depth = max(1, int(np.log2(dim)) + np.random.randint(-1, 2))
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal sine-wave harmonic component
        fractal_harmonic = 0.0
        for i in range(self.dim):
            freq = self.harmonic_freq[i]
            amp = self.harmonic_amp[i]
            harmonic_sum = 0.0
            for depth in range(1, min(self.recursion_depth + 1, 5)):
                scale = 1.0 / (2 ** depth)
                harmonic_sum += amp * np.sin(freq * x[i] * scale) * scale
            fractal_harmonic += harmonic_sum
        
        # Adaptive Gaussian mixture with directional influence
        gauss_mixture = 0.0
        for i in range(self.dim):
            mix_sum = 0.0
            for j in range(3):
                center = self.gauss_centers[i, j]
                height = self.gauss_heights[i, j]
                width = self.gauss_widths[i, j]
                # Directional conditioning effect
                dir_cond = np.abs(np.dot(self.conditioning_dirs[i], x))
                mix_sum += height * np.exp(-0.5 * ((x[i] - center) / (width + 0.1 * dir_cond)) ** 2)
            gauss_mixture += mix_sum
        
        # Cross-dimensional directional conditioning
        dir_conditioning = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning_strength[i]
            dir_proj = np.abs(np.dot(self.conditioning_dirs[i], x))
            dir_conditioning += cond_factor * (x[i] ** 2) * (1.0 + 0.5 * np.sin(dir_proj))
        
        # Self-similar basin structure
        basin_structure = 0.0
        for i in range(self.dim):
            # Create basin-like curvature with recursive influence
            basin_sum = 0.0
            for k in range(1, min(4, self.recursion_depth + 2)):
                scale = 1.0 / (3 ** k)
                basin_sum += np.sin(x[i] * scale) * scale
            basin_structure += basin_sum ** 2
        
        # Combine components with dynamic weights based on dimensionality
        dim_factor = 1.0 + 0.3 * np.log(self.dim)
        return (0.35 * fractal_harmonic + 0.30 * gauss_mixture + 
                0.25 * dir_conditioning + 0.10 * basin_structure) * dim_factor