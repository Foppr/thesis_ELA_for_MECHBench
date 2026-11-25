import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Multi-peak sinusoidal landscape with dynamic scaling
        peaks = 0.0
        for i in range(self.dim):
            freq = 3 + 2 * np.sin(0.3 * x_norm[i])
            peaks += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2)
        
        # Composite chaotic modulation with exponential decay
        chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                chaos += np.sin(10 * dist) * np.cos(7 * dist) * np.exp(-0.2 * dist**2)
        
        # Adaptive polynomial coupling with dynamic exponents
        poly_coupling = 0.0
        for i in range(self.dim):
            exp_factor = 2 + 0.5 * np.sin(3 * x_norm[i])
            poly_coupling += x_norm[i]**exp_factor * (1 + 0.3 * np.cos(5 * x_norm[i]))
        
        # Dynamic saddle-point repulsion field
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x_norm[i]**2 - 1)**2 * np.exp(-0.5 * x_norm[i]**2)
        
        # Radial fractal component with multi-scale interference
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sin(12 * r) * np.cos(9 * r) * np.exp(-0.4 * r**2)
        
        # Adaptive noise with position-dependent amplitude
        noise = 0.0
        for i in range(self.dim):
            amp = 0.2 * (1 + 0.5 * np.sin(4 * x_norm[i]))
            noise += amp * np.sin(15 * x_norm[i]) * np.cos(8 * x_norm[i])
        
        # Combined landscape with global scaling
        return 1.5 * (peaks + chaos + poly_coupling + saddle + radial + noise)