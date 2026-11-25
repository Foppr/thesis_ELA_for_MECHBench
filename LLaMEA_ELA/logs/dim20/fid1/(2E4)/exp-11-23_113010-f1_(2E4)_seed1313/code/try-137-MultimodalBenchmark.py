import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced nested fractal exponential interactions with improved modulation
        fractal_interaction = 0.0
        for i in range(self.dim):
            base = np.exp(-np.abs(x_norm[i]))
            modulator = np.sin(2**(i+1) * np.pi * x_norm[i])
            nested_mod = np.cos(3**(i+1) * np.pi * x_norm[i])
            # Add improved fractal scaling
            scale = 1.0 + 0.3 * np.sin(i * np.pi / self.dim)
            fractal_interaction += base * modulator * nested_mod * scale
        
        # Enhanced dynamic phase-coupled chaotic components
        phase_coupling = 0.0
        for i in range(self.dim):
            # Improved frequency adaptation with better distribution
            freq_i = 2**(i % 4 + 1) * (1 + 0.15 * np.sin(i * np.pi / self.dim))
            freq_j = 3**(i % 5 + 1) * (1 + 0.2 * np.cos(i * np.pi / self.dim))
            # Add improved coupling with amplitude modulation
            amp_mod = 1.0 + 0.2 * np.sin(2 * i * np.pi / self.dim)
            coupling_term = amp_mod * np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[i]**2)
            phase_coupling += coupling_term
        
        # Refined adaptive basin geometry with better dimension scaling
        adaptive_basin = 0.0
        for i in range(self.dim):
            # Improved scale factor with more controlled variation
            scale_factor = 1.0 + 0.4 * np.sin(self.dim * x_norm[i] / 2)
            power_factor = 1.0 + 0.2 * np.cos(self.dim * x_norm[i] / 3)
            # Add improved basin term with better control
            basin_term = np.exp(-np.abs(x_norm[i])**power_factor) * scale_factor
            adaptive_basin += basin_term
        
        # Enhanced multi-scale periodic potential with better frequency distribution
        periodic_potential = 0.0
        for i in range(self.dim):
            # Improved frequency nesting with better spacing
            freq_base = 2**(i % 6 + 1)
            freq_mod = np.sin(i * np.pi / self.dim) * np.cos(i * np.pi / (self.dim + 2))
            effective_freq = freq_base * (1 + 0.15 * freq_mod)
            # Add improved periodic term with better balance
            periodic_potential += np.sin(effective_freq * x_norm[i]) * np.cos(effective_freq * x_norm[i]**3) * (1 + 0.1 * np.sin(i * np.pi / self.dim))
        
        # Enhanced recursive chaotic gradient with better memory effects
        recursive_grad = 0.0
        for i in range(self.dim):
            # Improved memory effect from previous dimensions with better weighting
            memory_effect = np.sum([np.sin(2**(j+1) * np.pi * x_norm[j]) * (1 + 0.1 * np.cos(j * np.pi / self.dim)) for j in range(i)])
            # Add improved chaotic component with better normalization
            chaotic_component = np.cos(3**(i+1) * np.pi * x_norm[i]) * memory_effect * (1 + 0.05 * np.sin(i * np.pi / self.dim))
            recursive_grad += chaotic_component
        
        # Improved weight adaptation with better balance and reduced complexity
        weight_fractal = 0.7 + 0.15 * np.sin(self.dim * np.pi / 8)
        weight_phase = 0.5 + 0.25 * np.cos(self.dim * np.pi / 6)
        weight_basin = 0.6 + 0.2 * np.sin(self.dim * np.pi / 4)
        weight_periodic = 0.6 + 0.18 * np.cos(self.dim * np.pi / 5)
        weight_recursive = 0.3 + 0.15 * np.sin(self.dim * np.pi / 3)
        
        return (weight_fractal * fractal_interaction + 
                weight_phase * phase_coupling + 
                weight_basin * adaptive_basin + 
                weight_periodic * periodic_potential + 
                weight_recursive * recursive_grad)