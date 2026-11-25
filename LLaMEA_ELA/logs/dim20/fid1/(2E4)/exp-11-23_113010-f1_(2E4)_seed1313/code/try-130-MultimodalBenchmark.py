import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal exponential interactions with chaotic modulation and recursive coupling
        fractal_interaction = 0.0
        for i in range(self.dim):
            base = np.exp(-np.abs(x_norm[i])**1.5)
            modulator = np.sin(3**(i+2) * np.pi * x_norm[i] * 0.7)
            nested_mod = np.cos(4**(i+1) * np.pi * x_norm[i] * 1.3)
            fractal_interaction += base * modulator * nested_mod
        
        # Enhanced phase-coupled chaotic components with dynamic frequency modulation and temporal coupling
        phase_coupling = 0.0
        for i in range(self.dim):
            freq_i = 3**(i % 4 + 2) * (1 + 0.15 * np.sin(i * np.pi / self.dim))
            freq_j = 4**(i % 5 + 1) * (1 + 0.2 * np.cos(i * np.pi / (self.dim + 2)))
            coupling_term = np.sin(freq_i * x_norm[i]**1.5) * np.cos(freq_j * x_norm[i]**3)
            phase_coupling += coupling_term
        
        # Enhanced adaptive basin geometry with non-linear scaling and chaotic dimension coupling
        adaptive_basin = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.6 * np.sin(self.dim * x_norm[i] * 1.2)
            power_factor = 1.0 + 0.35 * np.cos(self.dim * x_norm[i] * 0.8)
            basin_term = np.exp(-np.abs(x_norm[i])**power_factor) * scale_factor
            adaptive_basin += basin_term
        
        # Multi-scale periodic potential with enhanced frequency nesting and chaotic mixing
        periodic_potential = 0.0
        for i in range(self.dim):
            freq_base = 3**(i % 6 + 2)
            freq_mod = np.sin(i * np.pi / (self.dim + 1)) * np.cos(i * np.pi / (self.dim + 3))
            effective_freq = freq_base * (1 + 0.2 * freq_mod)
            periodic_potential += np.sin(effective_freq * x_norm[i]**1.3) * np.cos(effective_freq * x_norm[i]**4)
        
        # Enhanced recursive chaotic gradient with memory effects and multi-dimensional temporal coupling
        recursive_grad = 0.0
        for i in range(self.dim):
            # Memory effect from previous dimensions with enhanced chaotic coupling
            memory_effect = np.sum([np.sin(3**(j+2) * np.pi * x_norm[j] * 0.8) for j in range(i)])
            chaotic_component = np.cos(4**(i+1) * np.pi * x_norm[i]) * memory_effect
            recursive_grad += chaotic_component
        
        # Combined landscape with enhanced dynamic weight adaptation based on dimensionality and input characteristics
        weight_fractal = 0.8 + 0.25 * np.sin(self.dim * np.pi / 7)
        weight_phase = 0.6 + 0.35 * np.cos(self.dim * np.pi / 5)
        weight_basin = 0.5 + 0.3 * np.sin(self.dim * np.pi / 4)
        weight_periodic = 0.7 + 0.25 * np.cos(self.dim * np.pi / 6)
        weight_recursive = 0.4 + 0.25 * np.sin(self.dim * np.pi / 3)
        
        return (weight_fractal * fractal_interaction + 
                weight_phase * phase_coupling + 
                weight_basin * adaptive_basin + 
                weight_periodic * periodic_potential + 
                weight_recursive * recursive_grad)