import numpy as np

class HierarchicalSpiralFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        
        # Hierarchical Gaussian peaks with varying heights and widths
        self.peak_centers = np.random.uniform(-4.0, 4.0, (dim, dim))
        self.peak_heights = np.random.uniform(1.0, 5.0, dim)
        self.peak_widths = np.random.uniform(0.5, 2.0, dim)
        
        # Adaptive spiral forces with varying rotation speeds
        self.spiral_centers = np.random.uniform(-3.0, 3.0, (dim, dim))
        self.spiral_speeds = np.random.uniform(0.5, 3.0, dim)
        self.spiral_amplitudes = np.random.uniform(1.0, 4.0, dim)
        
        # Dynamic correlation matrices for dimension interactions
        self.correlation_matrices = []
        for _ in range(dim):
            matrix = np.random.rand(dim, dim) * 2 - 1
            matrix = (matrix + matrix.T) / 2
            np.fill_diagonal(matrix, 0.0)
            self.correlation_matrices.append(matrix)
        
        # Self-similar fractal noise parameters
        self.fractal_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.fractal_frequencies = np.random.uniform(1.0, 5.0, dim)
        self.fractal_roughness = np.random.uniform(0.1, 0.9, dim)
        
        # Adaptive scaling factors
        self.scaling_factors = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Hierarchical Gaussian peaks
        for i in range(self.dim):
            peak_value = 0.0
            for j in range(self.dim):
                distance = (x[j] - self.peak_centers[i][j])**2
                peak_value += np.exp(-distance / (2 * self.peak_widths[i]**2))
            result += self.peak_heights[i] * peak_value
            
        # Adaptive spiral forces
        for i in range(self.dim):
            spiral_value = 0.0
            for j in range(self.dim):
                dx = x[j] - self.spiral_centers[i][j]
                dy = x[(j + 1) % self.dim] - self.spiral_centers[i][(j + 1) % self.dim]
                distance = np.sqrt(dx**2 + dy**2)
                angle = np.arctan2(dy, dx)
                spiral_value += self.spiral_amplitudes[i] * np.sin(self.spiral_speeds[i] * distance + angle)
            result += spiral_value
            
        # Dynamic correlation interactions
        for i in range(self.dim):
            corr_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    corr_sum += self.correlation_matrices[i][j] * x[i] * x[j]
            result += corr_sum
            
        # Self-similar fractal noise
        for i in range(self.dim):
            noise_value = 0.0
            for k in range(1, 6):
                freq = self.fractal_frequencies[i] * (2 ** k)
                amp = self.fractal_amplitudes[i] * (self.fractal_roughness[i] ** k)
                noise_value += amp * np.sin(freq * x[i])
            result += noise_value
            
        # Adaptive scaling
        for i in range(self.dim):
            result *= (1.0 + self.scaling_factors[i] * np.sin(x[i]))
            
        # Add a global distortion term
        global_distortion = 0.0
        for i in range(self.dim):
            global_distortion += np.sin(x[i]**3) * np.cos(x[i])
        result += 0.5 * global_distortion
        
        return result