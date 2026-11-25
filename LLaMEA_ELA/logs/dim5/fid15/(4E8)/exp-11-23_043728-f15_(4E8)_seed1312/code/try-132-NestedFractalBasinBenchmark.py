import numpy as np

class NestedFractalBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_depth = 4
        self.quantum_coupling = 2.1
        self.nested_scale = 1.7
        self.dynamic_exponent = 3.2
        self.interference_modulation = 0.8
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Create nested fractal basin structure with recursive scaling
        basin_positions = []
        for depth in range(self.fractal_depth):
            scale = self.nested_scale ** depth
            positions = np.random.uniform(-1, 1, size=(self.dim, 2**depth))
            basin_positions.append(positions)
        
        # Calculate nested basin attraction fields with quantum coupling
        basin_fields = np.zeros(self.dim)
        for i in range(self.dim):
            distances = np.abs(x_norm[i] - basin_positions[0][i % len(basin_positions[0]), :])
            field = np.sum(np.exp(-distances**self.dynamic_exponent))
            basin_fields[i] = field
        
        # Add quantum interference patterns with multiple coupling strengths
        quantum_pattern = np.zeros(self.dim)
        for i in range(self.dim):
            coupling_strength = self.quantum_coupling * (1.0 + 0.5 * np.sin(i * 0.7))
            quantum_pattern[i] = np.sin(x_norm[i] * coupling_strength) * \
                               np.cos(x_norm[i] * coupling_strength * 1.3) * \
                               np.sin(x_norm[i] * coupling_strength * 2.1)
        
        # Combine basin and quantum components
        combined = basin_fields + quantum_pattern
        
        # Apply dynamic dimension scaling factor
        dim_scale = 1.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * 0.5)
        
        # Add higher-order polynomial terms for increased ruggedness
        poly_term = np.sum(combined**5) + 0.4 * np.sum(combined**7)
        
        # Introduce nested interference effects with chaotic modulation
        interference = self.interference_modulation * np.sum(np.sin(4.0 * x_norm) * np.cos(3.0 * x_norm))
        
        # Add adaptive penalty for dimensionality and solution distribution
        penalty = 0.15 * self.dim * (np.std(x_norm)**2.0 + 0.08 * np.mean(np.abs(x_norm)))
        
        # Final fitness with nested scaling
        return dim_scale * (poly_term + interference + penalty)