import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency bands for spectral decomposition
        self.freq_bands = np.linspace(1.0, 9.0, min(9, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with varying degree
        result = 0.1 * np.sum(x**4) + 0.3 * np.sum(x**2)
        
        # Spectral decomposition with frequency-dependent damping
        for i in range(self.dim):
            freq = self.freq_bands[min(i, len(self.freq_bands)-1)]
            # Apply damped sinusoidal components
            result += 2.0 * np.sin(freq * x[i]) * np.exp(-0.2 * abs(x[i]))
            result += 1.5 * np.cos(freq * x[i]) * np.exp(-0.1 * abs(x[i]))
        
        # Polynomial chaos expansion with Hermite polynomials
        for i in range(self.dim):
            xi = x[i] / 5.0  # Normalize to [-1, 1]
            # Third-order Hermite polynomial components
            h3 = 2 * xi**3 - xi
            result += 1.2 * h3 * np.sin(2 * i * np.pi / self.dim)
        
        # Adaptive saddle-point potentials with dynamic weights
        for i in range(self.dim):
            # Create a saddle potential with adaptive steepness
            steepness = 1.5 + 0.8 * np.sin(i * np.pi / (self.dim + 1))
            # Saddle potential: x^2 - y^2 type behavior
            result += steepness * (x[i]**2 - 0.3 * np.sin(4 * x[i]))
        
        # Cross-dimensional coupling with spectral filtering
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Frequency-dependent coupling strength
                coupling_strength = 0.7 + 0.5 * np.cos((i+j) * np.pi / (self.dim + 3))
                # Coupling with phase modulation
                phase = np.sin(i * x[j] - j * x[i])
                result += coupling_strength * np.exp(-0.15 * (x[i]**2 + x[j]**2)) * phase
        
        # Multi-scale harmonic oscillations with chaotic amplitude modulation
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            amplitude = 1.2 + 0.6 * np.cos(8 * x[i] + i)
            result += amplitude * np.sin(scale * x[i]) * np.cos(scale * x[i])
        
        # Boundary regularization with spectral filtering
        boundary_penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.6:
                # Apply frequency-dependent penalty scaling
                freq_scale = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
                boundary_penalty += freq_scale * (abs(x[i]) - 4.6)**3
        result += boundary_penalty
        
        # Global conditioning with adaptive scaling factor
        global_conditioning = 1.4 + 0.6 * np.sin(np.sum(x) * np.pi / (self.dim + 2))
        result *= global_conditioning
        
        return result