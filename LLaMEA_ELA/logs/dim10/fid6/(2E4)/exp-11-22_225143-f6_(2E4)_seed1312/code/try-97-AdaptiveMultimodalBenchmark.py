import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random parameters for each dimension
        self.wave_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.wave_frequencies = np.random.uniform(1.0, 8.0, dim)
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, 3))
        self.rbf_widths = np.random.uniform(0.5, 2.5, (dim, 3))
        self.conditioning_factors = np.random.uniform(0.1, 2.0, dim)
        self.local_minima_positions = np.random.uniform(-4.0, 4.0, (dim, 5))
        self.local_minima_heights = np.random.uniform(0.1, 1.5, (dim, 5))
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Sinusoidal wave components with adaptive frequencies and amplitudes
        for i in range(self.dim):
            wave_component = self.wave_amplitudes[i] * np.sin(self.wave_frequencies[i] * x_norm[i])
            f_val += wave_component**2
        
        # Radial basis function components with multiple centers per dimension
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(3):
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[i, j]
                rbf_sum += np.exp(-0.5 * ((x_norm[i] - center) / width)**2)
            f_val += 0.5 * rbf_sum
        
        # Adaptive conditioning with dimension-specific scaling
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * x_norm[i]**4
        
        # Local minima landscape with multiple peaks and valleys
        for i in range(self.dim):
            local_sum = 0.0
            for j in range(5):
                pos = self.local_minima_positions[i, j]
                height = self.local_minima_heights[i, j]
                local_sum += height * np.exp(-0.5 * ((x_norm[i] - pos) / 0.3)**2)
            f_val += 0.3 * local_sum
        
        # Enhanced cross-dimension interaction terms with stronger coupling
        coupling_strengths = np.random.uniform(0.5, 1.5, self.dim)
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling range
                coupling = coupling_strengths[i] * np.sin(x_norm[i]) * np.cos(x_norm[j])
                f_val += 0.3 * coupling**2
        
        # Modified global trend with quadratic polynomial terms for better conditioning
        poly_terms = [x_norm[i]**2 for i in range(self.dim)]
        f_val += 0.15 * sum(poly_terms)
        
        # Add a small noise component to increase robustness
        noise = np.random.uniform(-0.01, 0.01)
        f_val += noise
        
        return f_val