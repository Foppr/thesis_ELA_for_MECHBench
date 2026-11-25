import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal coupling with higher-order exponential interactions
        fractal_interaction = 0.0
        for i in range(self.dim):
            base = np.exp(-np.abs(x_norm[i])**1.5)
            modulator = np.sin(2**(i+2) * np.pi * x_norm[i] * 1.2)
            nested_mod = np.cos(3**(i+2) * np.pi * x_norm[i] * 1.8)
            high_order_term = np.sin(5**(i+1) * np.pi * x_norm[i] * 0.7)
            fractal_interaction += base * modulator * nested_mod * high_order_term
        
        # Dynamic phase-coupled chaotic components with enhanced frequency diversity
        phase_coupling = 0.0
        for i in range(self.dim):
            freq_i = 2**(i % 4 + 2) * (1 + 0.15 * np.sin(i * np.pi / self.dim))
            freq_j = 3**(i % 5 + 2) * (1 + 0.2 * np.cos(i * np.pi / self.dim))
            freq_k = 5**(i % 3 + 1) * (1 + 0.1 * np.sin(i * np.pi / (self.dim + 2)))
            coupling_term = np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[i]**2) * np.sin(freq_k * x_norm[i]**3)
            phase_coupling += coupling_term
        
        # Adaptive basin geometry with enhanced non-linear transforms and multi-scale scaling
        adaptive_basin = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.6 * np.sin(self.dim * x_norm[i])
            power_factor = 1.0 + 0.4 * np.cos(self.dim * x_norm[i])
            non_linear_term = np.exp(-np.abs(x_norm[i])**power_factor) * (1 + 0.3 * np.sin(x_norm[i]**2))
            adaptive_basin += scale_factor * non_linear_term
        
        # Multi-scale periodic potential with enhanced chaotic mixing and frequency nesting
        periodic_potential = 0.0
        for i in range(self.dim):
            freq_base = 2**(i % 6 + 2)
            freq_mod = np.sin(i * np.pi / self.dim) * np.cos(i * np.pi / (self.dim + 2))
            freq_mix = np.sin(3 * i * np.pi / self.dim) * np.cos(2 * i * np.pi / (self.dim + 1))
            effective_freq = freq_base * (1 + 0.25 * freq_mod) * (1 + 0.15 * freq_mix)
            periodic_potential += np.sin(effective_freq * x_norm[i]) * np.cos(effective_freq * x_norm[i]**3) * np.sin(effective_freq * x_norm[i]**2)
        
        # Enhanced recursive chaotic gradient with memory effects and temporal-like dimension coupling
        recursive_grad = 0.0
        for i in range(self.dim):
            # Memory effect from previous dimensions with enhanced coupling
            memory_effect = np.sum([np.sin(3**(j+2) * np.pi * x_norm[j] * 1.1) for j in range(i)])
            chaotic_component = np.cos(4**(i+2) * np.pi * x_norm[i]) * memory_effect * (1 + 0.2 * np.sin(x_norm[i]))
            recursive_grad += chaotic_component
        
        # Combined landscape with enhanced dynamic weight adaptation
        weight_fractal = 0.85 + 0.15 * np.sin(self.dim * np.pi / 5)
        weight_phase = 0.65 + 0.35 * np.cos(self.dim * np.pi / 3)
        weight_basin = 0.55 + 0.45 * np.sin(self.dim * np.pi / 4)
        weight_periodic = 0.75 + 0.25 * np.cos(self.dim * np.pi / 6)
        weight_recursive = 0.45 + 0.55 * np.sin(self.dim * np.pi / 2)
        
        return (weight_fractal * fractal_interaction + 
                weight_phase * phase_coupling + 
                weight_basin * adaptive_basin + 
                weight_periodic * periodic_potential + 
                weight_recursive * recursive_grad)