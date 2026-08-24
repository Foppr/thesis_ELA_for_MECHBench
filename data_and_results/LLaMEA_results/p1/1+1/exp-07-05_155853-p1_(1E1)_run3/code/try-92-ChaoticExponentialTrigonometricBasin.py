import numpy as np

class ChaoticExponentialTrigonometricBasin:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic exponential decay components with varying rates
        exp_decay_sum = 0
        for i in range(self.dim):
            rate = 0.5 + 0.5 * np.sin(i * 0.6 + 1.0)
            exp_decay_sum += np.exp(-rate * np.abs(x[i])) * np.cos(rate * x[i]**2)
        
        # Trigonometric wave interference with dynamic amplitudes and frequencies
        wave_sum = 0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 0.8)
            freq = 2.0 + 1.5 * np.cos(i * 0.4)
            wave_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Adaptive parabolic basins with chaotic positioning and scaling
        basin_sum = 0
        for i in range(min(8, self.dim)):
            center = -4.0 + 8.0 * (i / max(1, self.dim - 1)) + 0.3 * np.sin(i * 1.2)
            scale = 0.5 + 0.5 * np.abs(np.cos(i * 0.7))
            basin_sum += scale * (x[i] - center)**2
        
        # Coupled higher-order polynomial terms with chaotic interaction weights
        poly_coupling = 0
        for i in range(self.dim - 1):
            weight = 0.7 + 0.3 * np.sin(i * 0.5)
            poly_coupling += weight * (x[i]**4 + x[i+1]**3) + (1.0 - weight) * (x[i]**2 * x[i+1]**2)
        
        # Complex chaotic oscillation with multiple frequencies and damping
        oscillation = 0
        for i in range(self.dim):
            freq1 = 1.0 + 0.3 * np.sin(i * 0.9)
            freq2 = 0.5 + 0.5 * np.cos(i * 0.6)
            damping = 0.8 + 0.2 * np.sin(i * 0.4)
            oscillation += damping * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]**2)
        
        # Cross-dimensional coupling with chaotic interaction matrix
        cross_coupling = 0
        for i in range(self.dim - 2):
            for j in range(i+1, self.dim - 1):
                weight = 0.3 + 0.7 * np.sin((i + j) * 0.5)
                cross_coupling += weight * x[i] * x[i+1] * x[j]
        
        # Global chaotic modulation with multiple exponential terms
        global_mod = np.exp(-0.1 * np.sum(np.abs(x))) * np.sin(0.3 * np.sum(x**2)) * np.cos(0.2 * np.sum(x))
        
        # Combine all components with dynamic weights
        return 1.5 * exp_decay_sum + 1.0 * wave_sum + 0.8 * basin_sum + 0.6 * poly_coupling + 0.4 * oscillation + 0.3 * cross_coupling + 0.2 * global_mod