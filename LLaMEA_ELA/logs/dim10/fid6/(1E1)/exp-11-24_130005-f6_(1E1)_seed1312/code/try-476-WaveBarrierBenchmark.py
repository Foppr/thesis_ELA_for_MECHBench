import numpy as np

class WaveBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with multiple concentric barriers
        r = np.sqrt(np.sum(x_scaled**2))
        
        # Logarithmic barrier terms that become increasingly steep
        barrier = 0.0
        for i in range(1, 6):
            barrier += np.exp(-i * r) * np.sin(i * np.pi * r) / (i * (1 + r))
        
        # Wave interference pattern with multiple frequencies and phases
        wave = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.01)
                wave += np.sin(3.0 * dist) * np.cos(2.0 * dist) / (1.0 + dist**2)
        
        # Periodic radial modulation with varying amplitudes
        periodic = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim])
            periodic += np.sin(5.0 * angle) * np.cos(4.0 * angle) * (1.0 + 0.5 * np.sin(3.0 * r))
        
        # Multi-scale harmonic components with exponential decay
        harmonic = 0.0
        for scale in [1, 2, 3, 4]:
            for i in range(self.dim):
                harmonic += np.sin(scale * x_scaled[i]) * np.cos(scale * x_scaled[i] * 0.7) * \
                           np.exp(-scale * r**2)
        
        # Combined function with carefully balanced weights
        return 1.5 * barrier + 2.0 * wave + 1.3 * periodic + 0.8 * harmonic