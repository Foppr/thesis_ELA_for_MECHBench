import numpy as np

class NestedHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Hierarchical frequency structure with nested harmonics
        self.base_frequencies = 1.0 + np.arange(dim) * 0.5
        self.harmonic_multipliers = np.random.uniform(1.0, 3.0, dim)
        # Dynamic phase shifts that adapt based on dimension
        self.phase_offsets = np.random.uniform(0, 2*np.pi, dim)
        # Nested energy well structure with varying depths
        self.well_depths = np.random.uniform(0.5, 3.0, dim)
        self.well_widths = np.random.uniform(0.5, 2.0, dim)
        # Adaptive modulation parameters for frequency scaling
        self.modulation_strength = np.random.uniform(0.1, 1.0, dim)
        self.modulation_frequency = np.random.uniform(0.5, 2.0, dim)
        # Multi-scale interaction coefficients
        self.interaction_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i != j:
                    self.interaction_matrix[i, j] = np.random.uniform(-0.5, 0.5) * np.exp(-abs(i-j)/max(1, dim/4))
        
        # Saddle-point structure to increase conditioning complexity
        self.saddle_positions = np.random.uniform(-1.0, 1.0, (dim, 3))
        self.saddle_strengths = np.random.uniform(0.5, 2.0, (dim, 3))
        self.saddle_widths = np.random.uniform(0.3, 1.0, (dim, 3))

    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1] for harmonic computation
        normalized_x = x / 5.0
        
        # Compute nested harmonic components
        harmonic_sum = np.zeros(self.dim)
        for i in range(self.dim):
            # Base harmonic with adaptive frequency
            freq = self.base_frequencies[i] * self.harmonic_multipliers[i]
            phase = self.phase_offsets[i] + self.modulation_strength[i] * np.sin(self.modulation_frequency[i] * normalized_x[i])
            
            # Multi-scale harmonic structure with interaction terms
            harmonic_sum[i] = (
                np.sin(freq * normalized_x[i] + phase) +
                0.5 * np.sin(2 * freq * normalized_x[i] + phase) +
                0.3 * np.sin(3 * freq * normalized_x[i] + phase)
            )
            
            # Add interaction effects from other dimensions
            for j in range(self.dim):
                if i != j:
                    harmonic_sum[i] += self.interaction_matrix[i, j] * np.cos(freq * normalized_x[j])
        
        # Compute nested energy wells with varying depths and widths
        well_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Multi-scale well structure
            well_value = 0.0
            for depth, width in zip(self.well_depths[i:i+3], self.well_widths[i:i+3]):
                if len(self.well_depths) > i+2:
                    well_value += depth * np.exp(-((normalized_x[i] - 1.0)**2) / (2 * width**2)) + \
                                 depth * np.exp(-((normalized_x[i] + 1.0)**2) / (2 * width**2))
            well_values[i] = well_value
        
        # Add saddle-point structures for increased complexity
        saddle_values = np.zeros(self.dim)
        for i in range(self.dim):
            for j in range(3):
                saddle_values[i] += self.saddle_strengths[i, j] * np.exp(-((normalized_x[i] - self.saddle_positions[i, j])**2) / (2 * self.saddle_widths[i, j]**2))
        
        # Combine harmonic, well, and saddle components
        fitness = 0.0
        for i in range(self.dim):
            combined_component = harmonic_sum[i] + well_values[i] - saddle_values[i]
            # Add nonlinearity with polynomial terms
            fitness += (combined_component**2 + 
                       0.3 * combined_component**3 + 
                       0.1 * combined_component**4)
        
        # Add hierarchical structure with multiple scales
        scale_factor = np.sum(np.abs(normalized_x)**3) / self.dim
        fitness += 0.5 * scale_factor
        
        # Add noise for additional complexity
        noise = np.random.uniform(-0.01, 0.01)
        return fitness + noise