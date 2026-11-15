import numpy as np

class PeriodicAsymmetricSaddle:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base periodic component with varying frequencies and amplitudes
        f = 0.0
        for i in range(self.dim):
            freq = 2 + i * 0.5
            amp = 1.0 + 0.2 * np.sin(i * 0.3)
            f += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
            
        # Asymmetric saddle points with directional bias
        for i in range(self.dim):
            # Quadratic terms with asymmetric coefficients
            a = 0.5 + 0.3 * np.sin(i * 0.7)
            b = 0.3 + 0.2 * np.cos(i * 1.1)
            c = 0.1 + 0.1 * np.sin(i * 0.9)
            f += a * x[i]**2 + b * x[i] + c
            
        # Multi-modal structure with periodic peaks
        for i in range(self.dim):
            f += 0.5 * np.sin(10 * x[i]) * np.cos(15 * x[i]) + 0.3 * np.sin(20 * x[i])
            
        # Dynamic coupling between dimensions with varying weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = 0.3 * np.sin(i * 0.5) * np.cos(j * 0.4) + 0.2 * np.sin(i * j * 0.1)
                coupling += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        f += coupling
        
        # Fractal-like complexity with recursive structure
        for i in range(self.dim):
            f += 0.1 * np.sin(31 * x_norm[i]) * np.cos(37 * x_norm[i]) * np.sin(41 * x_norm[i])
            
        # Chaotic modulation with exponential decay
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.exp(-0.1 * x[i]**2) * np.sin(43 * x_norm[i]) * np.cos(47 * x_norm[i])
        f += 0.2 * chaos
        
        # Subspace complexity variation
        for i in range(self.dim):
            if i % 3 == 0:
                f += 0.15 * x[i]**4
            elif i % 3 == 1:
                f += 0.1 * np.abs(x[i])**1.5
            else:
                f += 0.05 * np.tanh(x[i])**2
                
        # Additional noise and irregularity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(53 * x_norm[i]) + 0.03 * np.cos(59 * x_norm[i])
        f += noise
        
        return f