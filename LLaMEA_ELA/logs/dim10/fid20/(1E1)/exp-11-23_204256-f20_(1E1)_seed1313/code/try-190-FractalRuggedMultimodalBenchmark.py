import numpy as np

class FractalRuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base fractal-like radial component with multiple scales
        r = np.sqrt(np.sum(x_norm**2))
        fractal_radial = np.sum([
            0.6 * np.sin(2**i * np.pi * r) * np.exp(-r**2 / (2 * (0.1 + i * 0.07)**2))
            for i in range(7)
        ])
        
        # Composite angular structure with self-similar patterns
        if self.dim == 1:
            angular = 0
        else:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular = np.sum([
                0.4 * np.sin(3**i * angles) * np.cos(2**i * angles) * 
                np.exp(-abs(angles) / (0.25 + i * 0.04))
                for i in range(6)
            ])
        
        # Multi-scale cross-dimensional interactions with varying coupling strengths
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Slightly increased interaction range
                dist = np.abs(x_norm[i] - x_norm[j])
                cross += (np.sin(12 * (x_norm[i]**2 + x_norm[j]**2)) * 
                         np.cos(10 * (x_norm[i]**3 + x_norm[j]**3)) *
                         np.exp(-dist**2 / (0.4 + 0.1 * (i+j))) +
                         0.8 * np.sin(18 * (x_norm[i]**4 + x_norm[j]**4)) *
                         np.cos(15 * (x_norm[i]**5 + x_norm[j]**5)) *
                         np.exp(-dist**3 / (0.7 + 0.2 * (i+j))))
        
        # Adaptive noise with fractal characteristics and varying frequencies
        noise = np.sum([
            0.25 * np.sin(2**(i+1) * np.pi * x_norm) * 
            np.cos(3**(i+1) * np.pi * x_norm) * 
            np.exp(-np.abs(x_norm) / (0.12 + i * 0.025))
            for i in range(9)
        ])
        
        # Multi-scale periodic components with varying amplitudes and wavelengths
        periodic = np.sum([
            (0.6 / (i+1)) * np.sin((2**(i+2)) * np.pi * r) * 
            np.cos((2**(i+1)) * np.pi * r) * 
            np.exp(-r**2 / (2 * (0.35 + i * 0.06)**2))
            for i in range(5)
        ])
        
        # Adaptive conditioning based on dimensionality and position with increased complexity
        cond = 1.0 + 2.5 * np.exp(-self.dim / 4.0) * (1.0 + 0.6 * np.sin(r))
        
        # Combine all components with varying weights to create rugged terrain
        return cond * (fractal_radial + angular + cross + noise + periodic) * (1.0 + 0.3 * np.sin(4 * r))