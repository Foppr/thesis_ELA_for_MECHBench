import numpy as np

class PeriodicBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Periodic trigonometric components with varying frequencies and amplitudes
        periodic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            amp = 1.5 + 0.5 * np.cos(i * 0.3)
            periodic += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Exponential barrier functions with dynamic positions and steepness
        barriers = 0.0
        for i in range(self.dim):
            # Multiple exponential barriers with varying strengths and positions
            pos1 = 0.5 * np.sin(i * 0.7) + 0.2
            pos2 = -0.5 * np.cos(i * 0.9) - 0.3
            strength1 = 2.0 + 1.0 * np.sin(i * 0.4)
            strength2 = 1.5 + 0.8 * np.cos(i * 0.6)
            
            barrier1 = strength1 * np.exp(-5.0 * (x_scaled[i] - pos1)**2)
            barrier2 = strength2 * np.exp(-7.0 * (x_scaled[i] - pos2)**2)
            barriers += barrier1 + barrier2
        
        # Cross-dimensional coupling with interaction terms that create complex valleys
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction strength decreases with distance and includes chaotic modulation
                dist = np.abs(x_scaled[i] - x_scaled[j])
                mod = np.sin(0.3 * i + 0.4 * j) * np.cos(0.2 * i - 0.5 * j)
                coupling += (1.0 / (1.0 + dist**2)) * np.sin(3.0 * (x_scaled[i] + x_scaled[j])) * mod
        
        # Polynomial landscape with chaotic coefficients and exponential scaling
        poly = 0.0
        for i in range(self.dim):
            coeff1 = 1.0 + 0.5 * np.sin(i * 0.8)
            coeff2 = 0.8 + 0.3 * np.cos(i * 0.6)
            poly += coeff1 * x_scaled[i]**4 + coeff2 * x_scaled[i]**3
        
        # Combined function with carefully balanced components
        return 0.8 * periodic + 1.5 * barriers + 1.2 * coupling + 0.9 * poly