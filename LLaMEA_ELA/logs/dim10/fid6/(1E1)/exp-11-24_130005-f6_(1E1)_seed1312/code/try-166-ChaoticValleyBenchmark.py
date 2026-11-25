import numpy as np

class ChaoticValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sinusoidal oscillation component with varying frequencies
        sin_component = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.3)
            amp = 1.0 + 0.2 * np.cos(i * 0.4)
            sin_component += amp * np.sin(freq * x_scaled[i] * 2.0) * np.cos(freq * x_scaled[i])
        
        # Radial basis function with multiple centers
        rbf_component = 0.0
        num_centers = min(5, self.dim)
        for i in range(num_centers):
            center = np.sin(i * 0.8) * 0.7
            width = 0.5 + 0.3 * np.cos(i * 0.6)
            rbf_component += np.exp(-width * (x_scaled[i] - center)**2)
        
        # Cross-dimensional coupling with chaotic interaction
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if j < i + 3:  # Limited coupling
                    coupling_strength = 0.5 + 0.3 * np.sin(i * 0.5)
                    coupling_component += coupling_strength * np.sin(x_scaled[i] * x_scaled[j] * 3.0)
        
        # Chaotic attractor component with logistic map behavior
        chaotic_component = 0.0
        for i in range(self.dim):
            # Logistic-like behavior with parameter control
            param = 3.8 + 0.2 * np.sin(i * 0.4)
            chaotic_component += np.sin(param * x_scaled[i] * (1.0 - x_scaled[i]**2))
        
        # Multi-scale harmonic component
        harmonic_component = 0.0
        for scale in [1, 2, 3]:
            for i in range(self.dim):
                harmonic_component += np.sin(scale * x_scaled[i]) * np.cos(scale * x_scaled[i] * 0.5)
        
        # Combined function with adjusted weights
        return 0.8 * sin_component + 1.2 * rbf_component + 0.6 * coupling_component + 0.4 * chaotic_component + 0.3 * harmonic_component