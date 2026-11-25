import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with varying degrees and adaptive coefficients
        polynomial = 0
        for i in range(self.dim):
            coef = 1.0 + 0.3 * np.sin(0.5 * i)
            polynomial += coef * (x[i] ** 3) + 0.8 * (x[i] ** 2) - 1.2 * x[i]
        
        # Trigonometric components with frequency modulation and phase shifts
        trig = 0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.cos(0.3 * i)
            phase = 0.2 * np.sin(0.4 * i)
            trig += 1.5 * np.sin(freq * x[i] + phase) + 0.9 * np.cos(freq * x[i] + phase)
        
        # Radial basis function terms with adaptive centers and widths
        rbf = 0
        for i in range(self.dim):
            center = -2.0 + 4.0 * (i / self.dim)
            width = 0.5 + 0.3 * np.sin(0.6 * i)
            rbf += 2.0 * np.exp(-0.5 * ((x[i] - center) / width) ** 2)
        
        # Interaction terms with distance-dependent coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                coupling = 1.0 + 0.5 * np.sin(0.7 * (i + j))
                interaction += coupling * np.sin(3.0 * dist) / (dist + 0.1)
        
        # Adaptive global scaling factor
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * 0.1)
        
        return scale_factor * (polynomial + trig + rbf + 0.3 * interaction) + 20.0 * self.dim