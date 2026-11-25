import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal recursive tangent interactions with multi-scale resonance
        fractal_tan = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.7 * np.sin(0.15 * i)  # Increased frequency modulation
            for j in range(i+1, min(i+5, self.dim)):  # Extended cross-term interaction
                distance = np.abs(x[i] - x[j])
                fractal_tan += np.tan(freq_mod * np.pi * (x[i] + x[j])) * np.exp(-0.15 * distance) * np.cos(0.3 * distance)
        
        # Self-similar basin structures with adaptive scaling and phase shifts
        basin_structure = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.cos(0.25 * i)  # Increased scaling
            phase_shift = 0.1 * np.sin(0.1 * i)
            basin_structure += scale_factor * np.sin(0.6 * x[i] + phase_shift) ** 2 * np.exp(-0.07 * x[i]**2)
        
        # Logarithmic barrier penalties with nested complexity and dynamic scaling
        log_barrier = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 3.5:  # Increased barrier threshold
                penalty_scale = 1.0 + 0.3 * np.sin(0.15 * i)  # Enhanced penalty scaling
                log_barrier += penalty_scale * np.log(1 + np.abs(x[i]) - 3.5) * np.exp(-0.12 * x[i]**2)
        
        # Recursive sine-wave interactions with exponential decay and dynamic phases
        recursive_sine = 0.0
        amplitude = 1.5  # Increased base amplitude
        phase_shift = 0.0
        for i in range(self.dim):
            phase_shift += 0.15 * np.cos(0.07 * i)  # Increased phase modulation
            recursive_sine += amplitude * np.sin(2 ** (i+1) * x[i] + phase_shift) * np.exp(-0.03 * i)
            amplitude *= 0.75  # Slightly faster decay
        
        # Mixed polynomial-trigonometric interactions with dynamic exponents and coefficients
        mixed_interaction = 0.0
        for i in range(self.dim):
            coef = 1.2 + 0.2 * np.sin(0.15 * i)  # Increased coefficient variation
            exponent = 3.5 + 0.5 * np.cos(0.1 * i)  # Dynamic exponent
            mixed_interaction += coef * ((x[i] ** exponent) * np.cos(exponent * x[i]) + (x[i] ** 2) * np.sin(2 * x[i]))
        
        # Multi-scale Gaussian peaks with enhanced width variation and dynamic centers
        gaussian_peaks = 0.0
        for i in range(0, self.dim, 3):  # Every third dimension
            if i < self.dim:
                peak_center = 3.0 * np.sin(i) + 0.7 * np.cos(0.15 * i)  # Enhanced center position
                width = 0.7 + 0.4 * np.cos(i)  # Increased width variation
                height = 1.5 + 0.6 * np.sin(i) + 0.3 * np.tan(0.07 * i)  # Enhanced height
                gaussian_peaks += height * np.exp(-0.5 * ((x[i] - peak_center) ** 2) / (width ** 2))
        
        # Cross-term exponential attraction basins with enhanced coupling and dynamic strengths
        cross_attraction = 0.0
        strength = 1.5  # Increased base strength
        coupling_factor = 1.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j]) ** 2 + 1e-8)
                coupling_factor = 1.0 + 0.2 * np.sin(0.07 * (i + j))  # Enhanced coupling
                cross_attraction += strength * coupling_factor * np.exp(-dist) * np.cos(4 * dist)
                strength *= 0.93  # Slightly faster decay
        
        # Novel resonance interactions between dimensions with dynamic frequency bands
        resonance_interaction = 0.0
        for i in range(self.dim):
            freq_band = 2.0 + 1.5 * np.sin(0.1 * i)
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                resonance_interaction += np.sin(freq_band * dist) * np.cos(freq_band * (x[i] + x[j])) * np.exp(-0.05 * dist**2)
        
        # Combined fitness with adjusted weights and dynamic scaling
        total = 0.3 * fractal_tan + 0.25 * basin_structure + 0.2 * log_barrier + 0.15 * recursive_sine + 0.12 * mixed_interaction + 0.08 * gaussian_peaks + 0.07 * cross_attraction + 0.03 * resonance_interaction
        
        # Add a more chaotic component for enhanced multimodality
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(15 * x[i]) * np.cos(9 * x[i]) * np.exp(-0.02 * x[i]**2)
        
        return total + 0.08 * chaotic_component