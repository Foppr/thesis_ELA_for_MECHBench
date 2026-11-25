import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested fractal exponential interactions with recursive modulation
        fractal_interaction = 0.0
        for i in range(self.dim):
            base = np.exp(-np.abs(x_norm[i]))
            modulator = np.sin(2**(i+1) * np.pi * x_norm[i])
            nested_mod = np.cos(3**(i+1) * np.pi * x_norm[i])
            fractal_interaction += base * modulator * nested_mod
        
        # Dynamic phase-coupled chaotic components with adaptive frequencies
        phase_coupling = 0.0
        for i in range(self.dim):
            freq_i = 2**(i % 3 + 1) * (1 + 0.1 * np.sin(i * np.pi / self.dim))
            freq_j = 3**(i % 4 + 1) * (1 + 0.15 * np.cos(i * np.pi / self.dim))
            coupling_term = np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[i]**2)
            phase_coupling += coupling_term
        
        # Adaptive basin geometry with dimension-dependent scaling and non-linear transforms
        adaptive_basin = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(self.dim * x_norm[i])
            power_factor = 1.0 + 0.3 * np.cos(self.dim * x_norm[i])
            basin_term = np.exp(-np.abs(x_norm[i])**power_factor) * scale_factor
            adaptive_basin += basin_term
        
        # Multi-scale periodic potential with recursive frequency nesting and chaotic mixing
        periodic_potential = 0.0
        for i in range(self.dim):
            freq_base = 2**(i % 5 + 1)
            freq_mod = np.sin(i * np.pi / self.dim) * np.cos(i * np.pi / (self.dim + 1))
            effective_freq = freq_base * (1 + 0.2 * freq_mod)
            periodic_potential += np.sin(effective_freq * x_norm[i]) * np.cos(effective_freq * x_norm[i]**3)
        
        # Recursive chaotic gradient with memory effects and temporal-like dimension coupling
        recursive_grad = 0.0
        for i in range(self.dim):
            # Memory effect from previous dimensions
            memory_effect = np.sum([np.sin(2**(j+1) * np.pi * x_norm[j]) for j in range(i)])
            chaotic_component = np.cos(3**(i+1) * np.pi * x_norm[i]) * memory_effect
            recursive_grad += chaotic_component
        
        # Combined landscape with dynamic weight adaptation based on dimensionality and input characteristics
        weight_fractal = 0.8 + 0.2 * np.sin(self.dim * np.pi / 6)
        weight_phase = 0.6 + 0.4 * np.cos(self.dim * np.pi / 4)
        weight_basin = 0.5 + 0.3 * np.sin(self.dim * np.pi / 3)
        weight_periodic = 0.7 + 0.3 * np.cos(self.dim * np.pi / 5)
        weight_recursive = 0.4 + 0.2 * np.sin(self.dim * np.pi / 2)
        
        return (weight_fractal * fractal_interaction + 
                weight_phase * phase_coupling + 
                weight_basin * adaptive_basin + 
                weight_periodic * periodic_potential + 
                weight_recursive * recursive_grad)