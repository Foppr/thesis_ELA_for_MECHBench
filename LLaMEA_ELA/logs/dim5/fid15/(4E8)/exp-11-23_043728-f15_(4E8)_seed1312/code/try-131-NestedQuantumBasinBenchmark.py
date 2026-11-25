import numpy as np

class NestedQuantumBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.basin_levels = 4
        self.fractal_depth = 3.2
        self.quantum_coupling = 2.1
        self.dynamic_scaling = 1.5
        self.ruggedness_factor = 2.8
        self.chaotic_modulation = 0.8
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Create nested fractal basin structure with multiple hierarchical levels
        basin_centers = []
        for level in range(self.basin_levels):
            level_centers = np.random.uniform(-0.9, 0.9, self.dim)
            basin_centers.append(level_centers)
        
        # Calculate multi-level basin attraction fields with nested fractal scaling
        basin_fields = np.zeros(self.dim)
        for level in range(self.basin_levels):
            level_centers = basin_centers[level]
            distances = np.abs(x_norm - level_centers)
            strength = 1.0 / (level + 1.0)**self.fractal_depth
            basin_fields += strength * np.exp(-distances**(1.5 + self.fractal_depth))
        
        # Add quantum interference patterns with coupling between dimensions
        quantum_pattern = np.zeros(self.dim)
        for i in range(self.dim):
            coupling_strength = self.quantum_coupling * np.sin(x_norm[i] * (i + 1) * 0.7)
            quantum_pattern[i] = np.sin(x_norm[i] * 2.0) * np.cos(x_norm[i] * 3.0) * coupling_strength
        
        # Combine basin and quantum components with dynamic scaling
        combined = basin_fields + self.dynamic_scaling * quantum_pattern
        
        # Add higher-order polynomial terms for increased ruggedness
        poly_term = np.sum(combined**5) + self.ruggedness_factor * np.sum(combined**7)
        
        # Introduce chaotic modulation with nested sine waves
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(2.0**(i+1) * x_norm[i]) * np.cos(3.0**(i+1) * x_norm[i])
        
        # Add dynamic penalty based on solution distribution and dimensionality
        penalty = 0.2 * self.dim * (np.std(x_norm)**2.0 + 0.1 * np.mean(np.abs(x_norm)))
        
        # Apply chaotic modulation to the final fitness value
        final_fitness = poly_term + self.chaotic_modulation * chaotic_mod + penalty
        
        # Add dimension-dependent scaling factor for dynamic difficulty adjustment
        scale_factor = 1.0 + 0.03 * np.log(self.dim + 1) + 0.02 * np.cos(self.dim * 0.8)
        
        return scale_factor * final_fitness