import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random parameters for each dimension
        self.wave_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.wave_frequencies = np.random.uniform(1.5, 9.0, dim)  # Slightly increased frequencies
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, 4))  # More RBF centers
        self.rbf_widths = np.random.uniform(0.3, 2.2, (dim, 4))   # Adjusted widths
        self.conditioning_factors = np.random.uniform(0.15, 2.5, dim)  # Wider range
        self.local_minima_positions = np.random.uniform(-4.0, 4.0, (dim, 6))  # More local minima
        self.local_minima_heights = np.random.uniform(0.15, 1.8, (dim, 6))    # Adjusted heights
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Sinusoidal wave components with adaptive frequencies and amplitudes
        for i in range(self.dim):
            wave_component = self.wave_amplitudes[i] * np.sin(self.wave_frequencies[i] * x_norm[i])
            f_val += wave_component**3  # Changed from square to cube for stronger nonlinearity
        
        # Radial basis function components with multiple centers per dimension
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(4):  # More RBF centers
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[i, j]
                rbf_sum += np.exp(-0.5 * ((x_norm[i] - center) / width)**3)  # Cubic exponent for sharper peaks
            f_val += 0.6 * rbf_sum  # Increased weight
        
        # Adaptive conditioning with dimension-specific scaling
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * x_norm[i]**5  # Fifth power for higher curvature
        
        # Local minima landscape with multiple peaks and valleys
        for i in range(self.dim):
            local_sum = 0.0
            for j in range(6):  # More local minima
                pos = self.local_minima_positions[i, j]
                height = self.local_minima_heights[i, j]
                local_sum += height * np.exp(-0.5 * ((x_norm[i] - pos) / 0.2)**3)  # Sharper peaks
            f_val += 0.4 * local_sum  # Increased contribution
        
        # Cross-dimension interaction terms with varying coupling strengths
        coupling_strengths = np.random.uniform(0.15, 1.2, self.dim)
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended coupling range
                coupling = coupling_strengths[i] * np.sin(x_norm[i]) * np.sin(x_norm[j])  # Changed to sin-sin
                f_val += 0.3 * coupling**3  # Cubic coupling for stronger interactions
        
        # Add a global trend with polynomial terms
        poly_terms = [x_norm[i]**4 for i in range(self.dim)]  # Fourth power
        f_val += 0.15 * sum(poly_terms)
        
        return f_val