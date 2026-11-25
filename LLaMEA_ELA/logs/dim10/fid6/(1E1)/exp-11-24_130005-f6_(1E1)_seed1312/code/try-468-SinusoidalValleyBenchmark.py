import numpy as np

class SinusoidalValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Periodic sinusoidal components with varying frequencies and amplitudes
        periodic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * x_scaled[i])
            amp = 1.5 + 2.0 * np.cos(0.7 * x_scaled[i])
            periodic += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.6)
        
        # Exponential decay interactions between dimensions
        decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                weight = 1.0 / (1.0 + dist**2)
                decay += weight * np.exp(-dist * 2.0) * np.sin(3.0 * (x_scaled[i] + x_scaled[j]))
        
        # Gradient-based attraction fields with multiple local minima
        attraction = 0.0
        for i in range(self.dim):
            # Multiple attraction centers with varying strengths and positions
            center1 = 0.5 * np.sin(0.3 * x_scaled[i])
            center2 = -0.5 * np.cos(0.4 * x_scaled[i])
            strength1 = 1.0 + 0.5 * np.sin(0.6 * x_scaled[i])
            strength2 = 1.0 + 0.3 * np.cos(0.8 * x_scaled[i])
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            attraction += strength1 * np.exp(-dist1 * 0.5) + strength2 * np.exp(-dist2 * 0.7)
        
        # Ridge and valley structure with hyperbolic tangent modulation
        structure = 0.0
        for i in range(self.dim):
            ridge = np.tanh(2.0 * x_scaled[i]) * np.sin(4.0 * x_scaled[i])
            valley = np.tanh(3.0 * x_scaled[i]) * np.cos(2.0 * x_scaled[i])
            structure += ridge + valley
        
        # Combined function with weighted components
        return 1.5 * periodic + 1.2 * decay + 0.8 * attraction + 1.0 * structure