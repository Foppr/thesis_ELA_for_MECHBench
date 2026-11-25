import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with hyperbolic tangents and quantum interference
        chaotic_component = 0.0
        for i in range(self.dim):
            # Quantum-like phase modulation with hyperbolic tangent
            phase = np.tanh(17 * x[i]) * np.cos(11 * x[i])
            # Interference pattern with dynamic amplitude
            amplitude = 1.0 + 0.3 * np.sin(0.2 * i) * np.tanh(0.5 * x[i])
            chaotic_component += amplitude * phase * np.exp(-0.02 * x[i]**2)
        
        # Fractal recursive tangent interactions with self-similar patterns and dynamic frequency modulation
        fractal_tan = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.7 * np.tanh(0.15 * i)  # Enhanced frequency modulation with tanh
            for j in range(i+1, min(i+5, self.dim)):  # Extended cross-term interaction
                fractal_tan += np.tan(freq_mod * np.pi * (x[i] + x[j])) * np.exp(-0.1 * np.abs(x[i] - x[j]))
        
        # Self-similar basin structures with varying depths and adaptive scaling
        basin_structure = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.tanh(0.25 * i)
            basin_structure += scale_factor * np.sin(0.5 * x[i]) ** 2 * np.exp(-0.05 * x[i]**2)
        
        # Logarithmic barrier penalties with nested complexity and adaptive scaling
        log_barrier = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 3.0:
                penalty_scale = 1.0 + 0.3 * np.tanh(0.1 * i)
                log_barrier += penalty_scale * np.log(1 + np.abs(x[i]) - 3.0) * np.exp(-0.1 * (x[i] ** 2))
        
        # Recursive sine-wave interactions with diminishing amplitudes and dynamic phases
        recursive_sine = 0.0
        amplitude = 1.0
        phase_shift = 0.0
        for i in range(self.dim):
            phase_shift += 0.15 * np.tanh(0.05 * i)  # Enhanced phase modulation
            recursive_sine += amplitude * np.sin(2 ** i * x[i] + phase_shift) * np.exp(-0.02 * i)
            amplitude *= 0.75  # Diminishing amplitude
        
        # Mixed polynomial-trigonometric interactions with adaptive exponents and dynamic coefficients
        mixed_interaction = 0.0
        for i in range(self.dim):
            coef = 1.0 + 0.2 * np.tanh(0.1 * i)
            mixed_interaction += coef * ((x[i] ** 3) * np.cos(3 * x[i]) + (x[i] ** 2) * np.sin(2 * x[i]))
        
        # Multi-scale Gaussian peaks with varying widths, heights, and dynamic center positions
        gaussian_peaks = 0.0
        for i in range(0, self.dim, 2):  # Every other dimension
            if i < self.dim:
                peak_center = 2.5 * np.tanh(i) + 0.5 * np.cos(0.1 * i)  # Dynamic center position with tanh
                width = 0.5 + 0.4 * np.tanh(i)
                height = 1.0 + 0.6 * np.sin(i) + 0.3 * np.tanh(0.05 * i)  # Dynamic height
                gaussian_peaks += height * np.exp(-0.5 * ((x[i] - peak_center) ** 2) / (width ** 2))
        
        # Cross-term exponential attraction basins with varying strengths and dynamic coupling
        cross_attraction = 0.0
        strength = 1.0
        coupling_factor = 1.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j]) ** 2 + 1e-8)
                coupling_factor = 1.0 + 0.15 * np.tanh(0.05 * (i + j))  # Enhanced coupling with tanh
                cross_attraction += strength * coupling_factor * np.exp(-dist) * np.cos(3 * dist)
                strength *= 0.92  # Slight decay
        
        # Combined fitness with adjusted weights and dynamic scaling
        total = 0.25 * fractal_tan + 0.2 * basin_structure + 0.15 * log_barrier + 0.15 * recursive_sine + 0.1 * mixed_interaction + 0.08 * gaussian_peaks + 0.07 * cross_attraction
        
        # Enhanced chaotic component with quantum interference and scale-free properties
        enhanced_chaos = 0.0
        for i in range(self.dim):
            # Scale-free chaotic dynamics with hyperbolic tangent
            chaos_term = np.tanh(23 * x[i]) * np.sin(19 * x[i]) * np.exp(-0.015 * x[i]**2)
            enhanced_chaos += chaos_term
        
        return total + 0.1 * chaotic_component + 0.05 * enhanced_chaos