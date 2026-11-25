import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Exponential decay components with varying rates and amplitudes
        self.decay_rates = 0.5 + 4.0 * np.random.rand(dim)
        self.decay_amplitudes = 1.0 + 3.0 * np.random.rand(dim)
        # Trigonometric wave interference with multiple frequencies and phases
        self.wave_frequencies = 2.0 + 8.0 * np.random.rand(dim)
        self.wave_phases = 2.0 * np.pi * np.random.rand(dim)
        self.wave_amplitudes = 0.5 + 2.5 * np.random.rand(dim)
        # Radial basis function centers and widths
        self.rbf_centers = 4.0 * np.random.rand(dim, 10) - 2.0
        self.rbf_widths = 0.2 + 1.8 * np.random.rand(10)
        # Adaptive conditioning with exponential scaling
        self.conditioning_exponents = 1.0 + 4.0 * np.random.rand(dim)
        self.conditioning_factors = 0.5 + 2.0 * np.random.rand(dim)
        # Global rotation matrix for orientation effects
        angle = np.pi * np.random.rand()
        self.rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay component
        decay_sum = 0.0
        for i in range(self.dim):
            decay_sum += self.decay_amplitudes[i] * np.exp(-self.decay_rates[i] * np.abs(x_norm[i]))
        
        # Trigonometric wave interference
        wave_sum = 0.0
        for i in range(self.dim):
            wave_sum += self.wave_amplitudes[i] * np.sin(self.wave_frequencies[i] * x_norm[i] + self.wave_phases[i])
        
        # Radial basis function component
        rbf_sum = 0.0
        for k in range(10):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.rbf_centers[i, k])**2
            rbf_sum += np.exp(-dist / (2.0 * self.rbf_widths[k]**2))
        
        # Adaptive conditioning component
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += self.conditioning_factors[i] * (np.exp(self.conditioning_exponents[i] * np.abs(x_norm[i])) - 1.0)
        
        # Combine all components with weighted contributions
        result = 0.25 * decay_sum + 0.30 * wave_sum + 0.20 * rbf_sum + 0.25 * cond_sum
        
        # Add rotation effects for higher dimensions
        if self.dim >= 2:
            rotated = np.dot(self.rotation_matrix, x_norm[:2])
            result += 0.10 * (rotated[0]**3 + rotated[1]**3)
        
        # Penalty term with exponential scaling to discourage boundary violations
        penalty = 0.15 * np.sum(np.exp(2.0 * np.abs(x_norm)) - 1.0)
        
        return result + penalty