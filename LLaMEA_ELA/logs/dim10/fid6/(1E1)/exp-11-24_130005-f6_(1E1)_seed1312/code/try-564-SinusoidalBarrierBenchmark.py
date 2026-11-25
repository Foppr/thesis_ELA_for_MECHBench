import numpy as np

class SinusoidalBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with sinusoidal modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial = 2.0 * np.sin(3.0 * r) * np.exp(-0.5 * r**2)
        
        # Multi-periodic angular components
        angular = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim])
            angular += np.sin(7.0 * angle + 2.0 * r) * np.cos(5.0 * angle - 3.0 * r)
        
        # Exponential barrier terms with periodic positioning
        barriers = 0.0
        for i in range(self.dim):
            # Multiple exponential barriers with sinusoidal positions
            barrier_pos = 0.5 * np.sin(i * 1.2) + 0.3 * np.cos(i * 0.8)
            barrier_width = 0.2 + 0.1 * np.sin(i * 0.5)
            barriers += np.exp(-0.5 * ((x_scaled[i] - barrier_pos) / barrier_width)**2)
        
        # Cross-term interactions with periodic modulation
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Periodic interaction weights based on angular distance
                angle_diff = np.abs(np.arctan2(x_scaled[i], x_scaled[j]) - np.arctan2(x_scaled[j], x_scaled[i]))
                weight = 1.5 + 0.8 * np.sin(angle_diff * 3.0)
                cross_terms += weight * x_scaled[i] * x_scaled[j] * np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Global scaling and combination
        return 1.5 * radial + 2.0 * angular + 1.2 * barriers + 0.8 * cross_terms