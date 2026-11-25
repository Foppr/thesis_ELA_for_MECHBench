import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Periodic sinusoidal components with varying frequencies and amplitudes
        periodic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.5 + 0.5 * np.cos(0.3 * i)
            periodic += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Polynomial interaction terms with mixed degrees
        polynomial = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                poly_term = (x_scaled[i]**2 + x_scaled[j]**3) * np.sin(0.5 * (x_scaled[i] + x_scaled[j]))
                polynomial += poly_term
        
        # Radial basis functions with exponentially decaying weights and dynamic centers
        radial = 0.0
        for i in range(self.dim):
            center = np.sin(0.4 * i) * 0.8
            weight = 2.0 * np.exp(-0.5 * i)
            radial += weight * np.exp(-5.0 * (x_scaled[i] - center)**2)
        
        # Cross-dimensional coupling with chaotic phase shifts and exponential scaling
        coupling = 0.0
        for i in range(self.dim):
            phase_shift = np.sin(0.3 * x_scaled[i]) * np.cos(0.2 * x_scaled[i])
            coupling += np.exp(-0.1 * np.abs(x_scaled[i])) * phase_shift
        
        # Multi-scale harmonic interference with varying amplitudes and frequencies
        interference = 0.0
        for scale in [1, 2, 3, 4, 5]:
            for i in range(self.dim):
                interference += np.sin(scale * x_scaled[i] + 0.1 * scale * np.cos(scale * x_scaled[i])) * \
                              np.cos(scale * x_scaled[i] * 0.8) * \
                              np.exp(-0.3 * scale)
        
        # Combined function with weighted components
        return 1.5 * periodic + 0.8 * polynomial + 1.2 * radial + 0.9 * coupling + 1.1 * interference