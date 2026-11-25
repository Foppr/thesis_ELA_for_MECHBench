import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic sinusoidal components with adaptive frequencies
        periodic = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.2 * i) + 0.3 * np.cos(0.1 * i**2)
            periodic += np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Adaptive radial basis functions with dimension-dependent widths
        rbf = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                width = 0.5 + 0.5 * (i + j) / self.dim
                rbf += np.exp(-0.5 * (dist / width)**2) * np.sin(dist)
        
        # Cross-dimensional polynomial coupling with varying exponents
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_i = 1.0 + 0.3 * np.sin(0.1 * i)
                exp_j = 1.0 + 0.3 * np.cos(0.1 * j)
                poly_coupling += (x[i]**exp_i + x[j]**exp_j) * np.tanh(x[i] * x[j])
        
        # Condition number modulation with sine-based scaling
        cond_mod = 0
        for i in range(self.dim):
            cond_mod += (1.0 + 0.5 * np.sin(0.3 * x[i])) * x[i]**2
        
        # Noise component with dimensionally varying intensity
        noise = 0
        for i in range(self.dim):
            noise += 0.1 * np.sin(10 * x[i]) * np.cos(8 * x[i]) * (1.0 + 0.2 * np.sin(i))
        
        # Scaling factor based on dimensionality and sinusoidal modulation
        scale = 1.0 + 0.2 * np.sin(self.dim * 0.1) + 0.1 * np.cos(self.dim * 0.05)
        
        # Combine all components with optimized weights
        return scale * (0.4 * periodic + 0.3 * rbf + 0.2 * poly_coupling + 
                       0.08 * cond_mod) + noise