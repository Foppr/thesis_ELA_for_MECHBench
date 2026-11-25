import numpy as np

class HybridWaveBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basin component with multiple local minima
        radial_basin = 0.1 * np.sum(x**2) + 0.05 * np.sum(np.sin(5.0 * x)**2)
        
        # Periodic wave component with varying frequencies and amplitudes
        periodic_waves = 0.0
        for i in range(self.dim):
            periodic_waves += 3.0 * np.sin(2.0 * x[i]) + \
                              1.5 * np.sin(4.0 * x[i]) + \
                              0.8 * np.sin(7.0 * x[i]) + \
                              0.3 * np.sin(11.0 * x[i])
            
        # Cross-dimensional coupling with interaction terms
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += 0.5 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) + \
                                 0.3 * np.cos(2.0 * x[i]) * np.sin(2.0 * x[j])
        
        # Multi-scale sinusoidal interference patterns
        interference = 0.0
        for i in range(self.dim):
            interference += 2.0 * np.sin(10.0 * x[i] + 0.5 * np.sin(3.0 * x[i])) + \
                           1.0 * np.cos(8.0 * x[i] + 0.3 * np.cos(4.0 * x[i]))
        
        # Polynomial smoothing with higher-order terms
        polynomial_smooth = 0.1 * np.sum(x**3) + 0.05 * np.sum(x**4)
        
        # Adaptive noise component with dynamic amplitude modulation
        adaptive_noise = 0.0
        for i in range(self.dim):
            adaptive_noise += 0.2 * np.sin(15.0 * x[i]) * np.cos(12.0 * x[i]) + \
                             0.1 * np.sin(18.0 * x[i]) * np.cos(15.0 * x[i])
        
        # Combined fitness value
        return radial_basin + periodic_waves + cross_coupling + interference + polynomial_smooth + adaptive_noise