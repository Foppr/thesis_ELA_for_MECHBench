import numpy as np

class ChaoticFractalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters
        self.logistic_r = 3.9 + np.random.rand(dim) * 0.1
        self.fractal_exponents = 0.5 + np.random.rand(dim) * 1.5
        self.scale_factors = 1.0 + np.random.rand(dim) * 2.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map component for chaotic behavior
        logistic = 0.0
        for i in range(self.dim):
            # Initialize chaotic sequence
            chaotic_val = 0.5
            for _ in range(10):  # Iterate to reach chaotic regime
                chaotic_val = self.logistic_r[i] * chaotic_val * (1 - chaotic_val)
            logistic += chaotic_val * np.sin(x[i] * np.pi)
        
        # Radial basis function with dynamic centers and widths
        rbf = 0.0
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0.0
            width = 0.5 + 0.5 * np.sin(i * 0.7)
            rbf += np.exp(-0.5 * ((x[i] - center) / width) ** 2)
        
        # Fractal-like oscillation with multi-scale interference
        fractal = 0.0
        for i in range(self.dim):
            scale = self.scale_factors[i]
            exponent = self.fractal_exponents[i]
            # Multi-scale oscillation
            oscillation = 0.0
            for freq in [1.0, 2.0, 4.0]:
                oscillation += np.sin(freq * x[i] * scale) * (1.0 / (freq ** exponent))
            fractal += oscillation
        
        # Cross-dimensional interaction with dynamic coupling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin((x[i] + x[j]) * 0.5) * np.cos((x[i] - x[j]) * 0.3)
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross += coupling * np.exp(-dist * 0.1)
        
        # Multi-scale peak structure with varying amplitudes
        peaks = 0.0
        peak_positions = np.linspace(-4.5, 4.5, 9)
        for pos in peak_positions:
            for i in range(self.dim):
                width = 0.3 + 0.7 * np.cos(i * 0.5)
                height = 1.0 + 0.5 * np.sin(i * 0.3)
                peaks += height * np.exp(-0.5 * ((x[i] - pos) / width) ** 4)
        
        # Dynamic conditioning based on position
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (1.0 + 0.5 * np.sin(x[i] * 0.2)) * x[i]**2
        
        # Combine all components with varying weights
        weights = np.array([0.6, 0.8, 0.7, 0.5, 0.9, 0.4])
        components = np.array([logistic, rbf, fractal, cross, peaks, conditioning])
        return np.sum(weights * components)