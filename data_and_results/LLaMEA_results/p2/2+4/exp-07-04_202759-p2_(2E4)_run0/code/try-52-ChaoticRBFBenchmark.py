import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Dynamic polynomial component with varying exponents and chaotic scaling
        poly = 0
        for i in range(self.dim):
            exp = 3 + 2 * np.sin(0.3 * i)
            poly += (x[i]**exp) * (1 + 0.2 * np.sin(3 * x[i]))
        
        # Chaotic sine-wave interaction component with dynamic frequencies
        sine = 0
        for i in range(self.dim):
            freq = 4 + 3 * np.cos(0.5 * x[i])
            sine += np.sin(freq * x[i] + np.sin(2 * x[i])) * np.cos(freq * x[i] * 0.7)
        
        # Adaptive radial basis function with dynamic centers and widths
        rbf = 0
        for i in range(self.dim):
            center = 2 * np.sin(0.4 * i) * 4.5
            width = 0.5 + 0.3 * np.cos(0.6 * i)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.sin(5 * (x[i] - center))
        
        # Cross-term chaotic coupling with dynamic weights
        cross = 0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            weight = 1.5 + 0.8 * np.sin(0.7 * x[i])
            cross += weight * np.sin(2 * (x[i] + x[j])) * np.cos(3 * (x[i] - x[j]))
        
        # Multi-scale chaotic modulation component
        mod = 0
        for i in range(self.dim):
            mod += np.sin(x[i] * np.pi * (1 + 0.3 * np.sin(5 * x[i]))) * np.cos(x[i] * np.pi * (1 + 0.3 * np.cos(5 * x[i]))) * np.exp(-0.08 * x[i]**2)
        
        # Combine all components with adaptive weights
        return 0.3 * poly + 0.25 * sine + 0.2 * rbf + 0.15 * cross + 0.1 * mod