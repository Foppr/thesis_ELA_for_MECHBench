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
            0.5 * np.sin(2**i * np.pi * r) * np.exp(-r**2 / (2 * (0.1 + i * 0.05)**2))
            for i in range(6)
        ])
        
        # Composite angular structure with self-similar patterns
        if self.dim == 1:
            angular = 0
        else:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular = np.sum([
                0.3 * np.sin(3**i * angles) * np.cos(2**i * angles) * 
                np.exp(-abs(angles) / (0.2 + i * 0.03))
                for i in range(5)
            ])
        
        # Multi-scale cross-dimensional interactions with varying coupling strengths
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for complexity control
                dist = np.abs(x_norm[i] - x_norm[j])
                cross += (np.sin(10 * (x_norm[i]**2 + x_norm[j]**2)) * 
                         np.cos(8 * (x_norm[i]**3 + x_norm[j]**3)) *
                         np.exp(-dist**2 / (0.5 + 0.1 * (i+j))) +
                         0.7 * np.sin(15 * (x_norm[i]**4 + x_norm[j]**4)) *
                         np.cos(12 * (x_norm[i]**5 + x_norm[j]**5)) *
                         np.exp(-dist**3 / (0.8 + 0.15 * (i+j))))
        
        # Adaptive noise with fractal characteristics and varying frequencies
        noise = np.sum([
            0.2 * np.sin(2**(i+1) * np.pi * x_norm) * 
            np.cos(3**(i+1) * np.pi * x_norm) * 
            np.exp(-np.abs(x_norm) / (0.1 + i * 0.02))
            for i in range(8)
        ])
        
        # Multi-scale periodic components with varying amplitudes and wavelengths
        periodic = np.sum([
            (0.5 / (i+1)) * np.sin((2**(i+2)) * np.pi * r) * 
            np.cos((2**(i+1)) * np.pi * r) * 
            np.exp(-r**2 / (2 * (0.3 + i * 0.05)**2))
            for i in range(4)
        ])
        
        # Adaptive conditioning based on dimensionality and position
        cond = 1.0 + 2.0 * np.exp(-self.dim / 5.0) * (1.0 + 0.5 * np.sin(r))
        
        # Combine all components with varying weights to create rugged terrain
        return cond * (fractal_radial + angular + cross + noise + periodic) * (1.0 + 0.2 * np.sin(3 * r))