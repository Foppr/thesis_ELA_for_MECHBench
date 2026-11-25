import numpy as np

class FractalRuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base fractal-like radial component with chaotic scaling and multiple frequencies
        r = np.sqrt(np.sum(x_norm**2))
        fractal_radial = np.sum([
            0.8 * np.sin(2**(i+1) * np.pi * r) * np.cos(3**(i+1) * np.pi * r) * 
            np.exp(-r**2 / (2 * (0.05 + i * 0.03)**2))
            for i in range(8)
        ])
        
        # Composite angular structure with chaotic phase relationships and multi-scale correlations
        if self.dim == 1:
            angular = 0
        else:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular = np.sum([
                0.5 * np.sin(5**(i+1) * angles) * np.cos(4**(i+1) * angles) * 
                np.exp(-np.abs(angles) / (0.1 + i * 0.02))
                for i in range(7)
            ])
        
        # Multi-scale cross-dimensional interactions with chaotic coupling and dynamic strength
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended range for more complexity
                dist = np.abs(x_norm[i] - x_norm[j])
                cross += (np.sin(20 * (x_norm[i]**2 + x_norm[j]**2)) * 
                         np.cos(15 * (x_norm[i]**3 + x_norm[j]**3)) *
                         np.exp(-dist**2 / (0.3 + 0.05 * (i+j))) +
                         0.9 * np.sin(25 * (x_norm[i]**4 + x_norm[j]**4)) *
                         np.cos(20 * (x_norm[i]**5 + x_norm[j]**5)) *
                         np.exp(-dist**3 / (1.0 + 0.2 * (i+j))) +
                         0.6 * np.sin(30 * (x_norm[i]**6 + x_norm[j]**6)) *
                         np.cos(25 * (x_norm[i]**7 + x_norm[j]**7)) *
                         np.exp(-dist**4 / (0.8 + 0.15 * (i+j))))
        
        # Chaotic noise with fractal characteristics and unpredictable frequency spectrum
        noise = np.sum([
            0.3 * np.sin(2**(i+2) * np.pi * x_norm) * 
            np.cos(5**(i+2) * np.pi * x_norm) * 
            np.exp(-np.abs(x_norm) / (0.05 + i * 0.01))
            for i in range(10)
        ])
        
        # Multi-scale periodic components with chaotic amplitude modulation and wavelength variation
        periodic = np.sum([
            (1.0 / (i+1)) * np.sin((2**(i+3)) * np.pi * r) * 
            np.cos((3**(i+2)) * np.pi * r) * 
            np.exp(-r**2 / (2 * (0.2 + i * 0.04)**2))
            for i in range(6)
        ])
        
        # Dynamic conditioning with chaotic behavior and multi-scale adaptation
        cond = 1.5 + 3.0 * np.exp(-self.dim / 7.0) * (1.0 + 0.8 * np.sin(r**2)) * np.cos(r)
        
        # Combine all components with chaotic weights to create extreme ruggedness
        return cond * (fractal_radial + angular + cross + noise + periodic) * (1.0 + 0.5 * np.sin(5 * r) * np.cos(3 * r))