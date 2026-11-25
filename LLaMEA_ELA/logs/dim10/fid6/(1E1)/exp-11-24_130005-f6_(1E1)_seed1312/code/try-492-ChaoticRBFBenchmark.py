import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Periodic trigonometric components with varying frequencies and amplitudes
        periodic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.5 + 0.5 * np.cos(0.3 * i)
            periodic += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Radial basis functions with exponentially decaying weights and chaotic centers
        rbf = 0.0
        for i in range(self.dim):
            # Chaotic center positions
            center = np.sin(0.4 * i + 0.3 * np.cos(x_scaled[i])) * 0.8
            weight = 2.0 * np.exp(-0.5 * i)
            rbf += weight * np.exp(-10.0 * (x_scaled[i] - center)**2)
        
        # Cross-dimensional coupling with chaotic interaction terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling strength and phase
                strength = 1.0 + 0.5 * np.sin(0.3 * i + 0.4 * j)
                phase = np.sin(0.2 * x_scaled[i] + 0.3 * x_scaled[j]) * \
                       np.cos(0.4 * x_scaled[i] - 0.2 * x_scaled[j])
                coupling += strength * phase * \
                           np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Multi-scale harmonic components with varying decay rates
        multiscale = 0.0
        scales = [1, 2, 3, 4, 5]
        for scale in scales:
            for i in range(self.dim):
                multiscale += np.sin(scale * x_scaled[i]) * \
                             np.exp(-scale * np.abs(x_scaled[i]))
        
        # Complex curvature with sigmoidal transitions and chaotic modulation
        curvature = 0.0
        for i in range(self.dim):
            # Sigmoidal transitions with chaotic boundary positions
            pos1 = 0.2 * np.sin(0.5 * i)
            pos2 = -0.2 * np.cos(0.3 * i)
            sig1 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] - pos1)))
            sig2 = 1.0 / (1.0 + np.exp(-20.0 * (x_scaled[i] + pos2)))
            curvature += (sig1 - 0.5)**4 + (sig2 - 0.5)**4
        
        # Combine all components with modified weights
        return 1.5 * periodic + 2.0 * rbf + 1.3 * coupling + 0.8 * multiscale + 1.2 * curvature