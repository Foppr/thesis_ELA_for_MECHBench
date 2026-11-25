import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute delay parameters for time-delayed dynamics
        self.delays = np.linspace(0.1, 2.0, min(dim, 10))
        # Precompute sine modulation frequencies
        self.freqs = np.linspace(0.5, 3.0, min(dim, 10))
        # Adaptive basin weights
        self.basin_weights = np.random.rand(min(dim, 10)) * 2.0 + 1.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Time-delayed gradient component with chaotic feedback
        delayed = 0.0
        for i in range(self.dim):
            if i >= len(self.delays):
                break
            delay_idx = max(0, i - int(self.delays[i % len(self.delays)] * 5))
            feedback = x[delay_idx] if delay_idx < self.dim else 0.0
            delayed += np.sin(x[i] + 0.5 * feedback) * (1.0 + 0.2 * np.cos(0.3 * x[i]))
        
        # Hyperbolic sine modulation with dynamic amplitude
        sinh_mod = 0.0
        for i in range(self.dim):
            if i >= len(self.freqs):
                break
            amp = 1.5 + 0.5 * np.sin(0.2 * i + self.dim * 0.1)
            sinh_mod += amp * np.sinh(0.5 * x[i] * self.freqs[i % len(self.freqs)])
        
        # Adaptive basin connectivity with dynamic scaling
        basins = 0.0
        for i in range(self.dim):
            if i >= len(self.basin_weights):
                break
            # Create multiple overlapping basins with varying depths
            basin_depth = self.basin_weights[i % len(self.basin_weights)]
            center = -3.0 + 6.0 * (i / max(1, self.dim - 1))
            distance = np.abs(x[i] - center)
            # Basin with exponential decay and adaptive scaling
            basins += basin_depth * np.exp(-0.5 * (distance / (1.0 + 0.1 * i))**2)
        
        # Dynamic ridge structure with varying curvature
        ridges = 0.0
        for i in range(self.dim):
            # Varying ridge sharpness and position
            sharpness = 0.8 + 0.4 * np.sin(0.4 * i + self.dim * 0.2)
            position = -2.5 + 5.0 * (i / max(1, self.dim - 1))
            # Ridge with dynamic curvature
            ridges += sharpness * np.tanh(2.0 * (x[i] - position))**2
        
        # Asymmetric oscillatory component with phase coupling
        oscillatory = 0.0
        for i in range(self.dim):
            if i >= len(self.freqs):
                break
            freq = self.freqs[i % len(self.freqs)]
            phase = 0.3 * np.sin(0.5 * i + self.dim * 0.1)
            oscillatory += np.cos(freq * x[i] + phase) * np.sin(freq * x[i]**2)
        
        # Combine all components with dynamic weighting based on dimension
        dim_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        return (0.25 * delayed + 0.30 * sinh_mod + 
                0.20 * basins + 0.15 * ridges + 0.10 * oscillatory) * dim_factor